# Telegram Course Registration Bot

This is a Telegram bot that provides course information and handles course registration.

## Features

- Course information display
- Course registration with name and phone number collection
- Beautiful UI with emojis and formatted text

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Telegram bot token:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

3. Run the bot:
```bash
python bot.py
```

## How to Use

1. Start the bot by sending `/start` command
2. Choose between two options:
   - "Kurs haqida to'liq ma'lumot olmoqchiman" - Get detailed course information
   - "Kursda qatnashmoqchiman" - Register for the course

## Note

Make sure to get your bot token from [@BotFather](https://t.me/botfather) on Telegram. 