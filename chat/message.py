class Message:
    """
    Holds message data for a chat member.
    @author: Jared Barrow
    """
    def __init__(
            self,
            author_name='',
            message_id=0,
            text='',
            num_of_reacts=0):
        self.__author = author_name
        self.__message_id = message_id
        self.__text = text
        self.__number_of_reacts = num_of_reacts

    def __eq__(self, other):
        return \
            self.__author == other.get_author() and \
            self.__message_id == other.get_message_id() and \
            self.__text == other.get_text() and \
            self.__number_of_reacts == other.get_number_of_reacts()

    def get_text(self):
        return self.__text

    def set_text(self, tex):
        self.__text = tex

    def get_message_id(self):
        return self.__message_id

    def set_message_id(self, m_id):
        self.__message_id = m_id

    def get_author(self):
        return self.__author

    def set_author(self, auth):
        self.__author = auth

    def get_number_of_reacts(self):
        return self.__number_of_reacts

    def set_number_of_reacts(self, n_reacts):
        self.__number_of_reacts = n_reacts






