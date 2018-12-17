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

    #POST
    def post(self):
        msg = json.loads(self.request.body)

        fb_message = msg.get('message', {})
        sender = msg.get('sender')
        if 'text' in fb_message:
            #text message
            query = fb_message['text']
            print(">" + sender + ":\t" + query)

            response = self.application.chatbot.get_response(query)
            print ">AMAI:\t" + str(response)

        elif 'attachments' in fb_message:
            #attachment message (image)
            print("Sender message is attachment")

        #send_message("access_token", "recipient_id", "text", False)

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
