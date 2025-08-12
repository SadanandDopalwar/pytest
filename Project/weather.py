import requests

def get_weather(city):
    """Get current temperature in Celsius for a city using Open-Meteo."""
    coords = {
        "Mumbai": (19.0760, 72.8777),
        "London": (51.5072, -0.1276),
    }

    if city not in coords:
        raise ValueError("City not supported.")

    lat, lon = coords[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data["current_weather"]["temperature"]

def categorize_temperature(temp):
    """Categorize temperature."""
    if temp < 10:
        return "Cold"
    elif 10 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"
