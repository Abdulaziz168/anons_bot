from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

tugilgan_uy_qismatim = ["https://youtu.be/U8Du20QdUws"]
qora_niyat = ["https://youtu.be/q4LTny8siqU"]
omonat = ["https://youtu.be/NaN3_ygWgw4"]
olchalar_mavsumi = ["https://youtu.be/momLPmTjCEo"]
melek = ["https://youtu.be/3mdZNdcfCA0"]
jasur_yurak = ["https://youtu.be/wEHkK2TU-FE"]
qirmizi_xona = ["https://youtu.be/X9UYmbn5d1k"]


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton(text="To‘lov qanday qilinadi? 💸")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Anonslar 📲")
    keyboard.add(button_2)
    button_3 = "Video qo‘llanmani ko'rish 🎞"
    keyboard.add(button_3)
    button_4 = "Muammo haqida xabar qiling!"
    keyboard.add(button_4)
    button_5 = "back"
    keyboard.add(button_5)
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "To‘lov qanday qilinadi? 💸")
async def with_puree(message: types.Message):
    msg = '''
        “Sevimli play” platformasi oʻz faoliyatini pullik tizimda davom ettiradi. Turkiya seriallarini toʻliq tomosha qilish uchun oylik abonent toʻlovi 11 000 soʻm. 
Yangi tizimdan foydalanish uchun:
1. Mobil qurilma yoki kompyuter brauzeri orqali www.sevimliplay.tv saytiga kiriladi.
2. Kirish tugmasi bosiladi, login-parol terib, akkautga kiriladi.
3. Obunalar boʻlimiga oʻtib, karta orqali 11 000 soʻm toʻlanadi.
4. Jarayon tugagach, ilovaga qayta kirib, 1 oy davomida platformadan toʻliq foydalansa bo‘ladi!
    '''
    await message.reply(msg)


@dp.message_handler(lambda message: message.text == "Video qo‘llanmani ko'rish 🎞")
async def get_video_paid(message: types.Message):
    link_video_qollanma = "https://www.youtube.com/watch?v=tlE-E3ENctw"
    await message.reply(link_video_qollanma)


keyboard = types.ReplyKeyboardMarkup(row_width=3)
button_1 = types.InlineKeyboardButton(text="Tug‘ilgan uy qismatim 👨‍👩‍👧‍👧")
button_2 = types.InlineKeyboardButton(text="Qora niyat 🖤")
button_3 = types.InlineKeyboardButton(text="Omonat 💶")
button_4 = types.InlineKeyboardButton(text="Olchalar mavsumi 🍒")
button_5 = types.InlineKeyboardButton(text="Melek 🥀")
button_6 = types.InlineKeyboardButton(text="Jasur yurak ❤")
button_7 = types.InlineKeyboardButton(text="Qirmizi xona 🌹")
button_back = types.InlineKeyboardButton(text="back")
keyboard.add(button_1, button_6, button_5, button_4, button_2, button_3, button_7, button_back)


@dp.message_handler(lambda message: message.text == "Anonslar 📲")
async def without_puree(message: types.Message):
    await message.reply("Ajoyib tanlov!", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Tug‘ilgan uy qismatim 👨‍👩‍👧‍👧")
async def with_puree(message: types.Message):
    for x in tugilgan_uy_qismatim:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "Qora niyat 🖤")
async def with_puree(message: types.Message):
    for x in qora_niyat:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "Omonat 💶")
async def with_puree(message: types.Message):
    for x in omonat:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "Olchalar mavsumi 🍒")
async def with_puree(message: types.Message):
    for x in qora_niyat:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "Melek 🥀")
async def with_puree(message: types.Message):
    for x in melek:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "Jasur yurak ❤")
async def with_puree(message: types.Message):
    for x in jasur_yurak:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "Qirmizi xona 🌹")
async def with_puree(message: types.Message):
    for x in qirmizi_xona:
        await message.reply(x)


@dp.message_handler(lambda message: message.text == "back")
async def get_back(t):
        await bot_start()