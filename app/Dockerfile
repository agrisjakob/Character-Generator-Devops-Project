FROM python:latest
COPY . .

RUN pip3 install flask requests

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python3", "app1.py"]
