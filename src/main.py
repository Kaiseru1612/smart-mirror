from glob import glob
import time
from tkinter import Button
from unittest import case
from forcastIO.forecastIO import Weather
from location.location import UserLocation
from newspaper.NewsFetcher import NewsFetcher
from gui import window

location_flag = False
weather_flag = False
news_flag = False
init_flag = False

window = window

def init_state():
    print(1)


    global location
    location = UserLocation()
    location.get_location()

    global location_flag
    location_flag = True

    global weather 
    lat = location.get_user_lat()
    long = location.get_user_long()
    weather = Weather(lat, long)
    # weather.create_fio()
    
    global news
    news = NewsFetcher()

    global init_flag 
    init_flag = True

def fetch_data():
    print(2)

    global weather
    # weather.get_current_weatherforecast()
    weather.humidity = 66
    weather.temperature = 30
    global weather_flag 
    weather_flag = True

    global news
    news.FetchFromBBC()
    global news_flag
    news_flag = True

def display_data():
    global current_state
    global display_counter
    if display_counter < 10:
        window.update_idletasks()
        window.update()
        time.sleep(1)
        display_counter += 1
    else:
        window.quit()


def process_voice():
    pass

def execute_command():
    pass

def switch(state):
    return switcher.get(state)()

switcher = {
    1: init_state,
    2: fetch_data,
    3: display_data,
    4: process_voice,
    5: execute_command,
    }

display_counter = 0
def increase_counter():
    global display_counter
    display_counter+=1

def switch_state():
    global location_flag
    global weather_flag
    global news_flag
    global current_state
    global display_counter
    if init_flag is True and weather_flag is False:
        current_state = 2
    elif location_flag is True and weather_flag is True and news_flag is True and display_counter < 10:
        current_state = 3
    elif display_counter >= 10:
        weather_flag = False
        news_flag = False
        display_counter = 0
        current_state = 2

    print(display_counter)
    print(current_state)

def run_state():
    global location_flag
    global weather_flag
    global news_flag
    global current_state
    global display_counter
    if current_state == 1:
        switch(1)
    elif current_state == 2:
        switch(2)
    elif current_state == 3:
        switch(3)

def main_program():
    # location = UserLocation()
    # location.get_location()
    # print(location.get_user_long())
    # print('---')
    # print(location.get_user_lat())
    # lat = location.get_user_lat()
    # long = location.get_user_long()
    # weather = Weather(lat, long)
    # weather.get_current_weatherforecast()
    while True:
        switch_state()
        run_state()

        


current_state=1
switch(state=1)
main_program()