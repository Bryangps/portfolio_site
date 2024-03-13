from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aabed9da26634fb72ea6d0e7aa62c095'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// zboxcrossclub.db'

database = SQLAlchemy(app)

from zboxcrossvendasbebidas import route
