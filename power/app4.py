import random
from random import randint
from flask import Flask, Response, request, render_template, url_for
import requests
app = Flask(__name__)


@app.route('/power', methods=['POST'])
def power():
    char_info = request.data.decode('utf-8')
    roll = randint(1,100)
    if char_info[0] == char_info[1]:
        if roll > 50:
            base = randint(700,1000)
        else:
            base = randint(600,900)
    else:
        if roll > 90:
            base = randint(500, 800)
        else:
            base = randint(200,600)
    return Response(base, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True,port=5003, host='0.0.0.0')
