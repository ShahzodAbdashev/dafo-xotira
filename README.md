# Super Xotira Telegram Bot

Bu bot orqali foydalanuvchilar "Super Xotira" masterklassiga ro'yxatdan o'tishlari va kurs haqida ma'lumot olishlari mumkin.

## Bot funksionalligi

1. **Asosiy menyu**
   - Kurs haqida ma'lumot olish
   - Kursga ro'yxatdan o'tish

2. **Ro'yxatdan o'tish jarayoni**
   - Foydalanuvchi ismini kiritish
   - Telefon raqamini yuborish
   - Ro'yxatdan o'tish tasdiqlanadi
   - Foydalanuvchiga maxsus fayl yuboriladi

3. **Admin paneli**
   - Yangi ro'yxatdan o'tgan foydalanuvchilar haqida ma'lumot
   - Foydalanuvchi ID, ism va telefon raqami

## O'rnatish va ishga tushirish

1. Kerakli paketlarni o'rnatish:
```bash
pip install -r requirements.txt
```

2. `.env` faylini yaratish va bot tokenini qo'shish:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_telegram_id
```

3. Botni ishga tushirish:
```bash
python bot.py
```

## Fayl yuborish

Ro'yxatdan o'tish muvaffaqiyatli yakunlangandan so'ng, foydalanuvchiga quyidagi fayllar yuboriladi:
- Kurs dasturi
- Tayyorgarlik bo'yicha ko'rsatmalar
- Qo'shimcha ma'lumotlar

## Eslatma

Bot tokenini [@BotFather](https://t.me/botfather) orqali olishingiz mumkin. 