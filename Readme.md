# Kafka JSON API

## Run

    docker compose up --build

## Usage

    curl -X POST http://localhost:8000/data \
      -H 'Content-Type: application/json' \
      -d '{"id":"1","message":"hello"}'

Response:

    {"status":"ok"}

## Inspect Kafka

    kcat -b localhost:9094 -t test -C