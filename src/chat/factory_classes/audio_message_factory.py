from . import general_message_factory
from . message_classes import audio_message
from . message_classes import react_builder


class AudioMessageFactory(general_message_factory.GeneralFactory):
    def build_message(self, raw_message):
        audio_message_output = audio_message.AudioMessage()
        audio_message_output.author = raw_message['sender_name']
        audio_message_output.message_id = raw_message['timestamp_ms']
        audio_message_output.media_uri = raw_message['audio_files']
        r_builder = react_builder.ReactBuilder()
        audio_message_output.reacts = r_builder.build_reacts(
            raw_message['reacts'])
        return audio_message_output

