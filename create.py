from application import db
import sqlalchemy
from application.models import Posts

db.drop_all()
db.create_all()
