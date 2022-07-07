from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField, SubmitField,PasswordField,RadioField, DateField,SelectField, BooleanField
from wtforms.validators import EqualTo,DataRequired, Length


class AdminLogin(FlaskForm):

    username = StringField(label="Name",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class NewHospital(FlaskForm):

    HospitalName = StringField(label="HospitalName",validators=[DataRequired()])
    ContactNumber = IntegerField(label="ContactNumber",validators=[DataRequired()])
    Username = StringField(label="Username",validators=[DataRequired()])
    Password = PasswordField(label="Password",validators=[DataRequired()])  
    submit = SubmitField(label='Submit')

class HospitalUpdate(FlaskForm):

    TotalCapacity = IntegerField(label="TotalCapacity",validators=[DataRequired()])
    ICU_Beds = IntegerField(label="ICU_Beds",validators=[DataRequired()])  
    FirstDose = IntegerField(label="FirstDose")
    SecondDose = IntegerField(label="SecondDose")
    PrecautionaryDose = IntegerField(label="PrecautionaryDose")
    submit = SubmitField(label='Submit')  

class VaccinationStatus(FlaskForm):
 
    FirstDose = IntegerField(label="FirstDose")
    SecondDose = IntegerField(label="SecondDose")
    PrecautionaryDose = IntegerField(label="PrecautionaryDose")
    submit = SubmitField(label='Submit') 

class AddPatient(FlaskForm):
 
    Fname = StringField(label="FirstName",validators=[DataRequired()])
    Lname = StringField(label="LastName",validators=[DataRequired()])
    DOB = DateField(label ="DOB", format='%Y-%m-%d', validators=[DataRequired()])
    Gender = RadioField(label ="Gender", choices = [('M','Male'),('F','Female')]) 
    TestResult = SelectField(label = 'TestResult', choices = [('-ve', 'Negative'),('+ve', 'Positive')]) 
    submit = SubmitField(label='Submit')     

class UpdatePatientLogin(FlaskForm):
 
    Fname = StringField(label="FirstName",validators=[DataRequired()])
    Lname = StringField(label="LastName",validators=[DataRequired()])
    DOB = DateField(label ="DOB", format='%Y-%m-%d', validators=[DataRequired()]) 
    submit = SubmitField(label='Submit')                

class UpdatePatientStatus(FlaskForm):
    Status = RadioField(label = 'Status', choices = [('+ve', 'Positive'),('Recovered', 'Recovered'),('Deceased', 'Deceased')])  
    submit = SubmitField(label='Submit') 

