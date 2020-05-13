from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
from telebot.main_source import get_world_stat, get_top10_stat


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)
    if text == '/start':
        welcome = '''
W E L C O M E !
Are you looking for Covid19 statistics?
If your answer is yes, You are in the right place!

send 'world' for global statistics
send 'top10' for top 10 infected countries


share the bot @myCovidStatbot
developed by @AbseraTemesgen 

        '''
        bot.sendMessage(chat_id=chat_id, text=welcome)
    elif text == 'world':
        response = get_world_stat(text)
        bot.sendMessage(chat_id=chat_id, text=response)
    elif text == 'top10':
        response = get_top10_stat(text)
        bot.sendMessage(chat_id=chat_id, text=response)

    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
####

@bot.message_handler(commands=['menu'])
def menu(m):

  cid = m.chat.id

  menuKeyboard = types.InlineKeyboardMarkup()
  menuKeyboard.add(types.InlineKeyboardButton('Button1', callback_data='button1'),
           types.InlineKeyboardButton('Button2', callback_data='button2'))

  bot.send_message(cid, "Menu", reply_markup=menuKeyboard)
####

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
