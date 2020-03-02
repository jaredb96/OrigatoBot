from . import message


class MediaMessage(message.Message):
    def __init__(self):
        self.media_uri = ''
