from chatterbot import ChatBot
import os
import shutil
import chatterbot_corpus

class MaidChatDriver(object):
    def __init__(self, storage_adapter):
        self.chatbot = ChatBot(
            'AMAI',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
            database = './AMAI.sqlite3'
        )
        self.chatbot.train(
            #"chatterbot.corpus.english.conversations",
            #"chatterbot.corpus.english.greetings",
            #"chatterbot.corpus.english.ai",
            #"chatterbot.corpus.english.humor",
            #"chatterbot.corpus.custom.maidcorpus",
            #"chatterbot.corpus.custom.maidcorpus",
            #"chatterbot.corpus.custom.maidcorpus"
        )
        print "AMAI initialised"

    def getResponse(self, query):
        if "shutdown" in query:
            return "*shutdown"

        #default- revert to chatterbot
        response = self.chatbot.get_response(query)
        return response
