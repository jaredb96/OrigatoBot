from . import general_message_factory
from . message_classes import gif_message


class GifMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        gif_message_output = gif_message.GifMessage()
        gif_message_output.author = raw_message['sender_name']
        gif_message_output.message_id = raw_message['timestamp_ms']
        gif_message_output.media_uri = raw_message['gifs']['uri']
        gif_message_output.reacts = self.build_reactions()
        return gif_message_output




