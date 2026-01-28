import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)
from openai import OpenAI

# ENV variables
BOT_TOKEN = os.getenv("8478711385:AAEiVIwb9d0HhSOGyE746pzCmf9Z9qrxakQ")
OPENAI_API_KEY = os.getenv("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")

client = OpenAI(api_key=OPENAI_API_KEY)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 আমি DoubtSource AI!\n"
        "যেকোনো পড়াশোনার প্রশ্ন করো, আমি বুঝিয়ে দেবো 😊"
    )

# AI reply function
async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly Bangla AI tutor. "
                        "Explain answers simply for students. "
                        "Ask follow-up questions if needed."
                    )
                },
                {"role": "user", "content": user_question}
            ],
            max_tokens=500,
        )

        answer = response.choices[0].message.content
        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text(
            "⚠️ এখন একটু সমস্যা হচ্ছে। পরে আবার চেষ্টা করো।"
        )
        print(e)

# App start
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_reply))

app.run_polling()
