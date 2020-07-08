FROM python:latest
COPY . .

RUN pip3 install flask requests

EXPOSE 5003

ENTRYPOINT ["/usr/local/bin/python3", "app4.py"]
