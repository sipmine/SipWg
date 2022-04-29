from aiogram.types import reply_keyboard
from aiogram.types.reply_keyboard import KeyboardButton
from db import create, find_by_id
from newclient import configFile
from userconf import createFile 

# from safe import BOT_TOKEN

import logging
from aiogram import Bot, Dispatcher, executor, types


# add button on keyboard


# add guide how install vpn

# configure config
logging.basicConfig(level=logging.INFO)

# init bot
BOT_TOKEN = "5159971668:AAHopjga0bOGUNp3m8eZRZ5eNsvE4hfzHEw"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


button_info = types.KeyboardButton("/guide")
button_getvpn = types.KeyboardButton("/getvpn")
main_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_info)
main_kb.add(button_getvpn)

print("all commands bot:\n start \n help \n testreg \n")
# start message 
@dp.message_handler(commands="start")
async def cheack_commands(msg: types.message):
    user_id = msg.from_user.id 
    user_name = str(msg.from_user.username)
    create(user_id, user_name)
    await msg.answer("Привет! \n /getvpn даст тебе файл с vpn. \n /guide инструкция по установке", reply_markup=main_kb)

# get info bot

@dp.message_handler(commands="guide")
async def guide_commands(msg: types.message):
    await msg.answer('''И так чтобы пользоваться впн на мобильном устройстве зайди в (AppStore / Google Play) найди там приложение WireGuard. 
Теперь жмёшь плюсик и нажимаешь импорт из файла (скачай файл, который дал бот). ОБЯЗАТЕЛЬНО СКАЧЕННЫЙ ФАЙЛ ПРЕМЕНУЙТЕ У СЕБЯ НА ТЕЛЕФОНЕ.
Вот и всё нажимай включить и радуйся :).
На пк всё просто переходим на этот сайт и устанавливай https://www.wireguard.com/install/ дальше загружаем свой конфиг файл и радуемся''')




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
