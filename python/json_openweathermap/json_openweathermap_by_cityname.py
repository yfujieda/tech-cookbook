"""
This is an example Python program to get weather info from OpenWeatherMap

github: https://github.com/yfujieda
twitter: https://twitter.com/yfujieda_
Date: 09/22/2018

######################################

Open WeatherMap Examples:
https://openweathermap.org/current

By city name API call
api.openweathermap.org/data/2.5/weather?q={city name}

Example:
api.openweathermap.org/data/2.5/weather?q=London
"""

import requests

OWM_API = "https://api.openweathermap.org/data/2.5/weather"
city_name = "london"
APPID = "<USE YOUR API KEY>"

# parameters to send along with REST API Endpoint
payload = {'q': city_name, 'APPID': APPID}

# make a requests call using GET (including parameters)
r = requests.get(OWM_API, params=payload)

# print(r.url)
# print(r.json())

# get the returns json data
json_data = r.json()

# temperature is stored in main > temp (in the form of Kelvin)
temp_in_kelvin = json_data['main']['temp']
temp_in_celcius = temp_in_kelvin - 273.15

print(f'Temp in K: {temp_in_kelvin}')
print(f'Temp in C: {temp_in_celcius}')
