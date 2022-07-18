import pandas as pd
from psycopg2 import Date
import datetime
from sqlalchemy import update, cast , Date
from flask import redirect, render_template, request, flash, session, url_for

from covid_app import app , db

from covid_app.models import Users,Hospitals,Patients

from covid_app.forms import AdminLogin, HospitalUpdate, NewHospital,VaccinationStatus,AddPatient, UpdatePatientLogin, UpdatePatientStatus


@app.before_first_request
def populate_db():
    admin = Users(username = "admin", password = "123", is_admin = True)
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

    """if request.method == 'POST' and form.validate_on_submit():
        result = Hospitals.query.with_entities(Hospitals.id,Hospitals.HospitalName, Hospitals.Username, Hospitals.Password ).filter_by(Username = form.username.data).first()
        if result:
            (id,hospital_name,username,password) = result
        if form.username.data == "admin" and form.password.data == "123":
            return redirect(url_for('hospitals'))
        elif result and form.password.data == password:
            session['id']  = id
            session['hospital_name']  = hospital_name
            session['username']  = username
            session['password']  = password
            return redirect(url_for('details'))
        else:
            return redirect(url_for('admin'))"""
               
    return render_template('adminlogin.html', **locals())   



@app.route('/hospitals', methods = ['POST','GET'])
def hospitals():
       
    """Hospital = Hospitals.query.all()
 
    list_out = []
    for item in Hospital:        
            dict_out =  {
                'pk': item.id,
                'Name' : item.HospitalName,
                'Contact' : item.ContactNumber
            }
            list_out.append(dict_out)
       
    
    panda_out = pd.DataFrame(list_out) """
           

    return render_template("Hospitals.html", )  
    
    
@app.route('/addnew', methods = ['POST','GET'])
def add_hospital():
    """form = NewHospital()

    if form.validate_on_submit():
        NewHosp = Hospitals(HospitalName = form.HospitalName.data, ContactNumber = form.ContactNumber.data, Username = form.Username.data, Password = form.Password.data)
        db.session.add(NewHosp)
        db.session.commit()
        return redirect(url_for('hospitals'))"""

    return render_template("add_hospital.html",**locals())   



@app.route("/HospDelete/<int:hospid>")
def HospDelete(hospid):
    """Delhosp = Hospitals.query.get(hospid)
    db.session.delete(Delhosp)
    db.session.commit()"""
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























