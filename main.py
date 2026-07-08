from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    ["💡 Генерувати ідею"],
    ["📝 Генерувати назву"],
    ["🏷️ Хештеги"],
    ["⭐ PRO"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Вітаю!\n\n"
        "Я IdeaBot AI.\n"
        "Допоможу створювати ідеї для YouTube, TikTok та Instagram.\n\n"
        "Обери дію нижче 👇",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущений...")

app.run_polling()
