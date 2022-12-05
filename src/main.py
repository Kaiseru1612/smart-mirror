from forcastIO.forecastIO import Weather
from location.location import UserLocation
from newspaper.NewsFetcher import NewsFetcher

def main():
    location = UserLocation()
    location.get_location()
    print(location.get_user_long())
    print('---')
    print(location.get_user_lat())
    lat = location.get_user_lat()
    long = location.get_user_long()
    weather = Weather(lat, long)
    weather.create_fio()
    weather.get_current_weatherforecast()
    news = NewsFetcher("523505cd243b45d599b136431677a833")
    # print(news.FetchFromBBC())
    # print(weather.humidity)

main()