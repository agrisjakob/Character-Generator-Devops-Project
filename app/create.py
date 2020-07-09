from app1 import db

from app.models import Power

db.drop_all()
db.create_all()