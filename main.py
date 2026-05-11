import os
import logging
from google import genai
from telegram.ext import ApplicationBuilder, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)

async def reply(update, context):
    try:
        user_message = update.message.text

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_message,
        )

        await update.message.reply_text(response.text)

    except Exception as e:
        await update.message.reply_text("Error: AI failed to respond.")
        print(e)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("AI Bot Running...")

app.run_polling()
