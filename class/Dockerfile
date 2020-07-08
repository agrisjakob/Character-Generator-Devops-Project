FROM python:latest
COPY . .

RUN pip3 install flask requests

EXPOSE 5002

ENTRYPOINT ["/usr/local/bin/python3", "app3.py"]
