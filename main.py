from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import settings

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я твой персональный ассистент. 📝\n"
        "Скоро буду присылать тебе задачи и отслеживать их выполнение."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()
