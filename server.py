from db import create, find_by_id
from newclient import configFile
from userconf import createFile 

from safe import BOT_TOKEN

import logging
from aiogram import Bot, Dispatcher, executor, types


# configure config
logging.basicConfig(level=logging.INFO)
print(BOT_TOKEN)
# init bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
print("all commands bot:\n start \n help \n testreg \n")
# start message 
@dp.message_handler(commands="start")
async def cheack_commands(msg: types.message):
    user_id = msg.from_user.id 
    user_name = str(msg.from_user.username)
    create(user_id, user_name)
    await msg.answer("Привет! \n список мойх функций /help ")

# get info bot
@dp.message_handler(commands="help")
async def help_commands(msg: types.message):
    await msg.answer("Получить доступ к vpn /getvpn")


# get vpn
@dp.message_handler(commands="getvpn")
async def getvpn(msg: types.message):
    # init  var
    user_id = msg.from_user.id
    username = msg.from_user.username
    id_on_db = find_by_id(user_id)

    # media 
    media = types.MediaGroup()
    # create config file
    configFile(username, id_on_db)
    createFile(username, id_on_db)
    media.attach_document(types.InputFile(f'{username}_wg.conf'), "vpn file")
    await msg.answer("Ваш файл")
    await msg.answer_media_group(media=media)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
