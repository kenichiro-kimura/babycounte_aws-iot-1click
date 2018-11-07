# coding: utf-8
import json
from linebot import LineBotApi
from linebot.models import (TextSendMessage, FlexSendMessage, BubbleContainer, CarouselContainer,ImageComponent,BoxComponent,TextComponent)
from linebot.exceptions import LineBotApiError

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print json.dumps(body)
    return response

def sendmsg(event, context):
    s3url = ""
    groupId = ""
    line_token = ""
    
    deviceId = event['deviceInfo']['deviceId']
    clickType = event['deviceEvent']['buttonClicked']['clickType'];
    line_bot_api = LineBotApi(line_token)

    alttext = u"おしっこした！"
    cgfile = "";
    if(clickType == "LONG"):
        alttext = u"うんちした！"
        cgfile = ""
    if(clickType == "DOUBLE"):
        alttext = u"ミルク飲んだ！"
        cgfile = ""
        
    flex = BubbleContainer(
        hero=ImageComponent(
            size='full',
            url=s3url+cgfile,
        ),
        body=BoxComponent(
            layout='vertical',
            contents=[
                TextComponent(
                    text=alttext,
                    weight='bold',
                    size='lg'
                )
            ]
        ),
    )

    line_bot_api.push_message(
        groupId,
        FlexSendMessage(
            alt_text=alttext,
            contents=flex
        )
    )
    return
