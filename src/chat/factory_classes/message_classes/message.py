class Message:
    """
    Holds message data for a chat member.
    @author: Jared Barrow
    """
    def __init__(self, author_name='', message_id=''):
        self.author = author_name
        self.message_id = message_id
        self.reacts = []

    def __eq__(self, other):
        return \
            self.author == other.author and \
            self.message_id == other.message_id and \
            self.reacts == other.reacts






