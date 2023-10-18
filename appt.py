import os

from EasyTeleBot.TelegramBot import CreateEasyTelegramBot
my_token = '6675577249:AAGDkuPNMP-BONEM4GSx92LY80q2E9d8Sqk'
#test for payment luchiycinema.pro
#email apapap2000@decoymail.mx
easy_bot = CreateEasyTelegramBot('config.json', telegram_token=my_token)

app = easy_bot.flask_app

if __name__ == '__main__':
    print('main function started')
    app.run()
