from chat import message
import unittest
import inspect
from chat import react

class TestMessages(unittest.TestCase):
    """
    test_message.py - Unit test class for message container class.
    @author: Jared Barrow
    """
    def test_module_creation(self):
        """
        Checks that Message class loads correctly.
        """
        message_is_a_class = inspect.isclass(message.Message)
        self.assertTrue(message_is_a_class)

    def test_object_equality(self):
        first_message = message.Message()
        first_message.set_author('Alice')
        first_message.set_message_id('123')
        test_react_1 = react.React()
        test_react_1.set_reaction_type('laugh')
        test_react_1.set_actor('Bob')
        test_react_2 = react.React()
        test_react_2.set_reaction_type('cry')
        test_react_2.set_actor('Carol')
        test_react_3 = react.React()
        test_react_3.set_reaction_type('shock')
        test_react_3.set_actor('Dan')
        test_reacts = [test_react_1, test_react_2, test_react_3]
        first_message.set_reacts(test_reacts)
        second_message = message.Message()
        second_message.set_author('Alice')
        second_message.set_message_id('123')
        second_message.set_reacts(test_reacts)
        both_messages_are_equal = first_message == second_message
        self.assertTrue(both_messages_are_equal)

    def test_all_getters_and_setters(self):
        test_message = message.Message()
        test_message.set_author('Alice')
        self.assertEqual('Alice', test_message.get_author())

        test_message.set_message_id('123')
        self.assertEqual('123', test_message.get_message_id())

        test_react_1 = react.React()
        test_react_1.set_reaction_type('laugh')
        test_react_1.set_actor('Bob')
        test_react_2 = react.React()
        test_react_2.set_reaction_type('cry')
        test_react_2.set_actor('Carol')
        test_react_3 = react.React()
        test_react_3.set_reaction_type('shock')
        test_react_3.set_actor('Dan')
        test_reacts = [test_react_1, test_react_2, test_react_3]
        test_message.set_reacts(test_reacts)
        self.assertEqual(test_reacts, test_message.get_reacts())

