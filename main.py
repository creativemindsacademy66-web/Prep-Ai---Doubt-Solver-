from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.getenv("8478711385:AAEiVIwb9d0HhSOGyE746pzCmf9Z9qrxakQ")

def reply(update, context):
    update.message.reply_text(
        "🤖 আমি DoubtSource AI!\nতোমার প্রশ্ন লেখো 😊"
    )

updater = Updater(TOKEN)
updater.dispatcher.add_handler(
    MessageHandler(Filters.text, reply)
)

updater.start_polling()
updater.idle()
