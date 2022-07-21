import pandas as pd
from psycopg2 import Date
import datetime
from sqlalchemy import update, cast , Date
from flask import redirect, render_template, request, flash, session, url_for

from covid_app import app , db

from covid_app.models import Users,Hospitals,Patients

from covid_app.forms import AdminLogin, AddUser, AddHospital, HospitalUpdate,VaccinationStatus,AddPatient, UpdatePatientLogin, UpdatePatientStatus


@app.before_first_request
def populate_db():
    if Users.query.filter_by(is_admin = True).first() is None:
        admin = Users(username = "admin", password = "12345", is_admin = True)
        db.session.add(admin)
        db.session.commit()


@app.route('/', methods = ['POST','GET'])
def home():
    
    """confirmed = Patients.query.filter_by(TestResult = '+ve').count()
    print('Confirmed',"-->",confirmed)
    active = Patients.query.filter_by(Status = '+ve').count()
    print('Active',"-->",active)
    Recovered = Patients.query.filter_by(TestResult = '+ve', Status = '-ve').count()
    print('Recovered',"-->",Recovered)
    Deceased = Patients.query.filter_by(Status = 'Deceased').count()
    print('Deceased',"-->",Deceased)"""

    return render_template("home.html")


@app.route('/admin', methods = ['POST','GET'])
def admin():
    form = AdminLogin()    

    if request.method == 'POST' and form.validate_on_submit():
    
        if Users.query.filter_by(username = form.username.data,password = form.password.data, is_admin = True).first():
            return redirect(url_for('hospitals'))
        elif Users.query.filter_by(username = form.username.data,password = form.password.data, is_admin = False).first():
            session['username']  = form.username.data
            session['password']  = form.password.data
            return redirect(url_for('details'))
        else:
            return redirect(url_for('admin'))
               
    return render_template('admin_login.html', **locals())   



@app.route('/hospitals', methods = ['POST','GET','PUT'])
def hospitals():

    result1 = Users.query.filter_by(is_admin = False,is_deleted = False).all()   
    result2 = db.session.query(Hospitals, Users).join(Users).filter(Hospitals.is_deleted == False).all()
    
    user_list =[]
    for user in result1:
        user_dict =  {
                'pk': user.id,
                'name' : user.username    
            }
        user_list.append(user_dict)
    user_df = pd.DataFrame(user_list)

    hospital_list = []    
    for hospital, user in result2:        
            hospital_dict=  {
                'pk': hospital.id,
                'name' : hospital.hospital_name,
                'contact' : hospital.contact_number,
                'user' : user.username,
                'is_deleted': user.is_deleted
            }
            hospital_list.append(hospital_dict)    
    hospital_df = pd.DataFrame(hospital_list) 
    
           

    return render_template("hospitals.html",**locals())  


@app.route('/adduser', methods = ['POST','GET'])
def add_user():
    form = AddUser()

    if form.validate_on_submit():
        exists = db.session.query(Users.id).filter_by(username = form.username.data,password = form.password.data).first()
        if exists:
            print(exists)
            id = int(exists[0])
            print(id)
        
            db.session.query(Users).filter(Users.id == id).update({Users.is_deleted : False}, synchronize_session = False)
            db.session.commit()
        else:    
            user = Users(username = form.username.data,password = form.password.data, is_admin = False)
            db.session.add(user)
            db.session.commit()
        

        return redirect(url_for('hospitals')) 
           

    return render_template("adduser.html",**locals())   
    
    
    
@app.route('/addhosp', methods = ['POST','GET'])
def add_hospital():
    form = AddHospital()
    users = Users.query.with_entities(Users.username).filter_by(is_admin = False,is_deleted = False).all()
    users_list = [r for (r, ) in users]
    form.user.choices = users_list
    print(users_list)

    if form.validate_on_submit():
        user_admin = Users.query.filter_by(username = form.user.data).first()
        #print(form.hospital_name.data, form.contact_number.data, form.user.data)
        hospital = Hospitals(hospital_name = form.hospital_name.data, contact_number = form.contact_number.data, users = user_admin)
        db.session.add(hospital)
        db.session.commit()
        return redirect(url_for('hospitals'))

    return render_template("addhospital.html",**locals())   



@app.route("/deletehospital/<int:hospid>")
def DeleteHospital(hospid):
    db.session.query(Hospitals).filter(Hospitals.id == hospid).update({Hospitals.is_deleted : True}, synchronize_session = False)
    db.session.commit()
    return redirect(url_for('hospitals'))


@app.route("/deleteuser/<int:userid>")
def DeleteUser(userid):
    db.session.query(Users).filter(Users.id == userid).update({Users.is_deleted : True}, synchronize_session = False)
    db.session.query(Hospitals).filter(Hospitals.user_id == userid).update({Hospitals.is_deleted : True}, synchronize_session = False)

    db.session.commit()
    return redirect(url_for('hospitals'))



