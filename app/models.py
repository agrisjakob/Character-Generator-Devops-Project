from app1 import db

from datetime import datetime

class Power(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    power = db.Column(db.Integer, nullable= False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
