from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://danny:Linuxdatabase1@testbase2.mysql.database.azure.com/testing"
#os.getenv('DATABASE_URI')

db = SQLAlchemy(app)

from application import routes
