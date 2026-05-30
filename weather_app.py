"""
Real-Time Weather Forecasting App
Author: [Your Name]
Date: 2024
Description: A Python-based weather app using OpenWeatherMap API
"""

import requests
import json
import os
from datetime import datetime

# =============================================
# CONFIGURATION
# =============================================
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_weather(city_name, api_key=API_KEY):
    """
    Fetch current weather data for a given city.
    
    Args:
        city_name (str): Name of the city
        api_key (str): OpenWeatherMap API key
    
    Returns:
        dict: Weather data or None if error
    """
    try:
        url = f"{BASE_URL}weather"
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"  # Use 'imperial' for Fahrenheit
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return data
        
    except requests.exceptions.ConnectionError:
        print("ERROR: No internet connection. Please check your network.")
        return None
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("ERROR: Invalid API key. Please check your API key.")
        elif response.status_code == 404:
            print(f"ERROR: City '{city_name}' not found.")
        else:
            print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.Timeout:
        print("ERROR: Request timed out. Please try again.")
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def get_forecast(city_name, api_key=API_KEY, days=5):
    """
    Fetch 5-day weather forecast for a given city.
    
    Args:
        city_name (str): Name of the city
        api_key (str): OpenWeatherMap API key
        days (int): Number of forecast days (max 5)
    
    Returns:
        dict: Forecast data or None if error
    """
    try:
        url = f"{BASE_URL}forecast"
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric",
            "cnt": days * 8  # API gives data every 3 hours
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        return response.json()
        
    except Exception as e:
        print(f"Error fetching forecast: {e}")
        return None


def display_current_weather(data):
    """Display current weather in a formatted way."""
    
    if not data:
        return
    
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    weather_desc = data['weather'][0]['description'].title()
    wind_speed = data['wind']['speed']
    visibility = data.get('visibility', 'N/A')
    
    # Convert visibility to km
    if isinstance(visibility, int):
        visibility = f"{visibility / 1000:.1f} km"
    
    # Sunrise and sunset times
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
    
    print("\n" + "="*55)
    print(f"  🌍 WEATHER REPORT - {city}, {country}")
    print("="*55)
    print(f"  📅 Date & Time : {datetime.now().strftime('%d %B %Y, %H:%M')}")
    print(f"  🌤  Condition   : {weather_desc}")
    print(f"  🌡  Temperature : {temp:.1f}°C (Feels like {feels_like:.1f}°C)")
    print(f"  💧 Humidity    : {humidity}%")
    print(f"  🌬  Wind Speed  : {wind_speed} m/s")
    print(f"  📊 Pressure    : {pressure} hPa")
    print(f"  👁  Visibility  : {visibility}")
    print(f"  🌅 Sunrise     : {sunrise}")
    print(f"  🌇 Sunset      : {sunset}")
    print("="*55)


def display_forecast(data):
    """Display 5-day forecast in a formatted way."""
    
    if not data:
        return
    
    city = data['city']['name']
    country = data['city']['country']
    
    print(f"\n  📆 5-DAY FORECAST - {city}, {country}")
    print("-"*55)
    
    shown_dates = set()
    count = 0
    
    for item in data['list']:
        date_str = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        
        if date_str not in shown_dates and count < 5:
            shown_dates.add(date_str)
            count += 1
            
            date_display = datetime.fromtimestamp(item['dt']).strftime('%a, %d %b')
            temp = item['main']['temp']
            temp_min = item['main']['temp_min']
            temp_max = item['main']['temp_max']
            desc = item['weather'][0]['description'].title()
            humidity = item['main']['humidity']
            
            print(f"  {date_display:<14} {temp:.0f}°C  (Min:{temp_min:.0f}° Max:{temp_max:.0f}°)")
            print(f"  {'':14} {desc} | Humidity: {humidity}%")
            print()
    
    print("-"*55)


def save_weather_to_json(data, filename="weather_data.json"):
    """Save weather data to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\n  ✅ Data saved to '{filename}'")
    except Exception as e:
        print(f"  ❌ Error saving data: {e}")


def get_weather_emoji(weather_main):
    """Return emoji based on weather condition."""
    emojis = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Haze": "🌫️"
    }
    return emojis.get(weather_main, "🌡️")


def main():
    """Main function to run the weather app."""
    
    print("\n" + "="*55)
    print("     🌤  REAL-TIME WEATHER FORECASTING APP")
    print("="*55)
    print("     Using OpenWeatherMap API")
    print("="*55)
    
    while True:
        print("\n  OPTIONS:")
        print("  1. Get Current Weather")
        print("  2. Get 5-Day Forecast")
        print("  3. Get Weather + Forecast")
        print("  4. Save Weather Data to JSON")
        print("  5. Exit")
        
        choice = input("\n  Enter your choice (1-5): ").strip()
        
        if choice == "5":
            print("\n  👋 Thank you for using Weather App! Goodbye.\n")
            break
        
        if choice not in ["1", "2", "3", "4"]:
            print("  ❌ Invalid choice. Please enter 1-5.")
            continue
        
        city = input("  Enter city name: ").strip()
        
        if not city:
            print("  ❌ City name cannot be empty.")
            continue
        
        print(f"\n  ⏳ Fetching weather data for '{city}'...")
        
        if choice == "1":
            data = get_weather(city)
            display_current_weather(data)
        
        elif choice == "2":
            data = get_forecast(city)
            display_forecast(data)
        
        elif choice == "3":
            current = get_weather(city)
            forecast = get_forecast(city)
            display_current_weather(current)
            display_forecast(forecast)
        
        elif choice == "4":
            current = get_weather(city)
            if current:
                save_weather_to_json(current)
        
        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()
