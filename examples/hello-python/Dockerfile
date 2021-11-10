# syntax=docker/dockerfile:1
FROM python:3.9.3-slim AS build
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY src/ .

FROM build AS unit_test
RUN pip install pytest
CMD python -m pytest

FROM build AS final
CMD ["python", "server.py"]