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
    #user_id = message.from_user.id


@dp.message_handler(text=["JNK"])
async def startBot(message: types.Message):
    await message.reply(f"Returns TRUE!!! \U0001FAE1\n")


@dp.message_handler()
async def get_weather(message: types.Message):
    smileUpdate = {
        "Clear": "\U00002600",
        "Clouds": "\U00002601",
        "Rain": "\U00002614",
        "Drizzle": "\U00002614",
        "Thunderstorm": "\U000026A1",
        "Snow": "\U0001F328",
        "Mist": "\U0001F32B"
    }
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={TOKEN}&units=metric&lang=ru" # chosse the language - > add the  "&lang=ua"

        )
        OutputData = req.json()
        area = OutputData['sys']['country']
        CityName = OutputData['name']
        temp = OutputData['main']['temp']
        feels = OutputData['main']['feels_like']
        speed_wind = OutputData['wind']['speed']
        humidity = OutputData['main']['humidity']
        pressure = OutputData['main']['pressure']
        weather = OutputData['weather'][0]['main']
        if weather in smileUpdate:
            smiles = smileUpdate[weather]
        else:
            smiles = "Press F to pay respect \U0001FAE1 \U0001FAE1 \U0001FAE1"
        sunrise = datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(OutputData['sys']['sunset'])
        bright_PartOfTheDay = datetime.datetime.fromtimestamp(OutputData['sys']['sunset']) - datetime.datetime.fromtimestamp(OutputData['sys']['sunrise'])

        #print(f"Current time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        #f" Current time {time.asctime()}\n
        await message.reply(f"Current time {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f" City - > {CityName};  Сountry - > {area};\n"
              f" Shortly - > {weather} {smiles};\n temperature - > {temp} °C; "
              f" Temperature Feels Like - > {feels}°C;\n Speed of Wind - > {speed_wind} mps;\n"
              f" Humidity - > {humidity}%;\n Pressure - > {pressure*0.750062} mmHg;\n"
              f" Sunrise - > {sunrise};\n Sunset - > {sunset};\n"
              f" Bright Part Of The Day - > {bright_PartOfTheDay};")




    except:
        await message.reply("Check city name\nAnd enter the correct city name like: 'Kyiv' 'Київ' ")



if __name__ == '__main__':
    executor.start_polling(dp)