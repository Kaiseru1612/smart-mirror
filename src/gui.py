
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from forcastIO.forecastIO import Weather
from location.location import UserLocation
from newspaper.NewsFetcher import NewsFetcher
import time
import calendar
from datetime import date

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

today = date.today()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("480x280")
window.configure(bg = "#BFBFBF")


location = UserLocation()
location.get_location()
print(location.get_user_long())
print('---')
print(location.get_user_lat())
lat = location.get_user_lat()
long = location.get_user_long()
weather = Weather(lat, long)
# weather.create_fio()
# weather.get_current_weatherforecast()
print(weather.temperature)
print(weather.humidity)
# news = NewsFetcher()
# print(news.FetchFromBBC())

t = time.localtime()
current_time = time.strftime("%H:%M", t)

canvas = Canvas(
    window,
    bg = "#BFBFBF",
    height = 280,
    width = 480,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    83.0,
    135.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    355.0,
    144.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    83.0,
    206.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    50.0,
    57.0,
    image=image_image_4
)

canvas.create_text(
    39.0,
    30.0,
    anchor="nw",
    text="Ho Chi Minh City",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    66.72000122070312,
    52.866668701171875,
    anchor="nw",
    text=weather.temperature,
    fill="#FFFFFF",
    font=("Inter SemiBold", 10 * -1)
)

canvas.create_text(
    103.0,
    130.0,
    anchor="nw",
    text="32°C\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    103.0,
    154.0,
    anchor="nw",
    text="31°C\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    104.0,
    177.0,
    anchor="nw",
    text="33°C\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    103.0,
    200.0,
    anchor="nw",
    text="32°C\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    102.0,
    225.0,
    anchor="nw",
    text="31°C\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    102.0,
    248.0,
    anchor="nw",
    text="33°C\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    40.0,
    82.0,
    anchor="nw",
    text="Partly Cloudy",
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    365.0,
    58.0,
    anchor="nw",
    text=today.strftime("%B %d, %Y"),
    fill="#FFFFFF",
    font=("Inter SemiBold", 8 * -1)
)

canvas.create_text(
    396.0,
    30.0,
    anchor="nw",
    text=calendar.day_name[today.weekday()],
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    389.0,
    76.0,
    anchor="nw",
    text=current_time,
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    80.0,
    114.0,
    image=image_image_5
)

canvas.create_text(
    41.0,
    130.0,
    anchor="nw",
    text="Mon",
    fill="#FFFFFF",
    font=("Inter Bold", 8 * -1)
)

canvas.create_text(
    41.0,
    154.0,
    anchor="nw",
    text="Tue",
    fill="#FFFFFF",
    font=("Inter Bold", 8 * -1)
)

canvas.create_text(
    41.0,
    177.0,
    anchor="nw",
    text="Wed",
    fill="#FFFFFF",
    font=("Inter Bold", 8 * -1)
)

canvas.create_text(
    41.0,
    200.0,
    anchor="nw",
    text="Thur",
    fill="#FFFFFF",
    font=("Inter Bold", 8 * -1)
)

canvas.create_text(
    41.0,
    225.0,
    anchor="nw",
    text="Fri",
    fill="#FFFFFF",
    font=("Inter Bold", 8 * -1)
)

canvas.create_text(
    41.0,
    248.0,
    anchor="nw",
    text="Sat",
    fill="#FFFFFF",
    font=("Inter Bold", 8 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    83.0,
    160.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    83.0,
    183.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    83.0,
    228.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    83.0,
    251.0,
    image=image_image_9
)

canvas.create_text(
    374.0,
    130.0,
    anchor="nw",
    text="Brazil dismantle South Korea to dance into quarter-finals",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

window.resizable(False, False)
