import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_message(reply_token, template_message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, template_message)

    return "OK"

def send_multiple_message(reply_token, message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, img_url)

    return "OK"



