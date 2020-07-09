from flask import Flask, Response, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import Power
import requests
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= str(getenv('DATABASE_URI'))

db = SQLALCHEMY(app)

wep = 'http://app2:5001'
char = 'http://app3:5002'
base = 'http://app4:5003'


@app.route('/home', methods=['GET', 'POST'])
def home():
    weapon = requests.get(wep + '/weapons')
    character = requests.get(char + '/class')
    char_id = character.text
    wep_id = weapon.text
    getPower = requests.post(base + '/power', wep_id[0] + char_id[0])
    power= getPower.text
    addpower = Power(power=power)
    db.session.add(user)
    db.session.commit()
    return render_template('home.html', power=power)







if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')

    
    
