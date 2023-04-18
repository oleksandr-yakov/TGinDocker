import requests
import datetime, time
from pprint import pprint
from config import TOKEN
 
#name WeatherFrom_bot main:WeatherMap


def get_weather(city, TOKEN):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}&units=metric" # chosse the language - > add the  "&lang=ua"

        )
        OutputData = req.json()
        area = OutputData['sys']['country']
        CityName = OutputData['name']
        temp = OutputData['main']['temp']
        feels = OutputData['main']['feels_like']
        speed_wind = OutputData['wind']['speed']
        humidity = OutputData['main']['humidity']
        pressure = OutputData['main']['pressure']
        print(type(pressure))
        print(pressure *0.750062)
        weather = OutputData['weather'][0]['description']
        sunrise = datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(OutputData['sys']['sunset'])
        bright_PartOfTheDay = datetime.datetime.fromtimestamp(OutputData['sys']['sunset']) - datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])

        #print(f"Current time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"Current time2 {time.asctime()}")

        print(f" City - > {CityName};  Сountry - > {area};\n"
              f" Shortly - > {weather};\n temperature - > {temp} °C; "
              f" Temperature Feels Like - > {feels}°C;\n Speed of Wind - > {speed_wind} mps;\n"
              f" Humidity - > {humidity}%;\n Pressure - > {pressure*0.750062} mmHg;\n"
              f" Sunrise - > {sunrise};\n Sunset - > {sunset};\n"
              f" Bright Part Of The Day - > {bright_PartOfTheDay};")




    except Exception as ex:
        print(ex, "Check city name", sep='\n')


def main(): 
    city = input("Please enter the city whose weather you want to know\n")
    get_weather(city, TOKEN)


if __name__ == '__main__':
    main()