import unittest
import inspect
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'chat'))
from chat import text_message


class TestTextMessage(unittest.TestCase):
    def test_module_creation(self):
        """
        Checks that the text message is loading properly.
        """
        text_message_is_a_class = inspect.isclass(
            text_message.TextMessage)
        self.assertTrue(text_message_is_a_class)

    def test_getters_and_setters(self):
        test_message = text_message.TextMessage()
        expected_text_content = 'test_content'
        test_message.set_text_content(expected_text_content)
        actual_text_content = test_message.get_text_content()
        expected_text_content_is_actual = \
            expected_text_content == actual_text_content
        self.assertTrue(expected_text_content_is_actual)
