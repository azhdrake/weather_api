import requests
import os
from datetime import datetime

city = input('What city are do you want to know the weather of? ')
country = input('What is the two letter country code of where you want to know the weather of? ')

# get's the weather key from the OS
key = os.environ.get('WEATHER_KEY')

# the API call
url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {'q' : city + ',' + country, 'units' : 'imperial', 'appid' : key}
weather_data = requests.get(url = url, params = params).json()

# Using the data.
for time in weather_data['list']:
    temp_f   = time['main']['temp']
    weather  = time['weather'][0]['description']
    wind     = time['wind']['speed']
    dt = datetime.fromtimestamp(time['dt'])
    print(f'At {dt} it\'s {weather} and {temp_f:.2f}F. The wind is blowing at {wind} speed units per temporal units.')

# I used local time because I figure this app is most likely going to be used to look up local weather.
# Even if someone's traveling to somewhere else and want's to know the forcast there I think it's easier to understand using local time then UTC.
# Ideally the app would use the timezone of the place where the weather is being looked up, but that is beyond scope.