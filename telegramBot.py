from aiogram import Bot, Dispatcher, executor, types
import python_weather




bot = Bot(token="5534999839:AAGMryEHx-97MJv7CICSaQntGPK-otIzIf8")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-Ru")


@dp.message_handler()
async def echo(message: types.Message):
        weather = await client.find(message.text)

        celsius = (weather.current.temperature - 32) / 1.8

        resp_n = weather.location_name + "\n"
        resp_n += f"Текущая температура: {round(celsius)}\n"
        resp_n += f"Cостояние погоды: {weather.current.sky_text}"

        await message.answer(resp_n)

if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)
        # await client.close()


