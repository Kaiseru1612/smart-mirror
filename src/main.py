from forcastIO.forecastIO import Weather
from location.location import UserLocation

def main():
    location = UserLocation()
    location.get_location()
    print(location.get_user_long())
    print('---')
    print(location.get_user_lat())
    lat = location.get_user_lat()
    long = location.get_user_long()
    weather = Weather(lat, long)
    weather.get_current_weatherforecast()

main()