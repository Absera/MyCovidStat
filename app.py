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

    if text == '/start':
        welcome = '''
W E L C O M E !
/world - for global statistics
/top10 - for top 10 infected countries
/about - info about the bot

        '''
        about = '''
Commands!
/world - for global statistics
/top10 - for top 10 infected countries
/about - info about the bot


developer: @AbseraTemesgen
        '''
        bot.sendMessage(chat_id=chat_id, text=welcome)
    elif text in [ 'world', 'World', '/world', '/World']:
        response = get_world_stat(text)
        bot.sendMessage(chat_id=chat_id, text=response)
    elif text in ['top10', 'Top10', 'top 10', 'Top 10', '/top10', '/Top10']:
        response = get_top10_stat(text)
        bot.sendMessage(chat_id=chat_id, text=response)
    elif text in ['/about', 'about']:
       
        bot.sendMessage(chat_id=chat_id, text=about)
    else:
        response = 'Available messages are:\n /world\n /top10'
        bot.sendMessage(chat_id=chat_id, text=response)

    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "[WEBHOOK] - RUNNING WELL!"
    else:
        return "[WEBHOOK] - NOT RUNNING WELL!"

@app.route('/')
def index():
    return '[APP] - RUNNING WELL!'


if __name__ == '__main__':
    app.run(threaded=True)
