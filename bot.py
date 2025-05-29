import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _

# Bot token
TOKEN = '7622069536:AAEs8Bzvkg7xFJ5LxW1gI0G1-KJW4HxOF_c'
ADMIN_ID = 7054963789  # Replace with your Telegram ID

# Logging
logging.basicConfig(level=logging.INFO)

# FSM States
class Register(StatesGroup):
    name = State()
    phone = State()

# Course description
COURSE_DESCRIPTION = """
🌟 *SUPER XOTIRA* 🌟
*Onlayn Masterklass*

📅 *Sana:* 29-30-may
⏰ *Davomiyligi:* 2 kun

🎯 *2 kun ichida siz o'rganasiz:*

✅ Qanday qilib diqqat-e'tiborni kuchaytirib, chalg'imasdan soatlab o'qish va ishlashni

✅ Dangasalikdagi muammolarni yengib reja bilan ishlashni

✅ Xotirani 10 barobar kuchaytirib, chet tili so'zlarini va istalgan ma'lumotlarni tez yod olishni

📌 *Muhim:* 
• Kanalni PIN qilib qo'ying
• Yangiliklarni diqqat bilan kuzatib boring

📢 *Masterklass kunigacha:*
• Foydali ma'lumotlar
• Muhim xabarlar
• Maxsus tavsiyalar

💫 *Siz hozir hayotingizni o'zgartirish uchun birinchi qadamni tashladingiz. Va ishoning, bu safar hammasi boshqacha bo'ladi!*

🔗 *Telegram kanal:* https://t.me/+yZkX7CKSlTc1Y2Ey

#SuperXotira #Masterklass #O'zbekiston
"""

# Keyboards
def main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Kurs haqida ma'lumot")],
            [KeyboardButton(text="🎯 Kursga qatnashish")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_contact_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

# Handlers
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum! Xush kelibsiz!\n\n"
        "📌 Quyidagi tugmalardan birini tanlang:",
        reply_markup=main_keyboard()
    )

@dp.message(F.text == "📚 Kurs haqida ma'lumot")
async def course_info_handler(message: types.Message):
    await message.answer(COURSE_DESCRIPTION)

@dp.message(F.text == "🎯 Kursga qatnashish")
async def register_handler(message: types.Message, state: FSMContext):
    await message.answer(
        "📝 Kursda qatnashish uchun ro'yxatdan o'tish kerak.\n"
        "✍️ Iltimos, to'liq ismingizni kiriting:"
    )
    await state.set_state(Register.name)

@dp.message(Register.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        "✅ Rahmat! Endi telefon raqamingizni yuborish uchun quyidagi tugmani bosing:",
        reply_markup=get_contact_keyboard()
    )
    await state.set_state(Register.phone)

@dp.message(Register.phone, F.contact)
async def process_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    phone = message.contact.phone_number
    
    # Send confirmation to user
    await message.answer(
        f"🎉 Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n\n"
        f"👤 Ism: {name}\n"
        f"📱 Telefon: {phone}\n\n"
        "⏳ Tez orada siz bilan bog'lanamiz! 😊",
        reply_markup=main_keyboard()
    )
    
    # Send registration data to admin
    admin_message = (
        f"🆕 Yangi ro'yxatdan o'tgan foydalanuvchi:\n\n"
        f"👤 Ism: {name}\n"
        f"📱 Telefon: {phone}\n"
        f"👤 Username: @{message.from_user.username if message.from_user.username else 'Mavjud emas'}"
    )
    await message.bot.send_message(ADMIN_ID, admin_message)
    
    await state.clear()

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 