import sys
import os
sys.path.append(os.path.join(
    os.path.dirname(__file__), '../../builders'))
import message_builder
import unittest
import inspect


class TestMessageBuilder(unittest.TestCase):
    def test_module_creation(self):
        """
        Checks the MessageBuilder module loads properly.
        """
        message_builder_is_a_class = inspect.isclass(
            message_builder.MessageBuilder)
        self.assertTrue(message_builder_is_a_class)
