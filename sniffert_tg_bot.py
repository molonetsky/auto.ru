import telebot
from Sniffer import main1
import time
from bot_token import bot_token


bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['text'])
def get_message(message2):
    if message2.text == 'Начать':
        upload_pars(message2)
    else:
        bot.send_message(message2.from_user.id, "Я тебя не понимаю. Напиши 'Начать'.")


@bot.message_handler(content_types=['text'])
def upload_pars(message):
    bot.send_message(message.from_user.id, 'Подождите 10 секунд, данные собираются с auto.ru')
    main1()
    time.sleep(10)
    # main2()
    bot.send_message(message.from_user.id, 'Вот автомобили в диапазоне 250-450 т.р. ')
    bot.send_document(message.chat.id, open(r'C:\Users\Администратор\PycharmProjects\sniffer_bot\pars_cars.txt', 'rb'))


bot.polling(none_stop=True, interval=0)
