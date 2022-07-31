import pandas as pd
from psycopg2 import Date
import datetime
from sqlalchemy import update, cast , Date, desc
from flask import redirect, render_template, request, flash, session, url_for

from covid_app import app , db
from covid_app.models import Users,Hospitals,Patients,CovidTest
from covid_app.forms import AdminLogin, AddUser, AddHospital, HospitalBeds,VaccinationStatus,AddPatient,UpdatePatientStatus


@app.before_first_request
def populate_db():
    if Users.query.filter_by(is_admin = True).first() is None:
        admin_password = "admin123"
        admin_password_hash = encrypt(admin_password)
        admin = Users(username = "admin",password = admin_password_hash, is_admin = True)
        db.session.add(admin)
        db.session.commit()

def encrypt(id):
    s = 28
    result = ""   
    for i in range(len(id)):
        char = id[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)           
    return result


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
        
        password_hash = encrypt(str(form.password.data))
        #adminlog = Users.query.filter_by(username = form.username.data, password = password_hash, is_admin = True).first()
        #userlog = Users.query.filter_by(username = form.username.data,password = password_hash, is_admin = False).first()

        if Users.query.filter_by(username = form.username.data, password = password_hash, is_admin = True).first():
            return redirect(url_for('hospitals'))
        elif Users.query.filter_by(username = form.username.data,password = password_hash, is_admin = False).first():
            session['username']  = form.username.data
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
        password_hash = encrypt(str(form.password.data))
        if Users.query.filter_by(username = form.username.data, password = password_hash).all():
            exists = Users.query.filter_by(username = form.username.data, password = password_hash).one()
            id = exists.id
            db.session.query(Users).filter(Users.id == id).update({Users.is_deleted : False}, synchronize_session = False)
            db.session.commit()
        else:    
            user = Users(username = form.username.data,password = password_hash, is_admin = False)
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
        print(user_admin.id)
        exists = db.session.query(Hospitals.id).filter_by(hospital_name = form.hospital_name.data,contact_number = form.contact_number.data, user_id = user_admin.id).first()
        if exists:
            id = int(exists[0])        
            db.session.query(Hospitals).filter(Hospitals.id == id).update({Hospitals.is_deleted : False}, synchronize_session = False)
            db.session.commit()

        else:
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
    username = session['username']
    print(username)
    result = db.session.query(Hospitals, Users).join(Users).filter(Hospitals.is_deleted == False, Users.username == username).all()
    hospital_list = []
    for hospital,user in result:        
            hospital_dict=  {
                'pk': hospital.id,
                'name' : hospital.hospital_name,
                'contact' : hospital.contact_number
            }
            hospital_list.append(hospital_dict) 
    """Hospital_Name = session['hospital_name'] """

    return render_template("details.html" , **locals())     

@app.route("/updatehospital/<int:hospital_id>")
def update_hospital(hospital_id):
    
    session['hospital_id'] = hospital_id
    hospital = Hospitals.query.with_entities(Hospitals.hospital_name).filter_by(id = hospital_id, is_deleted = False).one()
    hospital_name = hospital.hospital_name
    session['hospital_name'] = hospital_name

    return render_template("update_hospital.html", **locals())    



@app.route('/patients', methods = ['POST','GET'])
def patients():
    hospital_id = session['hospital_id']
    hospital_name = session['hospital_name']

    result = db.session.query(CovidTest, Patients).join(Patients).filter(CovidTest.hospital_id == hospital_id).distinct(Patients.id).all()

    patient_list = []
    for test,patients in result:        
            patient=  {
                'pk' : patients.id,
                'date_added' : test.date_added,
                'first_name' : patients.first_name,
                'last_name': patients.last_name,
                'age': patients.age,
                'dob': patients.dob.date(),
                'gender': patients.gender,
                'status': patients.status           
            }
            patient_list.append(patient) 
    if patient_list:        
        patient_df = pd.DataFrame(patient_list).sort_values(by='date_added',ascending=False ) 
 
    return render_template("patients.html", **locals())


@app.route("/patientdisplay/<int:patient_pk>", methods = ['GET','POST'])
def patient_display(patient_pk):
    form  = UpdatePatientStatus()

    patient_id = patient_pk
    session['patient_id'] = patient_id
    hospital_id = session['hospital_id']
    hospital_name = session['hospital_name']
    hospital = Hospitals.query.filter_by(id = hospital_id).one()
    patient = Patients.query.filter_by(id = patient_id).one()

    patient_first_name = patient.first_name
    patient_last_name = patient.last_name
    patient_dob = patient.dob.date()
    patient_age = patient.age
    patient_gender = patient.gender
    patient_status = patient.status

    if request.method == "POST":
        status = request.form.get('status')
        #print(select)
        db.session.query(Patients).filter(Patients.id == patient_id).update({Patients.status : status}, synchronize_session = False)
        db.session.query(CovidTest).filter(CovidTest.patient_id == patient_id).update({CovidTest.is_current : False}, synchronize_session = False)            
        db.session.commit()
        if patient_status == "positive" and status == "negative":                  
            test = CovidTest(test_result = status, is_recovered = True, date_added = datetime.datetime.now(),hospital_test = hospital, patient_test = patient )
            db.session.add(test)
            db.session.commit()
        
        elif status == "deceased":
            test = CovidTest(test_result = status,is_deceased = True,date_added = datetime.datetime.now(),hospital_test = hospital, patient_test = patient )
            db.session.add(test)
            db.session.commit()

        else: 
            test = CovidTest(test_result = status,date_added = datetime.datetime.now(),hospital_test = hospital, patient_test = patient )
            db.session.add(test)
            db.session.commit() 

            

        return redirect(url_for('patients'))  

    return render_template("patient_display.html", **locals())



