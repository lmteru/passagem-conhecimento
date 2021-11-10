# syntax=docker/dockerfile:1
FROM python:3.8.3-slim AS my-data-prep
WORKDIR /src
COPY dataprep/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY dataprep/ .
RUN python data_prep.py

FROM python:3.8.3-slim AS my-model-trainer
WORKDIR /src
COPY --from=my-data-prep /src/assets /src/assets
COPY trainer/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY trainer/ .
RUN python trainer.py

FROM python:3.8.3-slim AS my-model-api
WORKDIR /src
COPY --from=my-model-trainer /src/assets/pickled.pkl /src/assets/pickled.pkl
COPY flaskr/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY flaskr/ .
EXPOSE 5000
ENV FLASK_APP=flaskr
CMD python -m flask run --host=0.0.0.0