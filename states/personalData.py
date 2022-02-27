from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalDate(StatesGroup):
    fullname = State()
    email = State()
    descriptions = State()
    phoneNum = State()