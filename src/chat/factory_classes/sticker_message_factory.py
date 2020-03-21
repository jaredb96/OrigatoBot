from . import general_message_factory
from . message_classes import sticker_message


class StickerMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        sticker_message_output = sticker_message.StickerMessage()
        sticker_message_output.author = raw_message['sender_name']
        sticker_message_output.message_id = raw_message['timestamp_ms']
        sticker_message_output.media_uri = \
            raw_message['sticker']['uri']
        sticker_message_output.reacts = self.build_reactions()
        return sticker_message_output
