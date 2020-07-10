FROM python:latest
COPY . .

RUN pip3 install flask requests gunicorn

EXPOSE 5002

ENTRYPOINT ["gunicorn","--workers","4","--bind","0.0.0.0:5002", "app3:app"]
