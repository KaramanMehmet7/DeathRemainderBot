import logging
from telegram import Update
from telegram.ext import ApplicationBuilder
import schedule
import time
import asyncio


API_TOKEN = "7864569160:AAF0xn7iVgfsKComkBXx5Mwhyv6SZFleFU8"
CHAT_ID = "5578759592"


app = ApplicationBuilder().token(API_TOKEN).build()


async def olum_hatirlat():
    mesaj = "Fani'den faniye mesaj. Ölüm var!"
    await app.bot.send_message(chat_id=CHAT_ID, text=mesaj)
    print("Mesaj Gönderildi!")


schedule.every().day.at("01:00").do(lambda: asyncio.run(olum_hatirlat()))


while True:
    schedule.run_pending()
    time.sleep(60)  
