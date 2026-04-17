# Weather App

A modern desktop weather application built with Python and Flet featuring an Apple-inspired design. Displays current weather information for any city worldwide.

## Features

- **Apple-Inspired UI**: Clean, modern interface with card-based layout
- **Temperature Display**: Large, prominent temperature with feels-like temperature
- **Weather Conditions**: Weather description with visual icons from OpenWeatherMap
- **Sun Information**: Sunrise and sunset times
- **Weather Details**: Humidity, wind speed, and atmospheric pressure
- **Theme Support**: Dark and light mode toggle with Apple-style switcher
- **Search**: City search with Enter key or click
- **Demo Mode**: Runs without API key showing sample data

## Project Structure

```
WeatherAppPython/
├── main.py              # Application entry point
├── weather_api.py       # API interaction and data parsing
├── ui_components.py     # UI widgets and layouts (Apple-style)
├── config.py           # API key and settings
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nayaksomkar/WeatherAppPython.git
cd WeatherAppPython
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. (Optional) Configure API Key

To get real weather data, add your OpenWeatherMap API key in `config.py`:

```python
API_KEY = "your_openweathermap_api_key"
```

Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

**Note**: Without an API key, the app runs in demo mode showing sample data.

## Running the Application

With your virtual environment activated:

```bash
python main.py
```

## Weather Data Displayed

| Field | Description | Unit |
|-------|-------------|------|
| Temperature | Current temperature | °C |
| Feels Like | Temperature perception | °C |
| Weather | Condition description | Text |
| Humidity | Atmospheric humidity | % |
| Wind Speed | Wind velocity | m/s |
| Pressure | Atmospheric pressure | hPa |
| Sunrise | Sunrise time | HH:MM |
| Sunset | Sunset time | HH:MM |

## Code Organization

- **config.py**: Stores API key and configuration settings (excluded from git)
- **weather_api.py**: Handles API calls, response parsing, and sample data
- **ui_components.py**: Contains all Flet UI widgets with Apple-style design
- **main.py**: Application initialization, event handling, and main layout

## Troubleshooting

**Application fails to start:**
- Verify Python version (3.8+)
- Ensure virtual environment is activated
- Check that all dependencies are installed

**Weather data not loading:**
- Verify internet connection
- Check API key validity in `config.py`
- App will work in demo mode without API key

**UI issues:**
- Update Flet to the latest version: `pip install flet --upgrade`

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| requests | >=2.28.0 | HTTP API calls |
| flet | >=0.21.0 | Desktop UI framework |
