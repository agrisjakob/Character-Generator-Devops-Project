from flask import Flask, Response, request, render_template, url_for
import requests


app = Flask(__name__)

wep = 'http://app2:5001'
char = 'http://app3:5002'
base = 'http://app4:5003'

@app.route('/home', methods=['GET', 'POST'])
def home():
    weapon = requests.get(wep + '/weapons')
    character = requests.get(char + '/class')
    weapon.json().update(character.json())
    getPower = requests.post(base + '/power',json= weapon.json())
    power= getPower.text
    return render_template('home.html', power=power)







if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')

    
    
