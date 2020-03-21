from . import general_message_factory
from . message_classes import video_message


class VideoMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        video_message_output = video_message.VideoMessage()
        video_message_output.author = raw_message['sender_name']
        video_message_output.message_id = raw_message['timestamp_ms']
        video_message_output.media_uri = \
            raw_message['videos']['uri']
        video_message_output.reacts = self.build_reactions()
        return video_message_output
