import config
import requests


def get_weather(zipp):
    URL = f'http://api.openweathermap.org/data/2.5/weather?'
    params = {
        "zip": zipp,
        "units": "imperial",
        "appid": config.weatherToken
    }
    r = requests.get(URL, params=params)
    res = r.json()
    return res


def getTemp(zipp):
    temp = get_weather(zipp)['main']['temp']
    city = get_weather(zipp)['name']
    return f"\nThe temperature in {city} is {temp} \n"


def getWind(zipp):
    wind = get_weather(zipp)['wind']['speed']
    degree = get_weather(zipp)['wind']['deg']
    gust = get_weather(zipp)['wind']['gust']
    city = get_weather(zipp)['name']
    return f"\nThe wind speed in {city} is {wind}, the direction is {degree}°, and the gust speed is {gust} \n"


def getLoc(zipp):
    lon = get_weather(zipp)['coord']['lon']
    lat = get_weather(zipp)['coord']['lat']
    city = get_weather(zipp)['name']
    return f"\nThe latitude and longitude of {city} is {lat}, and {lon}. \n"
