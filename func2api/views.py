from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot.models import MessageEvent, TextMessage, PostbackEvent,LocationMessage
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func
import sys
sys.path.append("..")
import line_chat_bot_settings as s

line_bot_api = LineBotApi(s.channel_access_token)
parser  = WebhookParser(s.channel_secret)

#1.1修改LineBotApi中的內容修改成您的機器人Channel access token
#1.2修改WebhookParser中的內容修改成您的機器人Channel secret 

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@蘇菲29':
                        func.searchResult(event)
                    elif mtext == '@查看使用說明書':
                        func.sendInstructions(event)
                    elif mtext == '@填寫表單':
                        func.sendSticker(event)
                    elif mtext == '@前往線上購物網':
                        func.sendCarousel(event)
                    elif mtext == '@查詢附近實體店面':
                        func.sendGoogleMapCarousel(event)
                    elif mtext == '@圖片地圖':
                        func.sendImgmap(event)
                    elif mtext == '@定位':
                        func.quick_action(event)
                    elif mtext =='text':
                        func.sendButton(event)
                if isinstance(event.message, LocationMessage):       
                    # latitudedata = event.message.latitude
                    # longitudedata = event.message.longitude
                    func.Location_get(event)

    
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
