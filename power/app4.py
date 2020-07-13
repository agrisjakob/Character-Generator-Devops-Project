from random import randint
import random
from flask import Flask, Response, request, render_template, url_for
import requests
app = Flask(__name__)


@app.route('/power', methods=['POST'])
def power():
    char_info = str(request.data.decode('utf-8'))
    roll = random.choice(range(1,101))
    if char_info[0] == char_info[1]:
        if roll > 40:
            base = randint(700,1000)
        else:
            base = randint(600,900)
    else:
        if roll > 80:
            base = randint(500, 800)
        else:
            base = randint(200,600)
    return Response(str(base), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True,port=5003, host='0.0.0.0')
