from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField, SubmitField,PasswordField,RadioField, DateField,SelectField, BooleanField
from wtforms.validators import EqualTo,DataRequired, Length,  ValidationError 


class AdminLogin(FlaskForm):

    username = StringField(label="username",validators=[DataRequired()])
    password = PasswordField(label="password",validators=[DataRequired()])
    submit = SubmitField(label='submit')

class AddUser(FlaskForm):

    username = StringField(label="username",validators=[DataRequired()])
    password = PasswordField(label="password",validators=[DataRequired()])
    submit = SubmitField(label='submit')


class AddHospital(FlaskForm):

    hospital_name = StringField(label="hospital_name",validators=[DataRequired()])
    contact_number = IntegerField(label="contact_number",validators=[DataRequired()])
    user = SelectField(label = 'user',coerce=str,validators=[DataRequired()]) 
    submit = SubmitField(label='submit')
    

class HospitalBeds(FlaskForm):

    total_capacity = IntegerField(label="total_capacity",validators=[DataRequired()])
    icu_beds = IntegerField(label="icu_beds",validators=[DataRequired()])  
    submit = SubmitField(label='submit')  

class VaccinationStatus(FlaskForm):
 
    first_dose = IntegerField(label="first_dose")
    second_dose = IntegerField(label="second_dose")
    precautionary_dose = IntegerField(label="precautionary_dose")
    submit = SubmitField(label='submit') 

class AddPatient(FlaskForm):
 
    first_name = StringField(label="first_name",validators=[DataRequired()])
    last_name = StringField(label="last_name",validators=[DataRequired()])
    dob = DateField(label ="dob", format='%Y-%m-%d', validators=[DataRequired()])
    gender = RadioField(label ="gender", choices = [('M','Male'),('F','Female')]) 
    unique_id = StringField(label="unique_id", validators=[DataRequired()])
    test_result = SelectField(label = 'test_result', choices = [('negative', 'Negative'),('positive', 'Positive')]) 
    submit = SubmitField(label='submit')  


class UpdatePatientStatus(FlaskForm):
    status = SelectField(label = 'status', choices = [('negative', 'Negative'),('positive', 'Positive')]) 
    submit = SubmitField(label='submit')    




