from . import message


class TextMessage(message.Message):
    def __init__(self):
        super(TextMessage, self).__init__()
        self.text = ''

