from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, send_multiple_message
from linebot.models import TemplateSendMessage, ButtonsTemplate, MessageAction
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from linebot import LineBotApi, WebhookParser


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose(self, event):
        text = event.message.text
        return text.lower() == "start"

    def on_enter_choose(self, event):
        buttons_template = ButtonsTemplate(
            title='Q1', text='你爲什麽要退選呢？', actions=[
               MessageAction(label='期中考考太爛', text='期中考考太爛'),
               MessageAction(label='作業太難寫了', text='作業太難寫了'),
               MessageAction(label='分組報告完全不會做', text='分組報告完全不會做'),
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_button_message(reply_token, template_message)


    def is_going_to_exam(self, event):
        text = event.message.text
        return text == "期中考考太爛"

    def on_enter_exam(self, event):
        buttons_template = ButtonsTemplate(
            title='Q1', text='其他人考得怎麽樣呢？', actions=[
               MessageAction(label='大家都一樣爛', text='大家都一樣爛'),
               MessageAction(label='只有我這麽爛', text='只有我這麽爛')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_button_message(reply_token, template_message)

    def is_going_to_homework(self, event):
        text = event.message.text
        return text == "作業太難寫了"

    def on_enter_homework(self, event):
        buttons_template = ButtonsTemplate(
            title='Q1', text='可不可以‘參考’別人的作業呢？', actions=[
               MessageAction(label='作業可以偷偷抄', text='作業可以偷偷抄'),
               MessageAction(label='助教抓抄襲超嚴格的', text='助教抓抄襲超嚴格的')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_button_message(reply_token, template_message)

    def is_going_to_project(self, event):
        text = event.message.text
        return text == "分組報告完全不會做"

    def on_enter_project(self, event):
        buttons_template = ButtonsTemplate(
            title='Q1', text='其他隊員怎麽樣呢？', actions=[
               MessageAction(label='全部和我一樣廢', text='全部和我一樣廢'),
               MessageAction(label='隊内有超神卷哥卷姐', text='隊内有超神卷哥卷姐')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_button_message(reply_token, template_message)

    def is_going_to_friend(self, event):
        text = event.message.text
        return text == "作業可以偷偷抄"

    def on_enter_friend(self, event):
        buttons_template = ButtonsTemplate(
            title='Q2', text='有沒有認識系上卷哥卷姐？', actions=[
               MessageAction(label='有', text='有'),
               MessageAction(label='沒有我超邊緣', text='沒有我超邊緣')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_button_message(reply_token, template_message)

    def is_going_to_teacher(self, event):
        text = event.message.text
        return text == "大家都一樣爛"

    def on_enter_teacher(self, event):
        buttons_template = ButtonsTemplate(
            title='Q2', text='該科教授看起來友善嗎？', actions=[
               MessageAction(label='超和藹可親的', text='超和藹可親的'),
               MessageAction(label='看起來就是大刀教授', text='看起來就是大刀教授')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_button_message(reply_token, template_message)

    def is_going_to_friend_find(self, event):
        text = event.message.text
        return (text == "沒有我超邊緣")

    def on_enter_friend_find(self, event):
        buttons_template = ButtonsTemplate(
            title='Q3', text='看完教程後，有信心和卷哥卷姐成爲朋友嗎嗎？', actions=[
               MessageAction(label='現在全系都是我朋友', text='現在全系都是我朋友'),
               MessageAction(label='不行我辦不到', text='不行我辦不到')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        reply_token = event.reply_token
        send_multiple_message(reply_token, [TextSendMessage("如何交朋友教程: https://zh.wikihow.com/%E4%BA%A4%E6%9C%8B%E5%8F%8B"),
                               template_message])

    def is_going_to_keep(self, event):
        text = event.message.text
        return (text == "有")|(text == "超和藹可親的")|(text == "現在全系都是我朋友")|(text == "隊内有超神卷哥卷姐")

    def on_enter_keep(self, event):
        reply_token = event.reply_token
        send_multiple_message(reply_token, [TextSendMessage("別退！教授和同學會拯救你的！"), 
                                            ImageSendMessage(original_content_url='https://stickershop.line-scdn.net/stickershop/v1/product/13127/LINEStorePC/main.png;compress=true',
                                                             preview_image_url='https://stickershop.line-scdn.net/stickershop/v1/product/13127/LINEStorePC/main.png;compress=true')])
        self.go_back()

    def is_going_to_drop(self, event):
        text = event.message.text
        return (text == "只有我這麽爛")|(text == "助教抓抄襲超嚴格的")|(text == "全部和我一樣廢")|(text == "看起來就是大刀教授")|(text == "不行我辦不到")

    def on_enter_drop(self, event):
        reply_token = event.reply_token
        send_multiple_message(reply_token, [TextSendMessage("快退吧！你沒救了！"), 
                                            ImageSendMessage(original_content_url='https://3.bp.blogspot.com/-2QLT7Uk6WnI/V77pnCrd0RI/AAAAAAAAHWc/qSgCr7BrJUERswcvL0tiAkihdNpsngkUACLcB/s1600/SnapShot%25280%25292.jpg', 
                                                             preview_image_url='https://3.bp.blogspot.com/-2QLT7Uk6WnI/V77pnCrd0RI/AAAAAAAAHWc/qSgCr7BrJUERswcvL0tiAkihdNpsngkUACLcB/s1600/SnapShot%25280%25292.jpg')])
        self.go_back()

    def on_exit_keep(self):
        print("Leaving keep")

    def on_exit_drop(self):
        print("Leaving drop")