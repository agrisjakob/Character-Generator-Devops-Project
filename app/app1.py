from flask import Flask, Response, request, render_template, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= str(getenv('DATABASE_URI'))

db = SQLAlchemy(app)


wep = 'http://app2:5001'
char = 'http://app3:5002'
base = 'http://app4:5003'

class Power(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    power = db.Column(db.Integer, nullable= False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@app.route('/home', methods=['GET', 'POST'])
def home():
    weapon = requests.get(wep + '/weapons')
    character = requests.get(char + '/class')
    char_id = character.text
    wep_id = weapon.text
    getPower = requests.post(base + '/power', wep_id[0] + char_id[0])
    power= getPower.text
    addpower = Power(power=power)
    db.session.add(addpower)
    db.session.commit()
    return render_template('home.html', power=power, character=char_id, weapon=wep_id)







if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')

    
    