@app.route('/details', methods = ['POST','GET'])
def details():
    """Hospital_Name = session['hospital_name'] """

    return render_template("details.html" , **locals())     



@app.route('/updHospDetails', methods = ['POST','GET'])
def Updatehospital():
    """form = HospitalUpdate()
    user = session['username'] 
    Hospital_Name = session['hospital_name']
    
    if form.validate_on_submit():       
        db.session.query(Hospitals).filter(Hospitals.Username == user).update({Hospitals.TotalCapacity : form.TotalCapacity.data, Hospitals.ICU_Beds : form.ICU_Beds.data}, synchronize_session = False)
        db.session.commit()
        return redirect(url_for('details'))"""

    return render_template("UpdateHospital.html", **locals())


@app.route('/addpatient', methods = ['POST','GET'])
def addpatient():
    """form = AddPatient()
    user = session['username']
    Hospital_Name = session['hospital_name'] 

    if form.validate_on_submit():
        Hosp = Hospitals.query.filter_by(Username = user).first()
        patient = Patients(Fname = form.Fname.data, Lname = form.Lname.data, Date = datetime.datetime.now(), DOB = form.DOB.data, Age = (datetime.datetime.now().year- form.DOB.data.year),  Gender = form.Gender.data, TestResult = form.TestResult.data, Status = form.TestResult.data ,hospitals = Hosp)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('details'))"""

    return render_template("add_patient.html", **locals())



@app.route('/vaccinationStatus', methods = ['POST','GET'])
def UpdateVaccine():
    """form = VaccinationStatus()
    user = session['username'] 
    Hospital_Name = session['hospital_name'] 

    if form.validate_on_submit():
        db.session.query(Hospitals).filter(Hospitals.Username == user).update({Hospitals.First_Dose : form.FirstDose.data, Hospitals.Second_Dose : form.SecondDose.data,Hospitals.Precautionary_Dose : form.PrecautionaryDose.data}, synchronize_session = False)
        db.session.commit()
        return redirect(url_for('details'))"""
    
    return render_template("updatevaccine.html" ,  **locals())   


@app.route('/updpatientstatus', methods = ['POST','GET'])
def UpdatePatientLog():
    """form = UpdatePatientLogin()
    hosp_id = session['id']
    Hospital_Name = session['hospital_name'] 
    
    if form.validate_on_submit():
        Fname_Lname_DOB = Patients.query.with_entities(Patients.Fname, Patients.Lname, Patients.DOB, Patients.id, Patients.Status).filter_by(Hosp_id = hosp_id).all()
        
        for item in Fname_Lname_DOB:
            if ((item[0] == form.Fname.data) and (item[1] == form.Lname.data) and (item[2].date() == form.DOB.data)):
                session['patient_Fname'] = item[0]
                session['patient_Lname'] = item[1]
                session['patient_id'] = item[3]
                session['status'] = item[4]

                return redirect(url_for('statusupdate'))
        else:
            flash('Enter correct values')
            return redirect(url_for('UpdatePatientLog'))    """

    return render_template("UpdatePatientLogin.html", **locals())


@app.route('/statusupdate', methods = ['POST','GET'])
def statusupdate():
    """form = UpdatePatientStatus()
    
    patient_Fname=session['patient_Fname'] 
    patient_Lname= session['patient_Lname']
    status = session['status']
    patient_id = session['patient_id']
    Hospital_Name = session['hospital_name'] 

    
    if request.method == 'POST' and form.validate_on_submit():
        if form.Status.data == '+ve':
            db.session.query(Patients).filter(Patients.id == patient_id).update({Patients.Status : form.Status.data, Patients.TestResult : form.Status.data}, synchronize_session = False)
            db.session.commit()
            return redirect(url_for('details'))
        elif form.Status.data == 'Recovered':
            db.session.query(Patients).filter(Patients.id == patient_id).update({Patients.Status : '-ve'}, synchronize_session = False)
            db.session.commit()
            return redirect(url_for('details'))
        elif form.Status.data == 'Deceased':
            db.session.query(Patients).filter(Patients.id == patient_id).update({Patients.Status : 'Deceased'}, synchronize_session = False)
            db.session.commit()
            return redirect(url_for('details'))   """ 
        
    
    return render_template("StatusUpdate.html" ,  **locals())











"""
admin_name,admin_password) = Users.query.with_entities(Users.username,Users.password).filter_by(is_admin = True).first()
    

    if request.method == 'POST' and form.validate_on_submit():
        users = Users.query.with_entities(Users.id,Users.username,Users.password).filter_by(is_admin = False, username = form.username.data).first()
        print(users)
        if result:
            (id,hospital_name,username,password) = result
        if form.username.data == admin_name and form.password.data == admin_password:
            return redirect(url_for('hospitals'))
        elif users and form.password.data == password:
            session['id']  = id
            session['hospital_name']  = hospital_name
            session['username']  = username
            session['password']  = password
            return redirect(url_for('details'))
        else:
            return redirect(url_for('admin'))


"""









