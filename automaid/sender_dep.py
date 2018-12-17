import subprocess

def send_message(access_token, recipient_id, text, passive=False):
    escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    args = [
        'curl',
        '-F',
        'recipient={"id":"%s"}' % recipient_id,
        '-F',
        'message={"text": "%s"}' % escaped_text
    ]
    if passive:
        args.append('-F')
        args.append('messaging_type=MESSAGE_TAG')
        args.append('-F')
        args.append('tag=NON_PROMOTIONAL_SUBSCRIPTION')
    else:
        args.append('-F')
        args.append('messaging_type=RESPONSE')
    args.append('localhost:1337/webhook')

    # Execute
    p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
    (output, err) = p.communicate()

    #['curl', '-F', 'recipient={"id":"recipient_id"}', '-F', 'message={"text": "text"}', '-F', 'messaging_type=RESPONSE', 'https://graph.facebook.com/v2.8/me/messages?access_token=access_token']


    print args
