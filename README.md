#  Real-Time Weather Forecasting App



---

#  Project Overview

The **Real-Time Weather Forecasting App** is a Python-based application that retrieves live weather information and forecasts using the OpenWeatherMap API.

The application provides real-time weather conditions, detailed atmospheric parameters, and 5-day weather forecasts for any city worldwide. It is designed with a simple user-friendly interface while demonstrating practical implementation of API integration, JSON processing, error handling, and real-world data analysis.

This project was developed as part of the B.E. Data Science curriculum at Chandigarh University.

---

#  Live Demo

###  Web Demo

**Netlify Deployment**

👉 https://23bda70050-gaurav.netlify.app/

### 📂 GitHub Repository

👉 https://github.com/GauravSharma1534/Weather-Forecasting-App

---

#  Project Objectives

The primary goals of this project are:

* Retrieve live weather information using APIs.
* Display current weather conditions.
* Generate multi-day weather forecasts.
* Provide accurate atmospheric data.
* Store weather information for future analysis.
* Handle API failures and invalid inputs gracefully.
* Demonstrate real-world API integration using Python.

---

#  Problem Statement

Weather information plays a critical role in daily decision-making, agriculture, transportation, tourism, and disaster management.

Many weather systems are complex and require multiple services to gather information. This project aims to create a lightweight and efficient weather forecasting application that fetches and displays real-time weather information using publicly available APIs.

The system provides a fast and accessible way to obtain weather information for any city worldwide.

---

#  Key Features

##  Current Weather Information

Retrieve:

* Temperature
* Feels Like Temperature
* Humidity
* Atmospheric Pressure
* Wind Speed
* Visibility
* Cloud Coverage
* Weather Condition
* Sunrise Time
* Sunset Time

---

##  5-Day Weather Forecast

The application provides:

* Daily Forecasts
* Temperature Trends
* Weather Conditions
* Humidity Trends
* Atmospheric Changes

---

##  JSON Data Storage

Users can save weather data locally for:

* Analysis
* Reporting
* Historical Comparison
* Data Collection

---

##  Robust Error Handling

The application handles:

* Invalid City Names
* Network Errors
* API Failures
* Invalid API Keys
* Server Timeouts

---

##  Real-Time API Integration

Live data is fetched directly from:

**OpenWeatherMap API**

Ensuring:

* Up-to-date Weather Information
* Global Coverage
* Reliable Data Sources

---

# 🏗️ System Architecture

```text
User Input (City Name)
            │
            ▼
      Python Application
            │
            ▼
     OpenWeatherMap API
            │
            ▼
      JSON Response
            │
            ▼
 Data Processing & Parsing
            │
            ▼
 Current Weather + Forecast
            │
            ▼
 Terminal Output / JSON File
```

---

#  Working Flow

### Step 1

User enters city name.

### Step 2

Application sends API request.

### Step 3

OpenWeatherMap server returns weather data.

### Step 4

JSON response is parsed.

### Step 5

Weather details are displayed.

### Step 6

Data can be saved locally.

---

#  Technologies Used

| Technology         | Purpose                |
| ------------------ | ---------------------- |
| Python 3.x         | Core Development       |
| Requests           | API Communication      |
| JSON               | Data Parsing & Storage |
| Datetime           | Time Formatting        |
| OpenWeatherMap API | Weather Data Source    |

---

# 📚 Python Concepts Implemented

This project demonstrates:

* REST API Integration
* HTTP Requests
* JSON Parsing
* Exception Handling
* Functions
* Loops
* Conditional Statements
* Data Formatting
* File Handling
* Modular Programming

---

#  Repository Structure

```text
Weather-Forecasting-App/
│
├── weather_app.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── current_weather.png
│   ├── forecast.png
│   ├── error_handling.png
│   └── json_output.png
│
├── Project_Report.pdf
├── Weather_App_PPT.pptx
├── Weather_Output_Demo.html
│
└── assets/
```

---

#  Installation Guide

## Step 1: Clone Repository

```bash
git clone https://github.com/GauravSharma1534/Weather-Forecasting-App.git

cd Weather-Forecasting-App
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install requests
```

---

## Step 3: Create API Key

Create a free account:

https://openweathermap.org

Generate API Key.

Open:

```python
API_KEY = "your_api_key_here"
```

Replace with your API key.

---

## Step 4: Run Application

```bash
python weather_app.py
```

---

#  Application Menu

```text
====================================
 REAL-TIME WEATHER FORECASTING APP
====================================

1. Current Weather
2. 5-Day Forecast
3. Save Weather Data
4. Exit
```

---

# 📊 Sample Output

```text
=====================================
 Current Weather Report
=====================================

City           : Chandigarh
Temperature    : 31°C
Feels Like     : 33°C
Humidity       : 68%
Pressure       : 1008 hPa
Wind Speed     : 12 km/h
Condition      : Clear Sky

Sunrise        : 05:42 AM
Sunset         : 07:16 PM
```

---

#  API Response Example

```json
{
  "city": "Chandigarh",
  "temperature": 31,
  "humidity": 68,
  "wind_speed": 12,
  "condition": "Clear"
}
```

---

# 📈 Real-World Applications

### Agriculture

* Crop Planning
* Irrigation Scheduling

### Transportation

* Route Planning
* Weather Monitoring

### Tourism

* Travel Forecasting
* Destination Planning

### Disaster Management

* Early Weather Alerts
* Risk Assessment

### Smart Cities

* Environmental Monitoring
* Weather Analytics

---

#  Screenshots

The repository includes screenshots demonstrating:

### Current Weather Dashboard

Displays live weather information.

### Forecast Module

Displays future weather predictions.

### Error Handling

Shows API validation and exception handling.

### JSON Output

Demonstrates data export functionality.

---

#  Learning Outcomes

During this project, I learned:

### Technical Skills

* API Integration
* REST Architecture
* Python Requests Library
* JSON Processing
* Data Parsing
* Error Handling
* Time Formatting
* File Operations

### Software Engineering Skills

* Modular Development
* Debugging
* Documentation
* Testing
* Code Organization

### Industry-Relevant Concepts

* Real-Time Data Processing
* Third-Party API Integration
* Cloud-Based Data Services
* Weather Analytics

---

# 📊 Performance Highlights

✅ Real-Time Weather Retrieval

✅ Fast API Response Processing

✅ Global City Coverage

✅ Lightweight Application

✅ JSON Data Export

✅ User-Friendly Interface

✅ Reliable Error Handling

✅ Scalable Architecture

---

#  Future Enhancements

Planned upgrades include:

* Weather Maps Integration
* Geolocation Support
* Streamlit Dashboard
* Flask Web Application
* Weather Notifications
* Email Alerts
* Mobile App Version
* AI-Based Weather Prediction
* Historical Weather Analytics
* Data Visualization Dashboard

---

#  Conclusion

The Real-Time Weather Forecasting App successfully demonstrates the integration of Python with real-world APIs to provide live weather information and forecasting services.

The project highlights practical implementation of REST APIs, JSON data processing, error handling, and real-time information systems. It provides a reliable and scalable foundation for building advanced weather analytics platforms.

This project not only strengthens software development skills but also showcases how modern applications can leverage external APIs to deliver meaningful information and improve user decision-making.

---

