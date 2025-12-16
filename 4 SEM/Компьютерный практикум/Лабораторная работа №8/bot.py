import telebot

# Укажите токен вашего бота
BOT_TOKEN = "7162174877:AAFsaxMgMxug8iKQa-LRLqrkx5eGJCPGz8c"

# Укажите URL вашей функции или сервера, где будет запущен бот
WEBHOOK_URL = "https://d5drhe2pc12do9puko1i.apigw.yandexcloud.net"

bot = telebot.TeleBot(BOT_TOKEN)

# Установка нового вебхука
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

print("Webhook успешно установлен!")