@app.route('/addpatient', methods = ['POST','GET'])
def add_patient():
    form = AddPatient()
    hospital_id = session['hospital_id']
    hospital_name = session['hospital_name']
    hospital = Hospitals.query.filter_by(id = hospital_id).one()
    
    if form.validate_on_submit():
        unique_id_hash = encrypt(str(form.unique_id.data))
    
        if Patients.query.filter_by(first_name = form.first_name.data, last_name = form.last_name.data,dob = form.dob.data,unique_id = unique_id_hash, gender = form.gender.data).all():
            exists = Patients.query.filter_by(first_name = form.first_name.data, last_name = form.last_name.data,dob = form.dob.data,unique_id = unique_id_hash).one()
            id = exists.id
            status = exists.status
            if status == "positive" and form.test_result.data == "negative":
                db.session.query(Patients).filter(Patients.id == id).update({Patients.status : form.test_result.data}, synchronize_session = False)            
                db.session.query(CovidTest).filter(CovidTest.patient_id == id).update({CovidTest.is_current : False}, synchronize_session = False)            
                test = CovidTest(test_result = form.test_result.data, is_recovered = True , date_added = datetime.datetime.now(),hospital_test = hospital, patient_test = exists )
                db.session.add(test)
                db.session.commit()
            else: 
                db.session.query(Patients).filter(Patients.id == id).update({Patients.status : form.test_result.data}, synchronize_session = False)            
                db.session.query(CovidTest).filter(CovidTest.patient_id == id).update({CovidTest.is_current : False}, synchronize_session = False)            
                test = CovidTest(test_result = form.test_result.data,  date_added = datetime.datetime.now(),hospital_test = hospital, patient_test = exists )
                db.session.add(test)
                db.session.commit() 

        else:
            if Patients.query.filter_by(unique_id = unique_id_hash).first():
                flash('Unique id already exists!!!')
                return redirect(url_for('patients'))
            else:    
                patient = Patients(first_name = form.first_name.data, last_name = form.last_name.data, dob = form.dob.data,unique_id = unique_id_hash, age = (datetime.datetime.now().year- form.dob.data.year), gender = form.gender.data, status = form.test_result.data)
                db.session.add(patient)
                db.session.commit()
                test = CovidTest(test_result = form.test_result.data, date_added = datetime.datetime.now(),hospital_test = hospital, patient_test = patient )
                db.session.add(test)
                db.session.commit() 

        return redirect(url_for('patients'))
    

    return render_template("add_patient.html", **locals())




@app.route('/hospitalbeds', methods = ['POST','GET'])
def hospital_beds():
    form = HospitalBeds()

    hospital_id = session['hospital_id']
    hospital_name = session['hospital_name']
    hospital_beds = Hospitals.query.with_entities(Hospitals.total_capacity, Hospitals.icu_beds).filter_by(id = hospital_id, is_deleted = False).one()
    total_capacity = hospital_beds.total_capacity
    icu_beds = hospital_beds.icu_beds

    if form.validate_on_submit():       
        db.session.query(Hospitals).filter(Hospitals.id == hospital_id).update({Hospitals.total_capacity : form.total_capacity.data, Hospitals.icu_beds : form.icu_beds.data}, synchronize_session = False)
        db.session.commit()
        return redirect(url_for('hospital_beds'))
    return render_template("hospital_beds.html", **locals())

@app.route('/vaccinationstatus', methods = ['POST','GET'])
def vaccination_status():
    form = VaccinationStatus()

    hospital_id = session['hospital_id']
    hospital_name = session['hospital_name']
    vaccination = Hospitals.query.with_entities(Hospitals.first_dose, Hospitals.second_dose, Hospitals.precautionary_dose).filter_by(id = hospital_id, is_deleted = False).one()
    first_dose = vaccination.first_dose
    second_dose = vaccination.second_dose
    precautionary_dose = vaccination.precautionary_dose


    if form.validate_on_submit():       
        db.session.query(Hospitals).filter(Hospitals.id == hospital_id).update({Hospitals.first_dose : Hospitals.first_dose + form.first_dose.data, Hospitals.second_dose : Hospitals.second_dose + form.second_dose.data, Hospitals.precautionary_dose : Hospitals.precautionary_dose + form.precautionary_dose.data}, synchronize_session = False)
        db.session.commit()
        return redirect(url_for('vaccination_status'))

    return render_template("vaccination_status.html", **locals())    
























