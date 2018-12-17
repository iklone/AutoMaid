from chatterbot import ChatBot

class MaidChatDriver(object):
    def __init__(self, storage_adapter):
        self.chatbot = ChatBot(
            'AMAI',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
            database = './AMAI.sqlite3'
        )
        '''
        self.chatbot.train(
            "chatterbot.corpus.english.conversations",
            "chatterbot.corpus.english.greetings"
        '''
        print "AMAI initialised"

    def get_response(self, query):
        response = self.chatbot.get_response(query)
        return response
