import unittest
from chat import media_message
import inspect


class TestMediaMessage(unittest.TestCase):
    def test_module_creation(self):
        """
        Checks the MediaMessage module loads properly.
        """
        media_message_is_a_class = inspect.isclass(
            media_message.MediaMessage)
        self.assertTrue(media_message_is_a_class)

    def test_get_and_set_media_uri(self):
        """
        Checks the simple getters and setters for the media uri
        property.
        """
        test_media_message = media_message.MediaMessage()
        test_media_uri = '123'
        test_media_message.set_media_uri(test_media_uri)
        expected_media_uri = '123'
        actual_media_uri = test_media_message.get_media_uri()
        expected_media_uri_is_actual = \
            expected_media_uri == actual_media_uri
        self.assertTrue(expected_media_uri_is_actual)
        not_expected_media_uri = '45'
        not_expected_media_uri_is_actual = \
            not_expected_media_uri == actual_media_uri
        self.assertFalse(not_expected_media_uri_is_actual)

