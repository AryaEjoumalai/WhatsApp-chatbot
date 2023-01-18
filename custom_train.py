from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
trainer = ListTrainer(bot)


#modify the list to custom train chatbot

trainer.train([
    'Hi',
    'Hello',
    'I need roadmap for Competitive Programming',
    'Just create an account on GFG and start',
    'I have a query.',
    'Please elaborate, your concern',
    'How long it will take to become expert in Coding ?',
    'It usually depends on the amount of practice.',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])
