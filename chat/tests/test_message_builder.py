import unittest
from chat import message_builder
from web import json_reader
from chat import message


class TestMessageBuilder(unittest.TestCase):
    def test_module_creation(self):
        """
        desc: Tests that the chat_scraper class is actually a class.
        """
        test_item = message_builder.MessageBuilder()
        class_name = 'MessageBuilder' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_all_getters_and_setters(self):
        test_item = message_builder.MessageBuilder()
        test_json_reader = json_reader.JsonReader()
        test_item.set_json_reader(test_json_reader)
        self.assertEqual(test_json_reader, test_item.get_json_reader())

    def test_make_list_of_messages(self):
        test_item = message_builder.MessageBuilder()
        test_json = open('test_json_file.json', 'r')
        test_json_reader = json_reader.JsonReader(test_json)
        test_item.set_json_reader(test_json_reader)
        message_1 = message.Message('Alice', 1572995131170, "Hello", 1)
        message_2 = message.Message(
            'Alice', 1572993597519, 'I agree.', 0)
        message_3 = message.Message(
            'Bob', 1572993597519, 'This is nice', 0)
        message_4 = message.Message(
            'Dan', 1572994091161, 'Hello World!', 0)
        message_5 = message.Message(
            'Edgar', 1572994272138, 'Hi Alice', 3)
        message_6 = message.Message(
            'Frank', 1572994272138, 'Nice weather', 3)
        message_7 = message.Message('George', 1572994091161, 'True', 0)
        message_8 = message.Message('Harry', 1572995131170, 'It is', 1)

        check_list = [
            message_1,
            message_2,
            message_3,
            message_4,
            message_5,
            message_6,
            message_7,
            message_8]
        self.assertEqual(
            check_list[7],
            test_item.make_list_of_messages()[7])

        test_json.close()
