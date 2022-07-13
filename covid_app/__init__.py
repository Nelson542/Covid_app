from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "covid_tracker"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev" 

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from covid_app import views, models

db.create_all()