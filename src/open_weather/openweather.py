import requests
from pprint import pprint

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d87d48cef6284bc4c6a99b581ea273c0 &units=metric'.format(city)

res = requests.get(url)

data = res.json()

print(data)

# temp = data['main']['temp']
# wind_speed = data['wind']['speed']

# latitude = data['coord']['lat']
# longitude = data['coord']['lon']

# description = data['weather'][0]['description']

# print('Temperature : {} degree celcius'.format(temp))
# print('Wind Speed : {} m/s'.format(wind_speed))
# print('Latitude : {}'.format(latitude))
# print('Longitude : {}'.format(longitude))
# print('Description : {}'.format(description))