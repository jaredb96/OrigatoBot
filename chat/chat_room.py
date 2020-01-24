from chat import chat_member, message


class ChatRoom:
    """
    A single messenger chat instance.
    @author: Jared Barrow
    """
    def __init__(self, members_list=[]):
        self._chat_members = members_list

    def get_chat_members(self):
        return self._chat_members

    def set_chat_members(self, chm):
        self._chat_members = chm

    def make_chat_members_from_names_list(self, names_list):
        members = []
        for name in names_list:
            member = chat_member.ChatMember(name)
            members.append(member)

        return members

    def sort_message_list_by_number_of_reacts(self, messages):
        # sorted_message_list = []
        # messages_to_reacts_map = {}
        #
        # for message in top_messages:
        #     print(message.get_author() + ': ' + message.get_text())
        #     print('--------------------------')
        #
        # for message in top_messages:
        #     messages_to_reacts_map[message] = \
        #         message.get_number_of_reacts()
        # reacts_list = sorted(list(messages_to_reacts_map.keys(),
        #                           reverse=True))
        # for i in range(len(reacts_list)):
        #     sorted_message_list.append(messages_to_reacts_map[
        #                                    reacts_list[i]])
        # return sorted_message_list

        # Message object is unhashable
        sorted_message_list = sorted(messages, key=lambda x: x.get_number_of_reacts(), reverse=True)
        return sorted_message_list

    def assign_messages_to_members(self, message_list):
        members = self.get_chat_members()
        for chat_message in message_list:
            author = chat_message.get_author()
            for member in members:
                if member.get_member_name() == author:
                    member.add_to_message_bank(chat_message)

    def get_top_k_messages(self, k):
        top_message_from_each_member = []
        for member in self.get_chat_members():
            best_message = member.get_best_message()
            # error where None was being added
            if best_message:
                top_message_from_each_member.append(best_message)
        sorted_messages = self.sort_message_list_by_number_of_reacts(
            top_message_from_each_member)
        top_k_messages = [sorted_messages[i] for i in range(k)]
        return top_k_messages
