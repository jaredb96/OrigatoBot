class Summary:
    def __init__(self, top_three_messages):
        self.top_three_messages = top_three_messages

    def make_summary_message(self):
        summary_message = ''
        summary_message += 'ya yeet gang gang here are your top messages' \
                           ' from the last 24 hours bitches !\n'

        for message in self.top_three_messages:
            num_reacts = message.get_number_of_reacts()
            author = message.get_author()
            text = message.get_text()

            summary_message += author + ': ' + text + '\n' + \
                               str(num_reacts) + ' react' + (
                                   's' if num_reacts > 1 else '') + '\n' \
                               + '------------------------' + '\n'
        summary_message += 'now that you got your messages, im out this ' \
                           'shit, bitch !'

        return summary_message