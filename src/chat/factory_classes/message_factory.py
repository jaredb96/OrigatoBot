from . import factories
from . message_classes import messages


class MessageFactory:
    def __init__(self):
        self.__factory_objects = factories.Factories()

    def build_messages(self, raw_messages):
        messages_output = messages.Messages()
        for r_message in raw_messages:
            message_object = self.build_message_object_from_raw_message(
                r_message)
            messages_output.add_message(message_object)
        return messages_output

    def build_message_object_from_raw_message(self, raw_message):
        factory_objects = self.__factory_objects
        type_for_raw_message = self.get_message_type(raw_message)
        factory_for_message_type = factory_objects.get_factory(
            type_for_raw_message)
        output_message = factory_for_message_type.build_message(
            raw_message)
        return output_message

    def get_message_type(self, raw_message):
        try:
            return self.get_type(raw_message)
        except KeyError:
            return 'default'

    def get_type(self, raw_message):
        media_types = {
            'photos': 'picture',
            'gifs': 'gif',
            'videos': 'video',
            'sticker': 'sticker',
            'audio_files': 'audio'}
        message_keys = set(raw_message.keys())
        type_keys = set(media_types.keys())

        # This raw message is a media message if at least one keys
        # in the raw message is a key in the media types map.
        # This checks that the intersection of the two key sets are
        # not equal.
        intersection_of_message_and_media_type_keys = \
            message_keys.intersection(type_keys)
        is_media_message = bool(
            intersection_of_message_and_media_type_keys)
        if is_media_message:
            # If the intersection isn't empty, it is made of one element
            # which is the message type
            return media_types[intersection_of_message_and_media_type_keys.pop()]
        else:
            # If not a media message then it is either a text message or deleted message.
            if 'content' in raw_message:
                return 'text'
            return 'deleted'




