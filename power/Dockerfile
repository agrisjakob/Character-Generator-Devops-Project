FROM python:latest
COPY . .

RUN pip3 install flask requests gunicorn

EXPOSE 5003

ENTRYPOINT ["gunicorn","--workers","4","--bind","0.0.0.0:5003", "app4:app"]
