"""
Weather API Module - Handles all OpenWeatherMap API interactions.

This module contains functions for fetching and processing weather data
from the OpenWeatherMap API, including temperature conversion and time formatting.
"""

import time
import requests

from config import API_KEY

API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


SAMPLE_WEATHER_DATA = {
    "success": True,
    "weather_desc": "Clear",
    "weather_icon": "01d",
    "temp_C": 25,
    "feels_like_C": 27,
    "temp_F": 77,
    "feels_like_F": 80,
    "wind_speed": 5.2,
    "pressure": 1013,
    "humidity": 65,
    "sunrise": "06:30:00",
    "sunset": "18:45:00",
    "name": "Demo City",
    "country": "XX",
}


def is_api_configured() -> bool:
    """Check if a valid API key is configured."""
    return bool(API_KEY and API_KEY.strip() and API_KEY != "YOUR_API_KEY_HERE")


def kelvin_to_celsius(kelvin_temp: float) -> int:
    """Convert temperature from Kelvin to Celsius."""
    return int(kelvin_temp - 273.15)


def celsius_to_fahrenheit(celsius_temp: int) -> int:
    """Convert temperature from Celsius to Fahrenheit."""
    return int((celsius_temp * 1.8) + 32)


def format_timestamp(timestamp: int, timezone_offset: int = -21600) -> str:
    """Format a Unix timestamp to a readable time string."""
    return time.strftime("%I:%M:%S", time.gmtime(timestamp + timezone_offset))


def fetch_weather_data(location: str) -> dict:
    """Fetch weather data from OpenWeatherMap API."""
    url = f"{API_BASE_URL}?q={location}&appid={API_KEY}"
    response = requests.get(url, timeout=10)
    return response.json()


def parse_weather_response(json_data: dict) -> dict:
    """Parse the API response and extract weather information."""
    status_code = json_data.get("cod")

    if status_code in ("404", "400"):
        return {
            "success": False,
            "error_code": status_code,
            "error_message": json_data.get("message", "Unknown error"),
        }

    temp_c = kelvin_to_celsius(json_data["main"]["temp"])
    feels_like_c = kelvin_to_celsius(json_data["main"]["feels_like"])

    return {
        "success": True,
        "weather_desc": json_data["weather"][0]["main"],
        "weather_icon": json_data["weather"][0]["icon"],
        "temp_C": temp_c,
        "feels_like_C": feels_like_c,
        "temp_F": celsius_to_fahrenheit(temp_c),
        "feels_like_F": celsius_to_fahrenheit(feels_like_c),
        "wind_speed": json_data["wind"]["speed"],
        "pressure": json_data["main"]["pressure"],
        "humidity": json_data["main"]["humidity"],
        "sunrise": format_timestamp(json_data["sys"]["sunrise"]),
        "sunset": format_timestamp(json_data["sys"]["sunset"]),
        "name": json_data["name"],
        "country": json_data["sys"]["country"],
    }


def get_weather(location: str) -> dict:
    """Get weather information for a location."""
    if not is_api_configured():
        sample_data = SAMPLE_WEATHER_DATA.copy()
        sample_data["name"] = location.title() if location else "Demo City"
        return sample_data

    try:
        json_data = fetch_weather_data(location)
        return parse_weather_response(json_data)
    except requests.ConnectionError:
        return {
            "success": False,
            "error_code": "CONNECTION_ERROR",
            "error_message": "Failed to establish a new connection",
        }
    except requests.Timeout:
        return {
            "success": False,
            "error_code": "TIMEOUT",
            "error_message": "Request timed out",
        }
    except requests.RequestException as e:
        return {
            "success": False,
            "error_code": "REQUEST_ERROR",
            "error_message": str(e),
        }
    except (KeyError, ValueError) as e:
        return {
            "success": False,
            "error_code": "PARSE_ERROR",
            "error_message": f"Failed to parse response: {str(e)}",
        }
