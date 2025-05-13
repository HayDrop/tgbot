import asyncio
from aiogram import bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
import os
TOKEN = os.getenv("TOKEN")
bot = bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command(commands = ["start"]))
async def cmd_start(message: types.Message):

    kb = [[KeyboardButton(text="Какие есть моды на данный момент?")], [KeyboardButton(text="Какие есть плагины на данный момент?")], [KeyboardButton(text="У вас есть дискорд для общения?")], [KeyboardButton(text="Вас можно как-то поддержать?")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Здраствуйте вы попапали в бота в котором вы можете скачать большенство модов из роликов канала СеноДроп вот ссылка на канал (https://www.youtube.com/@HayDrop) также другие интересные моды! Ну, с чего начнём?", reply_markup=keyboard)

@dp.message()
async def handle_message(message: types.Message):

    if message.text=="Какие есть моды на данный момент?":
        kb = [[KeyboardButton(text="Мод на оружие")],[KeyboardButton(text="Мод на пароплан")], [KeyboardButton(text="Назад")]]
        keyboard3 = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer("Моды в наличии",reply_markup=keyboard3)
        await message.answer("Также есть мод на пароплан ---> https://www.curseforge.com/minecraft/mc-mods/paragliders")

    elif message.text == "Мод на оружие":
        await message.answer("Мод на оружие ---> https://www.curseforge.com/minecraft/mc-mods/timeless-and-classic-guns-tac")

    elif message.text == "Мод на пароплан":
        await message.answer("Мод на пароплан https://www.curseforge.com/minecraft/mc-mods/paragliders")

    elif message.text=="Какие есть плагины на данный момент?":
        await message.answer("На данный момоент плагины ещё не готовы 😥😭😢")
        await message.answer("Но мы вам сообщим если они будут готовы 😀😉😅")

    elif message.text=="У вас есть дискорд для общения?":
        await message.answer("Да у нас есть свой дискорд канал для общения, чтобы стать частью семьи перейдите по ссылке")
        await message.answer("https://discord.com/invite/nJ3uFYfUfv")

    elif message.text=="Вас можно как-то поддержать?":
        await message.answer("Да на данный момент вы можете поддержать нас на сайте для донатов, вот ссылка на сайт")
        await message.answer("https://www.donationalerts.com/r/haydrop")
        await message.answer("также вы можете поддержать нашу команду морально вот по этим ссылкам")
        await message.answer("https://www.youtube.com/@HayDrop")
        await message.answer("https://www.youtube.com/@itsDester")
        await message.answer("https://youtube.com/@kokosik480?si=o-uDsG2UJm0XZQy7")

    elif message.text == "Назад":
        kb = [[KeyboardButton(text="Какие есть моды на данный момент?")],
              [KeyboardButton(text="Какие есть плагины на данный момент?")],
              [KeyboardButton(text="У вас есть дискорд для общения?")],
              [KeyboardButton(text="Вас можно как-то поддержать?")]]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer("Главное меню", reply_markup=keyboard)

    else:
        photo = FSInputFile('screen.PNG')
        await message.answer_photo(photo,caption="Извините но для того что-бы пользоваться ботом используйте кнопку как на скришоте 😅😅😅")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())