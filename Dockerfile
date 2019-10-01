FROM python:3.7-slim

COPY src src
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
