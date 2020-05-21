class MessageRanker:
    def get_top_three_messages(self, messages):
        top_three_message = []
        sorted_messages = self.get_sorted_messages(messages)
        for i, message in enumerate(sorted_messages):
            if i < 3 or message.get_number_of_reacts() >= 4:
                top_three_message.append(message)
            else:
                number_of_reacts_for_message = message.\
                    get_number_of_reacts()
                number_of_reacts_for_last_place = \
                    sorted_messages[i-1].get_number_of_reacts()
                there_is_a_tie_for_last_place = \
                    number_of_reacts_for_message == \
                    number_of_reacts_for_last_place
                if there_is_a_tie_for_last_place and number_of_reacts_for_message != 0:
                    top_three_message.append(message)
                else:
                    break
        return top_three_message

    def get_sorted_messages(self, messages):
        sorted_messages = sorted(
            messages.message_bank,
            key=lambda x: x.get_number_of_reacts(),
            reverse=True)
        return sorted_messages
