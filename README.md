# Weather API Project

A Python command-line tool that fetches coordinates for a location and displays a detailed weather forecast. This project was developed as an exercise for the **Python for Everybody (PY4E)** course from the University of Michigan.

## Features

* **Geocoding:** Converts location names (e.g., "Valencia", "New York") into Latitude and Longitude using the OpenStreetMap (Nominatim) API.
* **Weather Forecast:** Retrieves an 8-day daily forecast using the OpenWeatherMap One Call API 3.0.
* **Terminal Dashboard:** Formats the API response into a clean, readable table showing Date, Temperature (Day/Night), Conditions, Rain, and Wind.

## Prerequisites

* Python 3.8+
* An API Key from [OpenWeatherMap](https://openweathermap.org/api) (Specifically the "One Call API 3.0").

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/gonzaleztucci/weatherAPI.git](https://github.com/gonzaleztucci/weatherAPI.git)
    cd weatherAPI
    ```

2.  **Install required libraries:**
    This project uses `requests` for API calls and `python-dotenv` to manage security variables.
    ```bash
    pip install requests python-dotenv
    ```

## Configuration (Required)

To protect sensitive API keys and comply with usage policies, this project uses a `.env` file. This file is ignored by Git and must be created locally.

1.  **Create the file:**
    Create a file named `.env` in the root folder of the project.

2.  **Add your variables:**
    Copy the format below into your `.env` file and replace the values with your actual data:

    ```ini
    # .env
    
    # Required for OpenWeatherMap API access
    OPEN_WEATHER_API_KEY=your_api_key_here

    # Required for OpenStreetMap (Nominatim) User-Agent header
    # (Nominatim requires an email to contact you in case of excessive usage)
    OSM_EMAIL=your_email@example.com
    ```

    > **Warning:** The script will check for these variables and exit with an error if they are missing.

## Usage

Run the main script:

```bash
python main.py