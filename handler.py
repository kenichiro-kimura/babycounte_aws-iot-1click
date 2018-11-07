# coding: utf-8
import json
from datetime import datetime
import pytz
import ConfigParser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from linebot import LineBotApi
from linebot.models import (TextSendMessage, FlexSendMessage, BubbleContainer, CarouselContainer,ImageComponent,BoxComponent,TextComponent)
from linebot.exceptions import LineBotApiError

inifile = ConfigParser.SafeConfigParser()
inifile.read("./config.ini")

def hello(event, context):
    #LINE botのコールバック。取りあえずイベントを全部CloudWatch Logsに出すので
    #ここからgroupIdやroomIdを取得してconfigに反映する(手抜き)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    print json.dumps(body)
    return response

def sendmsg(event, context):
    #各種設定読み込み
    s3url = inifile.get('s3','url')
    groupId = inifile.get('line','targetId')
    line_token = inifile.get('line','token')
    credential_file = inifile.get('google','credential_file')
    scope = inifile.get('google','scope')
    sheet_key = inifile.get('google','sheet_key')
    sheet = inifile.get('google','sheet')
    babyname = inifile.get('general','babyname')
    
    #googleスプレッドシートへの接続
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scope)
    client = gspread.authorize(credentials)
    sp = client.open_by_key(sheet_key)
    wks = sp.worksheet(sheet)

    #LINE APIオブジェクト作成
    line_bot_api = LineBotApi(line_token)

    #イベント取得してメッセージを作成
    deviceId = event['deviceInfo']['deviceId']
    clickType = event['deviceEvent']['buttonClicked']['clickType']
    
    alttext = u"おしっこした！"
    eventtext = u"おしっこ"
    cgfile = inifile.get('s3','shortcg');
    if(clickType == "DOUBLE"):
        alttext = u"うんちした！"
        eventtext = u"うんち"
        cgfile = inifile.get('s3','doublecg');
    if(clickType == "LONG"):
        alttext = u"ミルク飲んだ！"
        eventtext = u"ミルク"
        cgfile = inifile.get('s3','longcg');

    print s3url+cgfile
    
    flex = BubbleContainer(
        hero=ImageComponent(
            size='full',
            url=s3url+cgfile,
        ),
        body=BoxComponent(
            layout='vertical',
            contents=[
                TextComponent(
                    text=babyname+alttext,
                    weight='bold',
                    size='lg'
                )
            ]
        ),
    )

    #googleスプレッドシートへ追加
    column = [eventtext,datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")]
    wks.append_row(column)

    #|LINEにプッシュメッセージを送る
    line_bot_api.push_message(
        groupId,
        FlexSendMessage(
            alt_text=babyname+alttext,
            contents=flex
        )
    )
    return
