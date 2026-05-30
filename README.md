# Real-Time Weather Forecasting App

**Gaurav Sharma | 23BDA70050 | B.E. | Chandigarh University | 2025**

A Python app that fetches live weather data using the OpenWeatherMap API.

## Features
- Get current weather for any city (temp, humidity, wind, pressure, sunrise/sunset)
- Get 5-day weather forecast
- Save weather data to JSON file
- Simple menu-driven interface
- Handles errors — wrong city, no internet, invalid API key

## How to Run

**Step 1 — Install dependency**
```bash
pip install requests
```

**Step 2 — Get free API key**
- Go to openweathermap.org → Sign up → Copy your API key
- Open weather_app.py and replace: `API_KEY = "your_api_key_here"`

**Step 3 — Run the app**
```bash
python weather_app.py
```

## Tech Stack
| Library | Use |
|---------|-----|
| Python 3.x | Main language |
| requests | HTTP API calls |
| json | Parse and save data |
| datetime | Format timestamps |
| OpenWeatherMap API | Weather data |

## Files
| File | Description |
|------|-------------|
| `weather_app.py` | Main Python code |
| `requirements.txt` | Lists: requests==2.31.0 |
| `README.md` | This file |
| `screenshots/` | Output screenshots |
| `Project_Report.pdf` | 30-page project report |
| `Weather_App_PPT.pptx` | 15-slide presentation |

## GitHub
https://github.com/GauravSharma1534/Weather-Forecasting-App
