from chat.message import Message


class SummaryBuilder:
    def __init__(self, messages=[]):
        self.messages = messages
        self.summary_message = self.create_summary_message()

    def create_summary_message(self):
        summary_message = ''
        summary_message += 'ya yeet gang gang here are your top messages from the last 24 hours bitches !\n'

        for message in self.messages:
            num_reacts = message.get_number_of_reacts()
            author = message.get_author()
            text = message.get_text()

            summary_message += author + ': ' + text + '\n' + \
                str(num_reacts) + ' react' + ('s' if num_reacts > 1 else '') + '\n' \
                + '------------------------' + '\n'
        summary_message += 'now that you got your messages, im out this shit, bitch !'

        return summary_message

    def get_summary_message(self):
        return self.summary_message

    def get_messages(self):
        return self.messages

    def set_messages(self, messages):
        self.messages = messages

    def set_summary_message(self, summary_message):
        self.summary_message = summary_message

# test case
# m_a = Message(author_name='joseph', text='im gey', num_of_reacts=5, message_id=0)
# m_b = Message(author_name='tanner', text='awight i like math', num_of_reacts=1, message_id=1)
# m_c = Message(author_name='hussain', text='<(^__^)>', num_of_reacts=1, message_id=2)
#
# messages = [m_a, m_b, m_c]
#
# summary_creator = SummaryBuilder(messages)
#
# print(summary_creator.get_summary_message())
