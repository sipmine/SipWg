from db import create


import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = "5159971668:AAHopjga0bOGUNp3m8eZRZ5eNsvE4hfzHEw"

# configure config
logging.basicConfig(level=logging.INFO)

# init bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
print("all commands bot:\n start \n help \n testreg \n")
# start message 
@dp.message_handler(commands="start")
async def cheack_commands(msg: types.message):
    user_id = msg.from_user.id
    user_name = str(msg.from_user.first_name)
    create(user_id, user_name)
    await msg.answer("Привет! \n список мойх функций /help ")

# get info bot
@dp.message_handler(commands="help")
async def help_commands(msg: types.message):
    await msg.answer("Получить доступ к vpn /getvpn")

    
@dp.message_handler(commands="getvpn")
async def getvpn(msg: types.message):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
