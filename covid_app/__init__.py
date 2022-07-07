from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "covid_tracker"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nelson28@localhost:5432/covid_dashboard" 

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from covid_app import views, models