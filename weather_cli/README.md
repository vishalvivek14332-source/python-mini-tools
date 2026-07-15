# Weather CLI

A simple command-line weather application that fetches real-time weather data using the OpenWeatherMap API.

## Features

- Search weather by city name
- Displays temperature and weather conditions
- Uses metric units (°C)
- Secure API key handling via environment variables

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Obtain a free API key from OpenWeatherMap and set it as an environment variable:

### Windows (PowerShell)

```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

### Linux/macOS

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

## Usage

```bash
python main.py
```

Enter the desired city name when prompted.

## Requirements

- Python 3.8+
- requests

## License

This project is released under the MIT License.
