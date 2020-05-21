from . import message


class MediaMessage(message.Message):
    def __init__(self):
        super(MediaMessage, self).__init__()
        self.media_uri = ''
