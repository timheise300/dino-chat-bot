# -*- coding: UTF-8 -*-

import responseutils as response
from fbchat import log, Client
from fbchat.models import *

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            response_text = get_message(message_object.text.lower())
            response = Message(response_text)
            self.send(response, thread_id=thread_id, thread_type=thread_type)

def get_message(message):
    if "!hatch" in message:
        return response.hatch_dino(message)
    elif "!color" in message:
        return response.randomize_color()

client = EchoBot("tweekwilledchatbot@gmail.com", "Sunk!st3")
client.listen()