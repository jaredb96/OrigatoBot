from ..factory_classes.message_classes import *
from . import rots


class Member:
    def __init__(self):
        self.name = ''
        self.messages = []
        self.__message_mapping = {}
        self.rots_obj = rots.Rots()

    def get_message(self, message_id):
        return self.__message_mapping[message_id]

    def get_number_of_messages(self):
        return len(self.messages)

    def get_total_number_of_reacts(self):
        messages = self.messages
        reacts_counter = 0
        for message in messages:
            reacts_counter += message.get_number_of_reacts()
        return reacts_counter

    def get_rots_score(self, total_reacts_in_chat):
        number_of_messages = self.get_number_of_messages()
        number_of_reacts = self.get_total_number_of_reacts()
        rots_for_this_member = self.rots_obj
        score = rots_for_this_member.get_score(
            number_of_reacts,
            number_of_messages,
            total_reacts_in_chat)
        return score
