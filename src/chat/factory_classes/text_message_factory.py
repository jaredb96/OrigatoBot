from . import general_message_factory
from . message_classes import text_message


class TextMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        text_message_output = text_message.TextMessage()
        text_message_output.author = raw_message['sender_name']
        text_message_output.message_id = raw_message['timestamp_ms']
        text_message_output.text = \
            raw_message['content']
        text_message_output.reacts = self.build_reactions()
        return text_message_output
