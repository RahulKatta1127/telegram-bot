import os
from google import genai
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
)

BOT_TOKEN = "8749833435:AAH601g8v-P28Q4L0bzHYeEJAQTxVu1W6hY"
GEMINI_API_KEY = "AIzaSyBkyGZrlZm24ZjYx0qBp2SheJeHTSKmuaE"

client = genai.Client(api_key=GEMINI_API_KEY)

async def reply(update, context):
    user_message = update.message.text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message,
    )

    await update.message.reply_text(response.text)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT, reply)
)

print("AI Bot Running...")

app.run_polling()
