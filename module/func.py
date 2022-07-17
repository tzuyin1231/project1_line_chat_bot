from . import dbsettings as dbs
import pymysql
from linebot import LineBotApi
from linebot.models import *

from linebot.models import TextSendMessage, AudioSendMessage, ImageSendMessage, LocationSendMessage, StickerSendMessage
from linebot.models import MessageEvent, TextMessage, PostbackEvent,LocationMessage
from linebot.models import TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
import sys
sys.path.append("..")
import line_chat_bot_settings as s
sys.path.append("..")
import other_settings as s2

line_bot_api = LineBotApi(s.channel_access_token)#機器人Channel access token
baseurl = 'https://'+s2.ngrok_without_https+'static/'
#baseurl = 'https://0a0438bf.ngrok.io/static/' 
#把以上的https://0a0438bf.ngrok.io改成您執行ngrok轉執服務後得到的轉址連結ex:-->   https://0a0438bf.ngrok.io

def sendInstructions(event):  #@查看使用說明書
    text="""感謝使用本服務。
欲查詢商品請於對話框打上
@商品名稱
'商品名稱'換成欲查詢的商品

或前往本服務官網查看詳細比價結果

比價結果僅供參考，實際價格以各網站為準"""
    try:
        message = TextSendMessage(text)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def Location_get(event):  #@查詢附近實體店面
    try:
        latitudevalue = event.message.latitude  #取得經度
        longitudevalue = event.message.longitude #取得緯度        
        #image_url = 'https://i.imgur.com/Q0cGcyx.png'  #圖片位址
        #image_url = 'https://i.imgur.com/Q3ypVTr.jpg'
        image_url = 'https://i.imgur.com/cResobO.jpg'
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 300
        message = [
            TextSendMessage("請點選欲查詢的店面"),
            ImagemapSendMessage(
            base_url=image_url,
            alt_text="選擇搜尋之店面",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                URIImagemapAction(  #開啟網頁
                    link_uri='https://www.google.com.tw/maps/search/'+'屈臣氏'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=0, 
                        y=0, 
                        width=imgwidth*0.2, 
                        height=imgheight  
                    )
                ),                
                URIImagemapAction(  #開啟網頁
                    link_uri='https://www.google.com.tw/maps/search/'+'康是美'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.2, 
                        y=0, 
                        width=imgwidth*0.2, 
                        height=imgheight  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='https://www.google.com.tw/maps/search/'+'寶雅'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.4, 
                        y=0, 
                        width=imgwidth*0.2, 
                        height=imgheight  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='https://www.google.com.tw/maps/search/'+'家樂福'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.6, 
                        y=0, 
                        width=imgwidth*0.2, 
                        height=imgheight  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='https://www.google.com.tw/maps/search/'+'全聯'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.8, 
                        y=0, 
                        width=imgwidth*0.2, 
                        height=imgheight  
                    )
                ),
            ]
        )]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def quick_action(event):   
    line_bot_api.reply_message(
							event.reply_token,
						TextSendMessage(
							text='請點擊下方以開啟定位服務',
							quick_reply=QuickReply(
							items=[
                            # return a location message
                            QuickReplyButton(
                                action=LocationAction(label="位置資訊")
                        ),
                    ])))

