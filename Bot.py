import telebot

# Replace with your bot token from BotFather
TOKEN = "7911428566:AA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I can solve math problems. Send me a question!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# Start the bot
bot.polling()
