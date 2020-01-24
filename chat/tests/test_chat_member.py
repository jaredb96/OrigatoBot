from chat import chat_member as chatmember
from chat import message
import unittest


class TestChatMember(unittest.TestCase):
    """
    Unit testing for ChatRoom Member.
    @author: Jared Barrow
    """
    def test_module_creation(self):
        """
        desc: Tests that the messages class is actually a class.
        """
        test_item = chatmember.ChatMember()
        class_name = 'ChatMember' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_all_getters_and_setters(self):
        test_item = chatmember.ChatMember()
        test_item.set_member_name('Alice')
        self.assertEqual('Alice',test_item.get_member_name())
        test_message_1 = message.Message()
        test_message_2 = message.Message()
        test_message_3 = message.Message()
        test_messages = [
            test_message_1,
            test_message_2,
            test_message_3]
        test_item.set_message_bank(test_messages)
        self.assertEqual(test_messages, test_item.get_message_bank())
        return "TODO"

    def test_sort_pairs(self):
        test_item = chatmember.ChatMember()
        test_message_1 = message.Message('Alice', 1, 'Test', 4)
        test_message_2 = message.Message('Bob', 2, 'Test', 2)
        test_message_3 = message.Message('Carol', 3, 'Test', 0)
        test_message_4 = message.Message('Dan', 4, 'Test', 8)
        test_message_5 = message.Message('Edgar', 5, 'Test', 1)
        test_message_6 = message.Message('Frank', 6, 'Test', 7)

        test_messages = [
            test_message_1,
            test_message_2,
            test_message_3,
            test_message_4,
            test_message_5,
            test_message_6]
        test_item.set_message_bank(test_messages)

        test_list = test_item.get_top_k_messages(3)

        self.assertEqual(
            [test_message_4, test_message_6, test_message_1],
            test_list)

    def test_add_to_message_bank(self):
        test_item = chatmember.ChatMember()
        test_message_1 = message.Message('Alice', 1, 'Test', 4)
        test_message_2 = message.Message('Bob', 2, 'Test', 2)
        test_message_3 = message.Message('Carol', 3, 'Test', 0)
        test_message_4 = message.Message('Dan', 4, 'Test', 8)
        test_message_5 = message.Message('Edgar', 5, 'Test', 1)
        test_message_6 = message.Message('Frank', 6, 'Test', 7)

        test_messages = [
            test_message_1,
            test_message_2,
            test_message_3,
            test_message_4,
            test_message_5,
            test_message_6]
        test_item.set_message_bank(test_messages)

        new_message = message.Message('TestMember', 1, 'Test', 2)
        test_item.add_to_message_bank(new_message)
        test_messages.append(new_message)

        self.assertEqual(test_messages, test_item.get_message_bank())


