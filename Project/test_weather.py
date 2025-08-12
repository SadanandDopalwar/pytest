import pytest
import weather
from unittest.mock import patch

# @patch("weather.requests.get")
# def test_get_weather_mocked(mock_get):
#     # Mock the requests.get call to return a fixed response
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = {
#         "current_weather": {"temperature": 30.5}
#     }

#     temp = weather.get_weather("Mumbai")
#     print(temp)
#     assert temp == 30.5
#     assert isinstance(temp, float)

import weather

def test_live_weather():
    city = "Mumbai"
    temp = weather.get_weather(city)
    category = weather.categorize_temperature(temp)

    print(f"Temperature in {city}: {temp}°C -> {category}")

    # Basic sanity check
    assert isinstance(temp, (int, float))
    assert category in ["Cold", "Moderate", "Hot"]

