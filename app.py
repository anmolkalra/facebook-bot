import os,sys
from flask import Flask,request
from utils import wit_response

from pymessenger import Bot
app=Flask(__name__)
PAGE_ACCESS_TOKEN="enter your acess tokken"
bot=Bot(PAGE_ACCESS_TOKEN)
@app.route('/',methods=['GET'])

def index():
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "token not found",403
        return request.args["hub.challenge"],200
    return "hi everyone",200
@app.route('/',methods=['POST'])
def webhook():
    data=request.get_json()
    log(data)
    if data['object']=='page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id=messaging_event['sender']['id']
                recipient_id=messaging_event['recipient']['id']
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text=messaging_event['message']['text']
                    else:
                        messaging_text='no text'
                    response=None
                    entity,value=wit_response(messaging_text)
                    if (entity=='courses' and value=='course'):
                        response='you can visit this links'+'https://www.chitkara.edu.in/admissions/'
                    elif entity=="location":
                        response="ok"
                    elif (entity=='courses' and value=='engineering'):
                        response='you can visit this link'+'https://www.chitkara.edu.in/engineering'
                    elif (entity=='courses' and  value=='computer'):
                        response='BCA,MCA,B.E in computer science and engineering'
                    elif (entity=='courses' and value=='computer science' or value=='cse'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/engineering/computer-science-engineering/'
                    elif (entity=='courses' and value=='mechanical'):
                        response='you can visit this link'+'https://www.chitkara.edu.in/engineering/mechanical-engineering/'
                    elif (entity=='courses' and value=='electrical'):
                        response='you can visit this link'+ 'https://www.chitkara.edu.in/engineering/electronics-communication-engineering'
                    elif (entity=='courses' and value=='civil'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/engineering/civil-engineering/'
                    elif(entity=='courses' and value=='management' or value=='mba'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/cbs'
                    elif(entity=='courses' and value=='pharmacy'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/pharmacy'
                    elif (entity=='courses' and value=='art and design' or value=='arts'):
                        response='you can visit this link'+ 'https://www.chitkara.edu.in/arts/'
                    elif (entity=='courses' and value =='optometry' or value=='health sciences' or value=='nursing'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/healthscience'
                        
                    elif (entity=='courses' and value=='hotel management'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/hospitality'
                    elif (entity=='courses' and value=='architecture'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/architecture'
                    elif (entity=='courses' and value=='mass comm' or value=='journalism'):
                        resposne='you can visit this link' + 'https://www.chitkara.edu.in/chitkara-school-of-mass-communication/'
                    elif (entity=='courses' and value=='IT' or value=='BCA' or value=='MCA'):
                        response='you can visit this link' + 'https://www.chitkara.edu.in/engineering'
                    elif (entity=='fees' and value=='fee' or value=='fee sturcture'):
                        response='you can visit this link'+'https://www.chitkara.edu.in/admissions/fees-structure/'
                    elif (entity=='contact' and value=='contact'):
                        response='you acn visit this link' + 'https://www.chitkara.edu.in/contact-information/punjab'
                    elif (entity=='chitkara' and value=='chitkara'):
                        response='you can visit this link ' + 'https://www.chitkara.edu.in/'
                    elif(entity=='start'):
                        response='Hey ! How can i help you'
                    if response==None:
                        response="sorry i did not understand"
                    bot.send_text_message(sender_id,response)
                    

    return "ok",200
def log(response):
    print(response)
    sys.stdout.flush()
if __name__=="__main__":
    app.run(debug=True,port=80)
        
