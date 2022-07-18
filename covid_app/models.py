from covid_app import db
from datetime import datetime
from sqlalchemy import Date

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(20),unique = True, nullable = False)
    password = db.Column(db.String(20),unique = True, nullable = False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    hospitals = db.relationship('Hospitals', backref = 'users')


class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    hospital_name = db.Column(db.String(50),nullable = False)
    contact_number = db.Column(db.Integer,unique = True, nullable = False)  
    user_id = db.Column(db.Integer,db.ForeignKey('users.id')) 
    total_capacity = db.Column(db.Integer)
    icu_beds = db.Column(db.Integer)
    first_dose = db.Column(db.Integer)
    second_dose = db.Column(db.Integer)
    precautionary_dose = db.Column(db.Integer)
    patients = db.relationship('Patients', backref = 'hospitals')
    

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    hosp_id = db.Column(db.Integer,db.ForeignKey('hospitals.id'))
    date_added = db.Column(db.DateTime)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    dob = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10), nullable = False)
    test_result =  db.Column(db.String(10))
    status = db.Column(db.String(10))
 
    


        