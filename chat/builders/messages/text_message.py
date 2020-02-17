from chat import message


class TextMessage(message.Message):
    def __init__(self):
        self.__text_content = ''

    def get_text_content(self):
        return self.__text_content

    def set_text_content(self, tc):
        self.__text_content = tc

