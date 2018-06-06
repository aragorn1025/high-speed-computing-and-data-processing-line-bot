from flask import Flask, request, abort

from linebot import (
        LineBotApi, WebhookHandler
)
from linebot.exceptions import (
        InvalidSignatureError
)
from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage,
)

import sys
sys.path.append('./src')
import app_response

app = Flask(__name__)

line_bot_api = LineBotApi('mO+JYSCaxiBiAyNaC94A9SWC6Y8eCoGcIcAE0U0NxJNalilZTx/3bKgm3YH/Na5TMTITULf16XwxwerOwcWuGD59NDYVOhRXgVRZDAcrvcS0VldSesluOeiGe81/5NkQj2jWZQuokyb/rKOQgSL2SgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0f86ba3e4a5c50d0aecfd58d18b36195')

@app.route('/callback', methods = ['POST'])
def callback():
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text = True)
        app.logger.info('Request body: ' + body)
        try:
	        handler.handle(body, signature)
        except InvalidSignatureError:
    	        abort(400)
        return 'OK'

@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
        line_bot_api.reply_message(
	        event.reply_token,
                TextSendMessage(text = app_response.output(event.message.text + ' ' + event.source.userId))
        )

if __name__ == '__main__':
        app.run()
