import json
import sys
import tornado.ioloop
import tornado.web

from config import ACCESS_TOKEN, VERIFY_TOKEN, STORAGE_ADAPTER
from chatbot import MaidChatDriver
from sender import send_message

class WebhookDriver(tornado.web.RequestHandler):
    print("Webhook Driver Booted")

    #GET
    def get(self):
        args = self.request.arguments
        if args.get('hub.mode', [''])[0] == 'subscribe' and args.get('hub.verify_token', [''])[0] == VERIFY_TOKEN:
            print("Verify Token Accepted")
            return
        print("Verify Token NOT Accepted, tried " + args.get('hub.verify_token', [''])[0])
        self.set_status(403)
        return

    def options(self):
        self.set_status(200)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST")
        self.set_header("Access-Control-Allow-Headers", "*")
        return

    #POST
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        msg = json.loads(self.request.body)

        fb_message = msg.get('message', {})
        sender = msg.get('sender')
        if 'text' in fb_message:
            #text message
            query = fb_message['text']
            print(">" + sender + ":\t" + query)

            response = str(self.application.chatbot.getResponse(query) )
            print ">AMAI:\t" + response + "\n"

        elif 'attachments' in fb_message:
            #attachment message (image)
            print("Sender message is attachment")

        if response.startswith("*"):
            if response == "*shutdown":
                response = "Goodbye, master"
                shutdown()

        self.write(response)

def shutdown():
    tornado.ioloop.IOLoop.current().stop()

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
