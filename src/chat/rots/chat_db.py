from . import member
from numpy.polynomial.polynomial import polyfit


class ChatDb:
    def __init__(self):
        self.members = []
        self.__member_mapping = {}
        self.messages_per_member = {}
        self.reacts_per_member = {}

    def get_member(self, name):
        return self.__member_mapping[name]

    def get_number_of_messages_in_chat(self):
        message_counter = 0
        for chat_member in self.members:
            message_counter += chat_member.get_number_of_messages()
        return message_counter

    def get_messages_per_member(self):
        return self.messages_per_member.values()

    def get_reacts_per_member(self):
        return self.reacts_per_member

    def get_coefficients_for_rots_score(self):
        messages_per_member = self.get_messages_per_member()
        reacts_per_member = self.get_reacts_per_member()
        return polyfit(
            messages_per_member,
            reacts_per_member,
            1)
