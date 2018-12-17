from chatterbot import ChatBot

class MaidChatDriver(object):
    def __init__(self, storage_adapter):
        self.chatbot = ChatBot(
            'AMAI',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
            database = './AMAI.sqlite3'
        )
        print "AMAI initialised"

    def get_response(self, query):
        response = self.chatbot.get_response(query)
        return response
