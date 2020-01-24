from chat import summary_builder
from chat.message import Message
import unittest


class TestSummaryBuilder(unittest.TestCase):
    def test_module_creation(self):
        """
        desc: Tests that the summary_creator class is actually a class.
        """
        test_item = summary_builder.SummaryBuilder()
        class_name = 'SummaryBuilder' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_all_getters_and_setters(self):
        test_item = summary_builder.SummaryBuilder()

        test_message_1 = Message(author_name='joseph', text='im gey', num_of_reacts=5, message_id=0)
        test_message_2 = Message(author_name='tanner', text='awight i like math', num_of_reacts=1, message_id=1)
        test_message_3 = Message(author_name='hussain', text='<(^__^)>', num_of_reacts=1, message_id=2)
        test_messages = [test_message_1, test_message_2, test_message_3]

        test_item.set_messages(test_messages)
        self.assertEqual(test_item.get_messages(), test_messages)

        test_summary_message = 'ya yeet test summary message'
        test_item.set_summary_message(test_summary_message)
        self.assertEqual(test_item.get_summary_message(), test_summary_message)

        test_item = summary_builder.SummaryBuilder(test_messages)
        test_summary_message = 'ya yeet gang gang here are your top messages bitches !\n' \
                               'joseph: im gey\n' \
                               '5 reacts\n' \
                               '------------------------\n' \
                               'tanner: awight i like math\n' \
                               '1 react\n' \
                               '------------------------\n' \
                               'hussain: <(^__^)>\n' \
                               '1 react\n' \
                               '------------------------\n' \
                               'now that you got your messages, im out this shit, bitch !'
        self.assertEqual(test_item.get_summary_message(), test_summary_message)

