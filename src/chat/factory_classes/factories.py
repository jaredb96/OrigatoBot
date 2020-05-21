from . import gif_message_factory
from . import audio_message_factory
from . import picture_message_factory
from . import sticker_message_factory
from . import text_message_factory
from . import video_message_factory
from . import deleted_message_factory

class Factories:
    def __init__(self):
        gif_factory = gif_message_factory.GifMessageMessageFactory()
        audio_factory = audio_message_factory.AudioMessageMessageFactory()
        picture_factory = picture_message_factory.PictureMessageMessageFactory()
        sticker_factory = sticker_message_factory.StickerMessageMessageFactory()
        text_factory = text_message_factory.TextMessageMessageFactory()
        video_factory = video_message_factory.VideoMessageMessageFactory()
        deleted_factory = deleted_message_factory.DeletedMessageMessageFactory()
        self.__factory_objects = {
            'gif': gif_factory,
            'audio': audio_factory,
            'picture': picture_factory,
            'sticker': sticker_factory,
            'text': text_factory,
            'video': video_factory,
            'deleted': deleted_factory,
            'default': text_factory
        }

    def get_factory(self, factory_type):
        return self.__factory_objects[factory_type]
