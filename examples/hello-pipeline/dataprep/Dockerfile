# syntax=docker/dockerfile:1
FROM python:3.8.3-slim
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest==6.2.5
COPY ./ .
CMD python -m pytest -vvv