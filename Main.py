import urllib.request
import requests
from requests import get
from yaspin import yaspin
from yaspin.spinners import Spinners
import time
from prettytable import PrettyTable
# Weather app Version 1



def WeatherInfo():

    #Grabs Public Ip address than makes a request to a geocoding api and returns Latitude/Longitude
    IP = external_ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
    Geocoding = get(f'https://ipapi.co/8.8.8.8/json').json()
    global Country
    Country = Geocoding["country_name"]
    Latitude = (Geocoding["latitude"])
    Longitude = (Geocoding["longitude"])

    Weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={Latitude}&longitude={Longitude}&daily=temperature_2m_max,temperature_2m_min&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1&timezone=auto")
    WeatherJson = Weather.json()
    currentForecast = (WeatherJson["current_weather"])
    DailyForecast = WeatherJson["daily"]


    # Current Forecast
    global CurrentTemp
    CurrentTemp = currentForecast["temperature"]
    
    global MaxTemp
    MaxTemp = DailyForecast["temperature_2m_max"]

    global MinTemp
    MinTemp = DailyForecast["temperature_2m_min"]
    

    return CurrentTemp, MaxTemp, MinTemp, Country


WeatherInfo()

def initTui():
    x = PrettyTable()
    x.field_names = ["Country", "Current Temperature ", "Min Temperature ", "Max Temperature"]
    x.add_row([Country, CurrentTemp, MinTemp, MaxTemp])
    print(x)

initTui()
