from flask import *
from telegram.ext import Application
import Constants as keys

app = Application.builder().token(keys.API_KEY).build()
async def sendIt () :
  await app.bot.send_message(chat_id='-4030149233', text='Ayyyy')

class endpoint (object):
  apiEndpoint = Flask(__name__)

  @apiEndpoint.route('/sendMessage')
  async def sendMessage():
    await sendIt(app)
    response = 'sent'
    response.status_code = 200
    return response
    

  def start(apiEndpoint):
    apiEndpoint.run(debug=True)


if __name__ == "__main__":
  api = endpoint()
  api.start(apiEndpoint=api)