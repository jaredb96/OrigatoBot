from chat import message
import unittest


class TestMessages(unittest.TestCase):
    """
    test_message.py - Unit test class for message container class.
    @author: Jared Barrow
    """
    def test_module_creation(self):
        """
        desc: Tests that the messages class is actually a class.
        """
        test_item = message.Message()
        class_name = 'Message' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_all_getters_and_setter(self):
        """
        desc: Tests all getters and setters in messages class.
        """
        test_item = message.Message()
        test_item.set_text('Hello world!')
        self.assertEqual('Hello world!', test_item.get_text())

        test_item.set_message_id(12345)
        self.assertEqual(12345, test_item.get_message_id())

        test_item.set_author('Alice')
        self.assertEqual('Alice', test_item.get_author())

        test_item.set_number_of_reacts(1)
        self.assertEqual(1, test_item.get_number_of_reacts())
