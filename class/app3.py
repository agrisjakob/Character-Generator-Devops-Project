import random
from flask import Flask, Response, request, jsonify
import requests
from random import randint

app = Flask(__name__)

@app.route('/class', methods=['GET'])
def character():
    classesA = ["1 Barbarian", "2 Rogue","3 Druid","4 Hunter","5 Sorcerer", "6 Shaman", "7 Dragoon", "8 Samurai", "9 Tank"]
    final_class = random.choice(classesA)

    return Response(final_class, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True,port=5002, host='0.0.0.0')
