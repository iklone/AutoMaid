import json
import sys
import lib/tornado.ioloop
import lib/tornado.web

from config import ACCESS_TOKEN, VERIFY_TOKEN

class WebhookDriver(tornado.web.RequestHandler):
    print("Webhook Driver Booted")

    #GET - incoming
    def get(self):
        args = self.request.arguments
        if args.get('hub.mode', [''])[0] == 'subscribe' and \
        args.get('hub.verify_token', [''])[0] == VERIFY_TOKEN:
            print("Verify Token Accepted")
            return
        print("Verify Token NOT Accepted, tried " + args.get('hub.verify_token', [''])[0])
        self.set_status(403)
        return

    #POST - outgoing
    def post(self):
        body = json.loads(self.request.body)
        for event in body.get('entry', []):
            messaging = event['messaging']
            for msg in messaging:
                fb_message = msg.get('message', {})
                print(fb_message)
                #recipient_id = msg['sender']['id']
                #print("Sender ID = " + recipient_id)
                if 'text' in fb_message:
                    #text message
                    query = fb_message['text']
                    print("Sender message = " + query)
                elif 'attachments' in fb_message:
                    #attachment message (image)
                    print("Sender message is attachment")
        print("Completed")

def main():
    #tornado
    application = tornado.web.Application([(
        r"/webhook", WebhookDriver),
    ])

    #start listening
    application.listen(1337)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
