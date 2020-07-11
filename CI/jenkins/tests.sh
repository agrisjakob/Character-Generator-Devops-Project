#!/bin/bash
sudo apt install python3-venv
python3 -m venv venv
. ./venv/bin/activate

pip3 install flask flask-testing pytest pytest-cov requests Werkzeug==0.16.1 flask-sqlalchemy pymysql

echo ${TESTING_URI}

cd app

pytest --cov app1 --cov-report term-missing

cd ..

cd weapons

pytest --cov app2 --cov-report term-missing

cd ..

cd class

pytest --cov app3 --cov-report term-missing

cd ..

cd power

pytest --cov app4 --cov-report term-missing
