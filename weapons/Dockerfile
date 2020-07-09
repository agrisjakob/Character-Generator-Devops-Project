FROM python:latest
COPY . .
RUN pip3 install flask requests gunicorn

EXPOSE 5001

ENTRYPOINT ["gunicorn","--workers","4","--bind", "0.0.0.0:5001", "app2:app"]
