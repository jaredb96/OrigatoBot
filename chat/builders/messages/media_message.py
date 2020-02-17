from chat import message


class MediaMessage(message.Message):
    def __init__(self):
        self.__media_uri = ''

    def get_media_uri(self):
        return self.__media_uri

    def set_media_uri(self, media_uri):
        self.__media_uri = media_uri
