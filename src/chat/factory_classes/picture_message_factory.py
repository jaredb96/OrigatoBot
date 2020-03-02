from . import general_message_factory
from . message_classes import picture_message


class PictureMessageFactory(general_message_factory.GeneralFactory):
    def build_message(self, raw_message):
        picture_message_output = picture_message.PictureMessage()
        picture_message_output.author = raw_message['sender_name']
        picture_message_output.message_id = raw_message['timestamp_ms']
        picture_message_output.media_uri = \
            raw_message['pictures']['uri']
        picture_message_output.reacts = self.build_reactions()
        return picture_message_output
