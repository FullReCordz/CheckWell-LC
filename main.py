import telebot

API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use /help to see available commands.")

@bot.message_handler(commands=['scan'])
def scan_command(message):
    bot.reply_to(message, "Scan command executed.")

@bot.message_handler(commands=['phish'])
def phish_command(message):
    bot.reply_to(message, "Phishing command executed.")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = "Available commands: /start, /scan, /phish, /help, /about"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['about'])
def about_command(message):
    bot.reply_to(message, "This bot was created to help with your tasks!")

if __name__ == '__main__':
    bot.polling()