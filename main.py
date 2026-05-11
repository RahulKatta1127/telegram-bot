import os
import logging
from google import genai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Reply function
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        user_message = update.message.text

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_message
        )

        ai_reply = response.text

        await update.message.reply_text(ai_reply)

    except Exception as e:
        logging.error(f"ERROR: {e}")

        await update.message.reply_text(
            "AI failed to respond."
        )

# Telegram app
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Message handler
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        reply
    )
)

print("AI Bot Running...")

# Run bot
app.run_polling()
