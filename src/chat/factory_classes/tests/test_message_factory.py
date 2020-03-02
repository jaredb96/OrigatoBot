import sys
import os
sys.path.append(os.path.join(
    os.path.dirname(__file__), '../../factory_classes'))
import message_factory
import unittest
import inspect
from message_classes import text_message


class TestMessageFactory(unittest.TestCase):
    def test_module_creation(self):
        """
        Checks the MessageFactory module loads properly.
        """
        message_factory_is_a_class = inspect.isclass(
            message_factory.MessageFactory)
        self.assertTrue(message_factory_is_a_class)

    def test_build_messages(self):
        raise NotImplementedError

    def test_build_message_object_from_raw_message(self):
        test_factory = message_factory.MessageFactory()
        expected_message = text_message.TextMessage()
        expected_message.set_text('test_text')
        expected_message.set_author('test_author')
        expected_message.set_message_id('test_id')
        actual_raw_message = {}
        actual_message = \
            test_factory.test_build_message_object_from_raw_message(
                actual_raw_message)
        expected_message_is_actual = expected_message == actual_message
        self.assertTrue(expected_message_is_actual)
        wrong_message = text_message.TextMessage()
        actual_message_is_wrong = actual_message == wrong_message
        self.assertFalse(actual_message_is_wrong)