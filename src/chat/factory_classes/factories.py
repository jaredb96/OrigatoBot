from . import gif_message_factory
from . import audio_message_factory
from . import picture_message_factory
from . import sticker_message_factory
from . import text_message_factory
from . import video_message_factory
from . import summary_message_factory


class Factories:
    def __init__(self):
        gif_factory = gif_message_factory.GifMessageFactory
        audio_factory = audio_message_factory.AudioMessageFactory
        picture_factory = picture_message_factory.PictureMessageFactory
        sticker_factory = sticker_message_factory.StickerMessageFactory
        text_factory = text_message_factory.TextMessageFactory
        video_factory = video_message_factory.VideoMessageFactory
        summary_factory = summary_message_factory.SummaryMessageFactory
        self.__factory_objects = {
            'gif': gif_factory,
            'audio': audio_factory,
            'picture': picture_factory,
            'sticker': sticker_factory,
            'text': text_factory,
            'video': video_factory,
            'summary': summary_factory,
            'default': text_factory}

    def get_factory(self, factory_type):
        return self.__factory_objects[factory_type]
