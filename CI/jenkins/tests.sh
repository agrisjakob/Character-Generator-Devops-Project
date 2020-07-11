#!/bin/bash
ssh swarm-master


python3 -m venv venv
. ./venv/bin/activate

pip3 install flask flask-testing pytest pytest-cov requests Werkzeug==0.16.1

cd /home/agrisjakob/char-gen/app

pytest --cov app1 --cov-report term-missing

cd /home/agrisjakob/char-gen/weapons

pytest --cov app2 --cov-report term-missing

cd /home/agrisjakob/char-gen/class

pytest --cov app3 --cov-report term-missing


cd /home/agrisjakob/char-gen/power

pytest --cov app4 --cov-report term-missing
