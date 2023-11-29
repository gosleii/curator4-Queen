import telebot
bot = telebot.TeleBot("6729248157:AAHOD4jqLsmYQHsEzBQiaa02tgwWsh1X6nc")

@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, 'Пррривет :3')

@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat .id , 'Я бы с раостью помог, но у меня лапки')

@bot.message_handler(commands=['heal'])

def main(message):
    bot.send_message(message.chat.id, '*Мрр мрр мрр*', parse_mode = ' Markdown ')

bot.infinity_polling(none_stop=True)
