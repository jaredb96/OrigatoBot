from . import general_message_factory
from . message_classes import picture_message


class PictureMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        picture_message_output = picture_message.PictureMessage()
        picture_message_output.author = raw_message['sender_name']
        picture_message_output.message_id = raw_message['timestamp_ms']
        picture_message_output.media_uri = \
            raw_message['photos'][0]['uri']
        if 'reactions' in raw_message:
            picture_message_output.reacts = self.build_reactions(raw_message['reactions'])
        return picture_message_output
