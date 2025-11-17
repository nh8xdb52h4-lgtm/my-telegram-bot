import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен от BotFather
TOKEN = os.environ.get("TELEGRAM_TOKEN")
PORT = int(os.environ.get("PORT", 8000))

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(f'Привет, {user.first_name}! Я твой первый бот! Работаю в облаке! ✅')

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Я просто повторюша! Напиши что-нибудь)')

# Обработка обычных сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f'Ты сказал: {user_text}')

async def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Запускаем бота для облака
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    # Бесконечный цикл чтобы бот не останавливался
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
