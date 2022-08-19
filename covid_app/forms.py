from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField, SubmitField,PasswordField,RadioField, DateField,SelectField, BooleanField
from wtforms.validators import EqualTo,DataRequired, Length,  ValidationError 

class AdminLogin(FlaskForm):
    username = StringField(label="username",validators=[DataRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField(label="password",validators=[DataRequired()],render_kw={"placeholder": "Password"})
    submit = SubmitField(label='Submit')

class AddUser(FlaskForm):
    username = StringField(label="username",validators=[DataRequired()],render_kw={"placeholder": "Username"})
    password = PasswordField(label="password",validators=[DataRequired()],render_kw={"placeholder": "Password"})
    submit = SubmitField(label='Submit')

class AddHospital(FlaskForm):
    hospital_name = StringField(label="hospital_name",validators=[DataRequired()],render_kw={"placeholder": "Hospital name"})
    contact_number = IntegerField(label="contact_number",validators=[DataRequired()],render_kw={"placeholder": "Contact number"})
    user = SelectField(label = 'user',coerce=str,validators=[DataRequired()])
    submit = SubmitField(label='Submit')
    
class HospitalBeds(FlaskForm):
    total_capacity = IntegerField(label="total_capacity",validators=[DataRequired()],render_kw={"placeholder": "Total Capacity"})
    icu_beds = IntegerField(label="icu_beds",validators=[DataRequired()],render_kw={"placeholder": "ICU Beds"})  
    submit = SubmitField(label='Submit')  

class VaccinationStatus(FlaskForm): 
    first_dose = IntegerField(label="first_dose",render_kw={"placeholder": "First Dose"})
    second_dose = IntegerField(label="second_dose",render_kw={"placeholder": "Second Dose"})
    precautionary_dose = IntegerField(label="precautionary_dose",render_kw={"placeholder": "Precautionary Dose"})
    submit = SubmitField(label='Submit') 

class PatientSearch(FlaskForm):
    unique_id = StringField(label="unique_id", validators=[DataRequired()],render_kw={"placeholder": "Unique ID"}) 
    submit = SubmitField(label='Submit')    

class AddPatient(FlaskForm): 
    first_name = StringField(label="first_name",validators=[DataRequired()],render_kw={"placeholder": "First name"})
    last_name = StringField(label="last_name",validators=[DataRequired()],render_kw={"placeholder": "Last name"})
    dob = DateField(label ="dob", format='%Y-%m-%d', validators=[DataRequired()],render_kw={"placeholder": "Date of Birth"})
    gender = RadioField(label ="gender", choices = [('M','Male'),('F','Female')],render_kw={"placeholder": "Gender"}) 
    unique_id = StringField(label="unique_id", validators=[DataRequired()],render_kw={"placeholder": "Unique ID"})
    test_result = SelectField(label = 'test_result', choices = [('negative', 'Negative'),('positive', 'Positive')],render_kw={"placeholder": "Test Result"}) 
    submit = SubmitField(label='Submit')  

class UpdatePatientStatus(FlaskForm):
    status = SelectField(label = 'status', choices = [('negative', 'Negative'),('positive', 'Positive')]) 
    submit = SubmitField(label='Submit')    




