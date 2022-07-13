from covid_app import db
from datetime import datetime
from sqlalchemy import Date


class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    HospitalName = db.Column(db.String(50),nullable = False)
    ContactNumber = db.Column(db.Integer,unique = True, nullable = False)
    Username = db.Column(db.String(20),unique = True, nullable = False)
    Password = db.Column(db.String(20),unique = True, nullable = False)
    TotalCapacity = db.Column(db.Integer)
    ICU_Beds = db.Column(db.Integer)
    First_Dose = db.Column(db.Integer)
    Second_Dose = db.Column(db.Integer)
    Precautionary_Dose = db.Column(db.Integer)
    patients = db.relationship('Patients', backref = 'hospitals')


class Patients(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    Hosp_id = db.Column(db.Integer,db.ForeignKey('hospitals.id'))
    Date = db.Column(db.DateTime)
    Fname = db.Column(db.String(20), nullable = False)
    Lname = db.Column(db.String(20), nullable = False)
    DOB = db.Column(db.DateTime)
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(10), nullable = False)
    TestResult =  db.Column(db.String(10))
    Status = db.Column(db.String(10))
 
    


        