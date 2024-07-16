import requests
from typing import Dict, Any

class WeatherAPI:

    def get_weather(self, lat: float, long: float) -> Dict[str, Any]:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"
        response = requests.get(url)
        return response.json()
