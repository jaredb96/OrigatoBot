from . import message


class DeletedMessage(message.Message):
    def __init__(self):
        super(DeletedMessage, self).__init__()

