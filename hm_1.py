from aiogram import Bot,Dispatcher,types,executor
import config
import random
bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(text=[1,2,3])
async def rando(message: types.Message):
    user = int(message.text)
    randomi = random.randint(1,3)
    if randomi == user:
        await message.reply(f"Правильно вы отгадали: {randomi}")
    else:
        await message.reply(f"Вы не угадали: {randomi}")

executor.start_polling(dp)