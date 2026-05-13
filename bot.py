from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# ВСТАВЬТЕ ВАШ ТОКЕН СЮДА
TOKEN = "8634917154:AAHO2mKfmUDkpK8IQ6gywPNPRXYdl4yCtHU"

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
            "🌬️ **Практика:**\n\nСделай глубокий вдох на 4 счёта,\n"
            "задержи дыхание на 7,\nвыдохни на 8.\n\nПовтори 4 раза.",
            parse_mode="Markdown"
        )
    else:
        await query.edit_message_text(
            "✨ **Цитата:**\n\nТвоё тело — это дом, в котором ты живёшь.\n"
            "Замечай его сегодня.",
            parse_mode="Markdown"
        )

if __name__ == "__main__":
    print("Бот запускается...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот успешно запущен!")
    app.run_polling()
