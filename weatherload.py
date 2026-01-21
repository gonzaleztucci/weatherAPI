import requests
import sys
import os
import datetime
from dotenv import load_dotenv

# Unused imports to be removed afterwards
# import urllib.request, urllib.parse, urllib.error
# import http
# import sqlite3
# import json
# import time
# import ssl

# Load the variables from the .env file into the environment
load_dotenv()

contact_email = os.getenv("OSM_EMAIL")




def get_coordinates(place_name):
    url = 'https://nominatim.openstreetmap.org/search?'

    contact_email = os.getenv("OSM_EMAIL")

    if not contact_email:
        print("Error: OSM_EMAIL not found in .env file.")
        sys.exit(1)

    params = {
        'q': place_name,
        'format': 'json',
        'limit': 1
    }

    # IMPORTANT: For OpenStreetMap, script must include a custom User-Agent
    headers = {
        'User-Agent': f'MyWeatherApp/1.0 ({contact_email})'
    }
    try:
        response = requests.get(url,params=params,headers=headers)

        response.raise_for_status() # Check for HTTP errors
        data = response.json()

        if data:
            location = data[0]
            name = location['name']
            lat = location['lat']
            lon = location['lon']
            return name, lat, lon
        else:
            return None, None, None   
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None, None 
    
def get_weather(lat,lon):
    url = 'https://api.openweathermap.org/data/3.0/onecall?'

    appid = os.getenv("OPEN_WEATHER_API_KEY")
    if not appid:
        print("Error: PEN_WEATHER_API_KEY not found in .env file")
        sys.exit(1)

    params = {
        'lat': lat,
        'lon': lon,
        'appid': appid,
        'units': 'metric'
    }

    # IMPORTANT: Script must include a custom User-Agent
    # headers = {
    #     'User-Agent': 'MyWeatherApp/1.0 (gonzaleztucci@gmail.com)'
    # }
    try:
        response = requests.get(url,params=params)

        response.raise_for_status() # Check for HTTP errors
        data = response.json()

        if data:
            print_weather_forecast(data['daily'])
            # location = data[0]
            # lat = location['lat']
            # lon = location['lon']
            # return lat, lon
        # else:
            # return None, None   
            # print(json.dumps(data['daily'], indent=4))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None



def print_weather_forecast(weather_data):
    """
    Parses weather API data and prints a formatted forecast for the terminal.
    """
    
    # Define the header format with specific spacing
    header = f"{'Date':<15} | {'Temp (Day/Night)':<20} | {'Condition':<25} | {'Rain':<10} | {'Wind':<15}"
    separator = "-" * len(header)
    
    print(separator)
    print(header)
    print(separator)

    for day in weather_data:
        # 1. Convert timestamp (dt) to readable date
        # The API uses Unix timestamps (seconds since 1970)
        dt_object = datetime.datetime.fromtimestamp(day['dt'])
        date_str = dt_object.strftime("%a, %b %d")  # e.g., "Mon, Jan 21"

        # 2. Extract Temperatures
        temp_day = day['temp']['day']
        temp_night = day['temp']['night']
        temp_str = f"{temp_day:.1f}°C / {temp_night:.1f}°C"

        # 3. Extract Weather Condition
        # We grab the description from the first item in the 'weather' list
        condition = day['weather'][0]['description'].capitalize()
        
        # 4. Extract Rain (Safely)
        # 'rain' key might be missing on dry days, so we default to 0
        rain_amount = day.get('rain', 0)
        rain_str = f"{rain_amount} mm" if rain_amount > 0 else "-"

        # 5. Extract Wind Speed
        wind_speed = day['wind_speed']
        wind_str = f"{wind_speed} m/s"

        # Print the formatted row
        print(f"{date_str:<15} | {temp_str:<20} | {condition:<25} | {rain_str:<10} | {wind_str:<15}")

    print(separator)


location = input("Enter the location: ")
name, latitude, longitude = get_coordinates(location)


if latitude:
    print(f"Found: Name: {name}, Lat {latitude}, Lon {longitude}")
    get_weather(latitude,longitude)
else:
    print("Place not found")

# serviceurl = 'https://api.openweathermap.org/data/3.0/onecall?'

# # Additional detail for urllib
# # http.client.HTTPConnection.debuglevel = 1

# # conn = sqlite3.connect('weather.sqlite')
# # cur = conn.cursor()

# # cur.execute('''
# # CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# # fh = open("where.data")
# count = 0
# nofound = 0
# # for line in fh:
# #     if count > 100 :
# #         print('Retrieved 100 locations, restart to retrieve more')
# #         break

# #     address = line.strip()
# #     print('')
# #     cur.execute("SELECT geodata FROM Locations WHERE address= ?",
# #         (memoryview(address.encode()), ))

# #     try:
# #         data = cur.fetchone()[0]
# #         print("Found in database", address)
# #         continue
# #     except:
# #         pass

# parms = dict()


# parms['lat'] = '39.4833'
# parms['lon'] = '-0.3667'
# parms['appid'] = '9f0c1ea5ca4ca5b8f4793ed892c39d7b'

# url = serviceurl + urllib.parse.urlencode(parms)

# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
# count = count + 1

# try:
#     js = json.loads(data)
# except:
#     print(data)  # We print in case unicode causes an error
#     # continue

# # if not js or 'features' not in js:
# #     print('==== Download error ===')
# #     print(data)
# #     break

# # if len(js['features']) == 0:
# #     print('==== Object not found ====')
# #     nofound = nofound + 1

# # cur.execute('''INSERT INTO Locations (address, geodata)
# #     VALUES ( ?, ? )''',
# #     (memoryview(address.encode()), memoryview(data.encode()) ) )

# # conn.commit()

# # if count % 10 == 0 :
# #     print('Pausing for a bit...')
# #     time.sleep(5)

# # if nofound > 0:
# #     print('Number of features for which the location could not be found:', nofound)

# # print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

