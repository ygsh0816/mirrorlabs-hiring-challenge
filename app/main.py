# app/main.py
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.weather_api import WeatherAPI
from .kafka_producer import send_message
from .kafka_consumer import kafka_consumer_service

app = FastAPI()


class Message(BaseModel):
    user_id: str
    lat: str
    long: str
    timestamp: str


@app.post("/produce/")
async def produce_message(message: Message) -> Dict[str, Any]:
    send_message(message.dict())
    return {"status": "Message sent successfully"}


@app.get('/user/weather')
async def get_user_weather(user_id: str) -> Dict[str, Any]:
    user_location = kafka_consumer_service.user_locations.get(user_id)
    if not user_location:
        raise HTTPException(status_code=400, detail="User not found")
    weather_api = WeatherAPI()
    weather = weather_api.get_weather(user_location['lat'], user_location['long'])
    return {
        "user_id": user_id,
        "location": user_location,
        "weather": weather
    }


@app.on_event("startup")
async def startup_event():
    kafka_consumer_service.start()


@app.on_event("shutdown")
async def shutdown_event():
    kafka_consumer_service.stop()
