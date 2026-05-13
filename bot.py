from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import os

TOKEN = "8634917154:AAHO2mKfmUDkpK8IQ6gywPNPRXYdl4yCtHU"  # ЗАМЕНИТЕ НА ВАШ ТОКЕН

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🌿 Практика", callback_data="practice")],
        [InlineKeyboardButton("💬 Цитата", callback_data="quote")],
    ]
    await update.message.reply_text(
        "🧘 **Привет! Я SomaBot**\n\nВыбери:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    if query.data == "practice":
        await query.edit_message_text("🌬️ **Практика:**\n\nГлубокий вдох → задержка → выдох. Повтори 4 раза.", parse_mode="Markdown")
    else:
        await query.edit_message_text("✨ **Цитата:**\n\nТвоё тело — твой дом. Замечай его.", parse_mode="Markdown")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен...")
    app.run_polling()
