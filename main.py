import json

from fastapi import FastAPI, HTTPException, Request
from confluent_kafka import Producer

app = FastAPI()

producer = Producer({"bootstrap.servers": "localhost:9094"})
TOPIC = "test"


@app.post("/data")
async def send_data(request: Request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    producer.produce(TOPIC, json.dumps(data).encode())
    producer.flush()

    return {"status": "ok"}
