import os
import asyncio
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# ========== НАСТРОЙКИ ==========
TOKEN = "8634917154:AAHO2mKfmUDkpK8IQ6gywPNPRXYdl4yCtHU"  # ← ВСТАВЬТЕ ВАШ ТОКЕН
# ================================

# Flask-приложение для Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Soma Bot is running!"

@flask_app.route('/health')
def health():
    return "OK"

# ========== ТЕЛЕГРАМ БОТ ==========
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🌿 Практика", callback_data="practice")],
        [InlineKeyboardButton("💬 Цитата", callback_data="quote")],
    ]
    await update.message.reply_text(
        "🧘 **Привет! Я SomaBot**\n\nВыбери, что хочешь получить:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == "practice":
        await query.edit_message_text(
            "🌬️ **Практика:**\n\nСделай глубокий вдох на 4 счёта, задержи дыхание на 7, выдохни на 8.\nПовтори 4 раза.",
            parse_mode="Markdown"
        )
    else:
        await query.edit_message_text(
            "✨ **Цитата:**\n\nТвоё тело — это дом, в котором ты живёшь. Замечай его сегодня.",
            parse_mode="Markdown"
        )

def run_telegram():
    """Запускает Telegram-бота в отдельном потоке"""
    telegram_app = Application.builder().token(TOKEN).build()
    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Telegram-бот запущен...")
    telegram_app.run_polling(allowed_updates=["message", "callback_query"])

# ========== ЗАПУСК ==========
if __name__ == "__main__":
    # Запускаем Telegram-бота в фоновом потоке
    bot_thread = Thread(target=run_telegram)
    bot_thread.start()
    
    # Запускаем Flask-сервер (основной поток)
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)
