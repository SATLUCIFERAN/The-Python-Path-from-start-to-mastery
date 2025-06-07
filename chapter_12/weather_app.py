
import os
import requests
from datetime import datetime

def get_current_weather(city_name):
    """
    Fetches current weather data for the specified city_name
    using the OpenWeatherMap API, then prints a formatted summary.
    """
    # 1. Read API key from environment
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        return

    # 2. Construct the URL and parameters
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Celsius; change to "imperial" for Fahrenheit
    }

    try:
        # 3. Send the GET request
        response = requests.get(base_url, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        # If the server returns 4xx or 5xx, handle it here
        print(f"HTTP error: {http_err} (status code {response.status_code})")
        return
    except requests.exceptions.RequestException as err:
        # This catches network-level issues (DNS failure, no internet, etc)
        print(f"Request exception: {err}")
        return

    # 4. Verify we received JSON
    content_type = response.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        print("Error: Server did not return JSON. Content-Type:", content_type)
        return

    try:
        data = response.json()
    except ValueError:
        print("Error: Received invalid JSON.")
        return

    # 5. Check OpenWeatherMap's internal 'cod' field (200 means success)
    if data.get("cod") != 200:
        # It might be 404 if the city wasn’t found, or another error
        message = data.get("message", "No message provided")
        print(f"OpenWeatherMap error: {data.get('cod')} – {message}")
        return

    # 6. Extract fields of interest
    name        = data.get("name", "Unknown location")
    country     = data["sys"].get("country", "N/A")
    description = data["weather"][0]["description"].title()
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    wind_speed  = data["wind"]["speed"]
    timestamp   = data.get("dt", None)

    # 7. Convert Unix UTC timestamp to local time (using system’s locale)
    local_time_str = "N/A"
    if timestamp:
        local_dt       = datetime.fromtimestamp(timestamp)
        local_time_str = local_dt.strftime("%Y-%m-%d %H:%M:%S")

    # 8. Print a nicely formatted summary
    print(f"------ Current Weather for {name}, {country} ------")
    print(f"Time (local):    {local_time_str}")
    print(f"Condition:       {description}")
    print(f"Temperature:     {temp:.1f}°C  (Feels like {feels_like:.1f}°C)")
    print(f"Humidity:        {humidity}%")
    print(f"Wind speed:      {wind_speed} m/s")
    print("-----------------------------------------------")

if __name__ == "__main__":
    # 9. Prompt the user (or hardcode a city)
    city_to_lookup = input("Enter a city name (e.g., 'Bangkok'): ").strip()
    if city_to_lookup:
        get_current_weather(city_to_lookup)
    else:
        print("No city entered. Exiting.")
