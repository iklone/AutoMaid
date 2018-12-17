#Facebook Token
ACCESS_TOKEN = "EAAEKFyAMe2wBAPT5rCPWZAKapbTUdUmpFBQZCpBCKkyxPZBt2kSef3266FbBdLZAN4ops5H2IYsvJgAXVhCYeyWbjDjTtwhPJ5Rr0Ggwfp2n8sBMRzHDivufmlo5EwY11Cdz7ZCfmIIllGJhDyvQtET3qI9ZBDh86xDKK0UJXtfAZDZD"
VERIFY_TOKEN = "maid"
STORAGE_ADAPTER = "chatterbot.storage.JsonFileStorageAdapter"

#prints FB tokens
def getFBTokens():
    print("Access Token = " + ACCESS_TOKEN)
    print("Verify Token = " + VERIFY_TOKEN)

#curl -X GET "localhost:1337/webhook?hub.verify_token=maid&hub.challenge=CHALLENGE_ACCEPTED&hub.mode=subscribe"
#curl -H "Content-Type: application/json" -X POST "localhost:1337/webhook" -d '{"sender": "James", "message": {"text": "MESSAGE"}}'
