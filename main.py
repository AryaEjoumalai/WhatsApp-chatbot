
''' Ask the sender to use prefix 0 for chatting with bot. example: 0hi'''


from chatterbot import ChatBot
from alright import WhatsApp
bot = ChatBot('Bot')
messenger = WhatsApp()


while True:
    # Enter the contact's number or name or group's name in palace of 91871xxxxxxx
    request=str(messenger.get_last_message_received(query="91871xxxxxxx"))
    
    if request[0]=='0':
        
        response=bot.get_response(request)
        r=str(response)
        messenger.send_message(r)
    
     
