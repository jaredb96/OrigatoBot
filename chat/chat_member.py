from chat import message


class ChatMember:
    """
    Represents a member of the messenger chat - holds a list of
    messages.
    @author: Jared Barrow
    """
    def __init__(self, member_name='', message_bank=[]):
        self.__name = member_name
        self.__message_bank = []

    def get_member_name(self):
        return self.__name

    def set_member_name(self, nam):
        self.__name = nam

    def get_message_bank(self):
        return self.__message_bank

    def set_message_bank(self, mb):
        self.__message_bank = mb

    def add_to_message_bank(self, chat_messsge):
        self.__message_bank.append(chat_messsge)

    def get_top_k_messages(self, k):
        """
        Returns a list of te top k messages for this chat member based
        on its number of reacts.
        :param k: positive int number of messages we want, must be less
        than or equal to the size of the message_bank
        :return: list of top k messages
        """
        # Method for sorting pairs based on second element.
        # Used to sort the (react, id) pairs we map to in descending
        # order.
        def sort_pairs(pairs):
            return sorted(pairs, key=lambda x: x[0], reverse=True)

        message_id_to_message_map = {}
        message_id_to_reacts_id_map = {}
        top_messages = []

        for message in self.get_message_bank():
            message_id_to_message_map[message.get_message_id()] = \
                message
        for message in self.get_message_bank():
            message_id_to_reacts_id_map[message.get_message_id()] = \
                (message.get_number_of_reacts(), message.get_message_id())

        reacts_id_pairs = message_id_to_reacts_id_map.values()
        sorted_pairs = sort_pairs(reacts_id_pairs)
        for pair in sorted_pairs:
            id_for_message = pair[1]
            top_messages.append(
                message_id_to_message_map[id_for_message])
        return top_messages[0:k]

    # function wasn't defined earlier
    def get_best_message(self):
        top_message_list = self.get_top_k_messages(1)
        if top_message_list:
            return top_message_list[0]
        return None

    def get_total_reacts(self):
        total_reacts = 0
        for message in self.get_message_bank():
            total_reacts += message.get_number_of_reacts()
        return total_reacts










