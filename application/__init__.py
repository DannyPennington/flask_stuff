from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://danny@flaskbase2:Linuxdatabase1@flaskbase2.mysql.database.azure.com/testing"
#os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = str(os.getenv("MY_SECRET_KEY"))

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
