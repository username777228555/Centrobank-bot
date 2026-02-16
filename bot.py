import os
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Получаем токен из переменной окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Не найдена переменная окружения BOT_TOKEN! Добавьте её в настройках Render.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик всех текстовых сообщений"""
    
    # Генерируем случайное количество "ы" и "ф"
    y_count = random.randint(50, 200)  # количество "ы"
    f_count = random.randint(100, 300)  # количество "ф"
    
    # Создаем разные варианты ответа
    variants = [
        "ы" * y_count + "ф" * f_count,
        "ы" * random.randint(30, 100) + "ф" * random.randint(80, 250) + "ы" * random.randint(20, 80),
        ("ы" * random.randint(5, 15) + "ф" * random.randint(10, 25)) * random.randint(5, 12),
        "ф" * random.randint(50, 150) + "ы" * random.randint(100, 250) + "ф" * random.randint(50, 150),
        "".join(random.choice(["ы", "ф"]) * random.randint(3, 10) for _ in range(random.randint(15, 35))),
    ]
    
    # Выбираем случайный вариант
    response = random.choice(variants)
    
    # Отправляем ответ
    await update.message.reply_text(response)

def main():
    """Запуск бота"""
    print("Запуск бота...")
    print(f"Токен найден: {BOT_TOKEN[:10]}...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчик для всех текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    print("Бот успешно запущен и работает!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
