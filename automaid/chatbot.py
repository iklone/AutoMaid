from chatterbot import ChatBot
import os
import shutil
import chatterbot_corpus
from google.cloud import translate

class MaidChatDriver(object):
    def __init__(self, storage_adapter):
        #Sets up chatterbot with name AMAI, a trainer, storage adapter and DB overwrite
        self.chatbot = ChatBot(
            'AMAI',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
            database = './AMAI.sqlite3'
        )
        #Trains AMAI on corpi. TODO Make optional and soften code
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

    def translateQuery(self, query):
        translateClient = translate.Client()

        query = u'Hello world'
        target = 'ja'

        translation = translateClient.translate(query, target_language=target)
        response = translation['translatedText']
        return response

    #Get response for text query
    #Runs through a master system simulated switch case with default being a chatterbot response
    #If utility functionality isn't working it's becasue of something here
    def getResponse(self, query):
        if "shutdown" in query:
            return "*shutdown"

        if query.startswith("Translate"):
            return self.translateQuery(query)

        #default- revert to chatterbot
        response = self.chatbot.get_response(query)
        return response
