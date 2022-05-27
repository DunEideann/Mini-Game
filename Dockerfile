FROM python:3.10.4-slim-bullseye

#RUN apk add build-base=0.5-r2 python3-dev=3.8.10-r0 postgresql-dev=12.8-r0 --no-cache

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src
COPY src .

ARG COMMIT=local
ENV COMMIT=${COMMIT}

CMD ["python3","main.py"]