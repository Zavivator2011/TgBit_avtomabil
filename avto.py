import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from btn import *
from products import *


BOT_TOKEN = "6502882014:AAE31XBkaUL1HrUh4E1Wb7VwmbiGXDdLGQ8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
  await dp.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
    ]
  )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await message.answer("Salom birodar", reply_markup=menu)


@dp.message_handler(text='Yengil mashina')
async def Yengil_handler(message: types.Message):
  await message.answer("Mashina yurini tanlang", reply_markup=Yengil_menu)

@dp.message_handler(text='Poygachi')
async def Poyga_handler(message: types.Message):
  await message.answer("ichimlik  turini tanlang", reply_markup=Poygachi_menu)


@dp.message_handler(text='Yuk Moshina')
async def yuk_handler(message: types.Message):
  await message.answer("yuk mashina turini tanlang", reply_markup=Yuk_menu)


@dp.message_handler(text='Malibu2')
async def malibu_handler(message: types.Message):
  print(malibu)
  img = malibu['img']
  context = f"Nomi: {malibu['name']}\nNarxi: {malibu['price']}"
  await message.answer_photo(img, caption=context)



@dp.message_handler(text='Gentra')
async def gentra_handler(message: types.Message):
  print(gentra)
  img = gentra['img']
  gentra1 = f"Nomi: {gentra['name']}\nNarxi: {gentra['price']}"
  await message.answer_photo(img, caption=gentra1)



@dp.message_handler(text='Nexia2')
async def nexia_handler(message: types.Message):
  print(nexia)
  img = nexia[img]
  context = f"Nomi: {nexia['name']}\nNarxi: {nexia['price']}"
  await message.answer_photo(img, caption=context)




@dp.message_handler(text='Hunday')
async def hunday_handler(message: types.Message):
  print(hunday)
  img = hunday['img']
  context = f"Nomi: {hunday['name']}\nNarxi: {hunday['price']}"
  await message.answer_photo(img, caption=context)



@dp.message_handler(text='ortga')
async def disert_handler(message: types.Message):
  await start_bot(message)

if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)