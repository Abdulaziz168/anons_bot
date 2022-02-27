from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalDate


@dp.message_handler(Command("anketa"), state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalDate.fullname.set()


@dp.message_handler(state=PersonalDate.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzil kiriting")
    await PersonalDate.next()


@dp.message_handler(state=PersonalDate.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Sizda qanday muammo bo‘layotganligini to'liq yozing")

    await PersonalDate.next()


@dp.message_handler(state=PersonalDate.descriptions)
async def tell_description(message: types.Message, state: FSMContext):
    description = message.text

    await state.update_data(
        {"description": description}
    )

    await message.answer("Telefon raqam kiriting ")

    await PersonalDate.next()


@dp.message_handler(state=PersonalDate.phoneNum)
async def answer_email(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )

    # Ma'lumotlarni qayta o‘qiymiz
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    description = data.get("description")
    phone = data.get("phone")

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Muammo - {description}\n"
    msg += f"Telefon - {phone}\n"

    await message.answer(msg)

    await state.finish()
    await state.reset_state(with_data=False)
