import requests
import datetime, time
from config import TOKEN, TG_TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def startBot(message: types.Message):
    userFULL = message.from_user.full_name
    await message.reply(f" Hi, {userFULL} !\n"
                        f"Please enter the city whose weather you want to know\n"
                        )


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={TOKEN}&units=metric" # chosse the language - > add the  "&lang=ua"

        )
        OutputData = req.json()
        area = OutputData['sys']['country']
        CityName = OutputData['name']
        temp = OutputData['main']['temp']
        feels = OutputData['main']['feels_like']
        speed_wind = OutputData['wind']['speed']
        humidity = OutputData['main']['humidity']
        pressure = OutputData['main']['pressure']
        weather = OutputData['weather'][0]['description']
        sunrise = datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(OutputData['sys']['sunset'])
        bright_PartOfTheDay = datetime.datetime.fromtimestamp(OutputData['sys']['sunset']) - datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])

        #print(f"Current time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

        await message.reply(f" Current time2 {time.asctime()}\n"
              f" City - > {CityName};  Сountry - > {area};\n"
              f" Shortly - > {weather};\n temperature - > {temp} °C; "
              f" Temperature Feels Like - > {feels}°C;\n Speed of Wind - > {speed_wind} mps;\n"
              f" Humidity - > {humidity}%;\n Pressure - > {pressure*0.750062} mmHg;\n"
              f" Sunrise - > {sunrise};\n Sunset - > {sunset};\n"
              f" Bright Part Of The Day - > {bright_PartOfTheDay};")




    except:
        await message.reply("Check city name")



if __name__ == '__main__':
    executor.start_polling(dp)