from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

