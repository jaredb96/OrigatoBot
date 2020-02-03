from chat import react


class Message:
    def __init__(self):
        self.__author = ''
        self.__message_id = ''
        self.__reacts = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_author(self):
        return self.__author

    def set_author(self, auth):
        self.__author = auth

    def get_message_id(self):
        return self.__message_id

    def set_message_id(self, mi):
        self.__message_id = mi

    def get_reacts(self):
        return self.__reacts

    def set_reacts(self, reac):
        self.__reacts = reac








