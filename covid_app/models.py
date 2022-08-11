from email.policy import default
from enum import unique
from covid_app import db
from datetime import datetime
from sqlalchemy import Date


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(20),nullable = False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    hospitals = db.relationship('Hospitals', backref = 'users')


class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    hospital_name = db.Column(db.String(50),nullable = False)
    contact_number = db.Column(db.Integer, nullable = False)  
    user_id = db.Column(db.Integer,db.ForeignKey('users.id')) 
    total_capacity = db.Column(db.Integer, default = 0)
    icu_beds = db.Column(db.Integer,default = 0)
    first_dose = db.Column(db.Integer, default = 0)
    second_dose = db.Column(db.Integer,default = 0)
    precautionary_dose = db.Column(db.Integer, default = 0)
    is_deleted = db.Column(db.Boolean, default=False)
    covidtest = db.relationship('CovidTest', backref = 'hospital_test')
    

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    unique_id = db.Column(db.String(20),nullable = False, unique = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    dob = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10), nullable = False)
    status = db.Column(db.String(10))
    covidtest = db.relationship('CovidTest', backref = 'patient_test')
    

class CovidTest(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    date_added = db.Column(db.DateTime)
    hospital_id = db.Column(db.Integer,db.ForeignKey('hospitals.id'))
    patient_id = db.Column(db.Integer,db.ForeignKey('patients.id'))
    test_result = db.Column(db.String(10)) 
    is_recovered = db.Column(db.Boolean, default=False)
    is_deceased = db.Column(db.Boolean, default=False)
    is_current = db.Column(db.Boolean, default=True)
    date_updated = db.Column(db.DateTime)

class ActivePatients(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    date_added = db.Column(db.DateTime)
    active_count = db.Column(db.Integer)   


        