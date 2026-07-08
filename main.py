from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
import os
import random

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

ideas = [
    "🎬 10 фактів, які зламають твоє уявлення про світ.",
    "😱 Найдивніші місця на Землі.",
    "💰 Як люди заробляють мільйони онлайн.",
    "👻 Містичні історії, які досі не пояснили.",
    "🚀 Технології майбутнього, які вже існують.",
    "🧠 Психологічні факти, які здивують.",
    "📱 Найкращі способи стати популярним у TikTok.",
    "🌍 Країни, де діють дивні закони.",
    "🤯 Оптичні ілюзії, які обманюють мозок.",
    "🔥 Ідея для вірусного Shorts прямо зараз."
]

names = [
    "IdeaStorm AI",
    "Viral Factory",
    "MindSpark",
    "Future Creator",
    "Content Machine",
    "Trend Hunter",
    "Creative Engine",
    "Next Viral",
    "Smart Creator",
    "Content Master"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Вітаю!\n\n"
        "Я IdeaBot AI.\n"
        "Допоможу створювати ідеї для YouTube, TikTok та Instagram.\n\n"
        "Обери дію нижче 👇",
        reply_markup=reply_markup
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💡 Генерувати ідею":
        await update.message.reply_text(random.choice(ideas))

    elif text == "📝 Генерувати назву":
        await update.message.reply_text(
            "📝 Варіанти назв:\n\n" +
            "\n".join(random.sample(names, 5))
        )

    elif text == "🏷️ Хештеги":
        await update.message.reply_text(
            "#youtube\n#shorts\n#tiktok\n#viral\n#ideas"
        )

    elif text == "⭐ PRO":
        await update.message.reply_text(
            "⭐ PRO скоро відкриється.\n\n"
            "Там будуть ШІ, сценарії та багато інших можливостей."
        )

    else:
        await update.message.reply_text(
            "Натисни одну з кнопок нижче 👇"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

print("Бот запущений...")

app.run_polling()
