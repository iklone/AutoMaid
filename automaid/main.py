import json
import sys
import tornado.ioloop
import tornado.web

from config import ACCESS_TOKEN, VERIFY_TOKEN, STORAGE_ADAPTER
from chatbot import MaidChatDriver
from sender import send_message

class WebhookDriver(tornado.web.RequestHandler):
    print("Webhook Driver Booted")

    #GET request - Used by messenger API
    def get(self):
        args = self.request.arguments
        if args.get('hub.mode', [''])[0] == 'subscribe' and args.get('hub.verify_token', [''])[0] == VERIFY_TOKEN:
            print("Verify Token Accepted")
            return
        print("Verify Token NOT Accepted, tried " + args.get('hub.verify_token', [''])[0])
        self.set_status(403)
        return

    #OPTIONS request - Verifies connection in accordance to HTTP
    def options(self):
        self.set_status(200)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST")
        self.set_header("Access-Control-Allow-Headers", "*")
        return

    #POST request - Main conversing function
    #User POSTs json containing username (sender) and message (message {text}), other fields are ignored
    #Example json: {"sender": "iklone", "message": {"text": "Hello"}}
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        msg = json.loads(self.request.body)

        message = msg.get('message', {})
        sender = msg.get('sender')
        if 'text' in message: #Checks message contains text
            query = message['text']
            print(">" + sender + ":\t" + query)

            response = self.application.chatbot.getResponse(query).decode("utf-8")
            print ">AMAI:\t" + response + "\n"

        elif 'attachments' in message: #Checks if message contains an attachment TODO
            print("Sender message is attachment")

        if response.startswith("*"):
            if response == "*shutdown":
                response = "Goodbye, master"
                shutdown()

        self.write(response)

#Quit process, the sole exit point: otherwise endless
def shutdown():
    tornado.ioloop.IOLoop.current().stop()

#Setup for webhook, chatterbot and maid object
def main():
    #tornado
    application = tornado.web.Application([(
        r"/webhook", WebhookDriver),
    ])

    application.chatbot = MaidChatDriver(STORAGE_ADAPTER)

    #start listening
    application.listen(1337)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
