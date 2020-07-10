FROM python:latest
COPY . .

RUN pip3 install flask requests flask-sqlalchemy PyMySQL cryptography gunicorn

EXPOSE 5000

ENTRYPOINT ["gunicorn","--workers","4","--bind", "0.0.0.0:5000", "app1:app"]
