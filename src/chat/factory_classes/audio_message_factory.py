from . import general_message_factory
from . message_classes import audio_message
from . message_classes import react_builder


class AudioMessageMessageFactory(general_message_factory.GeneralMessageFactory):
    def build_message(self, raw_message):
        audio_message_output = audio_message.AudioMessage()
        audio_message_output.author = raw_message['sender_name']
        audio_message_output.message_id = raw_message['timestamp_ms']
        audio_message_output.media_uri = raw_message['audio_files'][0]['uri']
        r_builder = react_builder.ReactBuilder()
        if 'reactions' in raw_message:
            audio_message_output.reacts = self.build_reactions(raw_message['reactions'])
        return audio_message_output

