from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import API_TOKEN                                    # Loading API
from database import db_start, create_profile, edit_profile     # Loading database code
from keyboards import get_kb, get_cancel_kb                     # Loading keyboards

# Launch
async def on_startup(_):
    await db_start()
    print("The server had been launched!")

# TODO: on_shutdown

# Creating bot, dispatcher and allocating memory for FSM
bot = Bot(API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

# Defining FSM states
class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


# Message handlers:

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text='Welcome! To create profile type /create',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.reply(text='Let\'s create your profile. Load your photo:',
                        reply_markup=get_cancel_kb())
    
    await create_profile(user_id=message.from_user.id)

    await ProfileStatesGroup.photo.set()


@dp.message_handler(commands=['cancel'], state=ProfileStatesGroup)
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return
    
    await state.finish()
    await message.reply(text='You\'ve interrupted creation',
                        reply_markup=get_kb())


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('That\'s not a photo!')


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    
    await message.reply('Type your name')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
    
    await message.reply('What\'s your age?')
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100, state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.reply('That\'s not an age!')


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text
    
    await message.reply('Tell about yourself')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_description(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['description'] = message.text

        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['name']}, {data['age']}\n{data['description']}")

    await edit_profile(state, user_id=message.from_user.id)
    await message.reply(text='You profile created succesfully',
                        reply_markup=get_kb())
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)