FROM python:3-alpine

RUN pip3 install -q Flask==3.0.0
COPY . ./app
CMD ["python3", "/app/service/server.py"]
