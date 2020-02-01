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
        all_messages = self.get_all_messages()
        all_messages_sorted = self.sort_message_list_by_number_of_reacts(all_messages)

        if k <= all_messages_sorted:
            return all_messages_sorted[0:k]
        else:
            return all_messages_sorted

    def get_top_k_messages_with_ties(self, k):
        all_messages = self.get_all_messages()
        all_messages_sorted = self.sort_message_list_by_number_of_reacts(all_messages)

        top_k_messages = []
        for i, message in enumerate(all_messages_sorted):
            if i < k:
                top_k_messages.append(message)
            else:
                num_reacts = message.get_number_of_reacts()
                ties_with_previous = num_reacts == all_messages_sorted[i-1].get_number_of_reacts()

                if ties_with_previous and num_reacts != 0:
                    top_k_messages.append(message)
                else:
                    break

        return top_k_messages

    def get_all_messages(self):
        all_messages = []
        for member in self.get_chat_members():
            all_messages.extend(member.get_message_bank())
        return all_messages