#沒使用
def Location_get1(event):  #@查詢附近實體店面
    try:
        latitudevalue = event.message.latitude  #取得經度
        longitudevalue = event.message.longitude #取得緯度
        message = TemplateSendMessage(
            alt_text='點擊連結，前往購物網',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/5BpVCwQ.jpg',
                        title='點擊下方連結，查詢附近店面',
                        text='第一頁，更多選擇請往右滑',
                        actions=[
                            URITemplateAction(
                                label='watsons屈臣氏',
                                uri='https://www.google.com.tw/maps/search/'+'屈臣氏'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1'
                            ),
                            URITemplateAction(
                                label='cosmed康是美',
                                uri='https://www.google.com.tw/maps/search/'+'康是美'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1'
                            ),
                            URITemplateAction(
                                label='poya寶雅',
                                uri='https://www.google.com.tw/maps/search/'+'寶雅'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/5BpVCwQ.jpg',
						#thumbnail_image_url=baseurl +'momo.jpg'https://i.imgur.com/92DJOwt.jpg,
                        title='點擊下方連結，查詢附近店面',
                        text='第一頁，更多選擇請往右滑',
                        actions=[
                            URITemplateAction(
                                label='carrefour家樂福',
                                uri='https://www.google.com.tw/maps/search/'+'家樂福'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1'
                            ),
                            URITemplateAction(
                                label='全聯',
                                uri='https://www.google.com.tw/maps/search/'+'全聯'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1'
                            ),
                            URITemplateAction(
                                label='tomod\'s',
                                uri='https://www.google.com.tw/maps/search/'+'tomod\'s'+'/@{},{}'.format(latitudevalue,longitudevalue)+',15z/data=!3m1!4b1'
                            ),
                            
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！{}'.format(e)))

def searchResult(event):#傳送sql結果
    try:
    # Connect to the database
        db = pymysql.connect(host=dbs.host,
                        user=dbs.user,
                        password=dbs.password,
                        database=dbs.database)
        #建立操作游標
        cursor = db.cursor()
        sql = """
        select market_name,goods_price,goods_num,unit_price 
        from goods_pricing_sofy_pad_29 
        ORDER BY goods_price,unit_price ;
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        
        sql = """
        select market_name, unit_price
        from goods_pricing_sofy_pad_29 
        ORDER BY unit_price ;
        """
        cursor.execute(sql)
        data_min = cursor.fetchone()
    
        text=""

        for i in data:
            text+="""{}：價格{} (共{}片)，每片{}元\n\n""".format(i[0],i[1],i[2],i[3])
        text+='目前單價最低為{}，每片{}元\n\n'.format(data_min[0],data_min[1])
        text+='或前往官網查看詳細內容:\n'+s2.ngrok_without_https+'/sofy'
        message = TextSendMessage(text)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        db.rollback()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！{}'.format(e)))
    cursor.close()
    db.close()

def sendCarousel(event):  #轉盤樣板，前往線上購物網
    try:
        message = TemplateSendMessage(
            alt_text='點擊連結，前往購物網',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        #thumbnail_image_url='https://i.imgur.com/5BpVCwQ.jpg',
						#thumbnail_image_url=baseurl +'momo.jpg'https://i.imgur.com/92DJOwt.jpg,
                        title='點擊下方連結，前往購物',
                        text='第一頁，更多選擇請往右滑',
                        actions=[
                            URITemplateAction(
                                label='MOMO購物網',
                                uri='https://m.momoshop.com.tw/main.momo'
                            ),
                            URITemplateAction(
                                label='pchome',
                                uri='https://www.pchome.com.tw/'
                            ),
                            URITemplateAction(
                                label='yahoo購物中心',
                                uri='https://tw.buy.yahoo.com'
                            ),

                        ]
                    ),
                    CarouselColumn(
                        #thumbnail_image_url='https://i.imgur.com/7kicILj.jpg',
                        title='點擊下方連結，前往購物',
                        text='第二頁，更多選擇請往右滑',
                        actions=[
                            URITemplateAction(
                            label='cosmed康是美網購',
                            uri='https://shop.cosmed.com.tw/'
                            ),
                            URITemplateAction(
                            label='屈臣氏線上購物',
                            uri='https://www.watsons.com.tw/'
                            ),
                            URITemplateAction(
                            label='寶雅線上買',
                            uri='https://www.poyabuy.com.tw/'
                            ),

                        ]
                    ),
					CarouselColumn(
                        #thumbnail_image_url='https://i.imgur.com/8HpZ4Fc.jpg',
                        title='點擊下方連結，前往購物',
                        text='最後一頁',
                        actions=[
                            URITemplateAction(
                            label='carrefour家樂福線上購',
                            uri='https://www.carrefour.com.tw'
                            ),
                            URITemplateAction(
                            label='誠品線上',
                            uri='https://www.eslite.com'
                            ),
                            URITemplateAction(
                            label='博客來',
                            uri='https://www.books.com.tw'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImgCarousel(event):  
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/fHVFvpr.jpg',
                        action=URITemplateAction(
                            label='前往MOMO購物網',
                            uri='https://m.momoshop.com.tw/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/nrgUqYN.jpg',
                        action=URITemplateAction(
                            label='前往pchome',
                            uri='https://www.pchome.com.tw/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/zxlJaXr.png',
                        action=URITemplateAction(
                            label='前往yahoo購物中心',
                            uri='https://tw.buy.yahoo.com'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/BSwaudu.jpg',
                        action=URITemplateAction(
                            label='前往屈臣氏線上購物',
                            uri='https://www.watsons.com.tw/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/9m0KE97.png',
                        action=URITemplateAction(
                            label='前往寶雅線上買',
                            uri='https://www.poyabuy.com.tw/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/xinl75s.png',
                        action=URITemplateAction(
                            label='前往康是美網購',
                            uri='https://shop.cosmed.com.tw/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/tiQ9bvi.jpg',
                        action=URITemplateAction(
                            label='前往家樂福線上購',#label字不能過長
                            uri='https://www.carrefour.com.tw'
                        )
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
"""
                    
                    
                    """
#未使用
def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
			    #thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
                #thumbnail_image_url=baseurl +'ology.png',

                title='按鈕樣版示範',  #主標題
                text='請選擇：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='文字訊息',
                        text='@購買飲料'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='文字訊息',
                        text='@購買飲料'
                    ),
                    MessageTemplateAction(  #顯示文字計息
                        label='文字訊息',
                        text='@購買飲料'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='連結網頁',
                        uri='https://www.lccnet.com.tw/commercial/career/33/transfer_gad.asp?med=g003&mpo=37898&gclid=CjwKCAiAi4fwBRBxEiwAEO8_HmclU4DPBg-ZA7GDKANGam5pVjMpzsZXWedFK5SYSdpAtM974-9WghoCFf8QAvD_BwE'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
