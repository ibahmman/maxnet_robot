from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

api_url = 'http://127.0.0.1:8000/api/v2/product/v2r/'

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get(api_url).json()
    print(response)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6392235672:AAElUj6EbqrPBWGdDDdhfBEvoe7SJFe1maA").build()

app.add_handler(CommandHandler("products", products))

app.run_polling()