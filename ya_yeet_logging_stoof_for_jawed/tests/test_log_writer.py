import unittest
from ya_yeet_logging_stoof_for_jawed import log_writer
import os


class TestLogWriter(unittest.TestCase):

    def test_module_creation(self):
        test_item = log_writer.LogWriter()
        class_name = 'LogWriter' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_log_info_from_map(self):
        test_logwriter = log_writer.LogWriter()

        test_map = {
            "info_1": "123",
            "info_2": "abc",
            "info_3": 123,
        }

        test_logwriter.log_info_from_map(test_map)

        expected_logs = "--------------------\n" \
                       "INFO_1: 123\n" \
                       "INFO_2: abc\n" \
                       "INFO_3: 123\n" \
                       "--------------------\n"

        with open('logs.txt') as file:
            self.assertTrue(expected_logs in file.read())

        os.remove('logs.txt')

    def test_log(self):
        test_logwriter = log_writer.LogWriter()
        test_tag = "this is the tag of the test log"
        test_log = "this is the content of the test log"

        test_logwriter.log(test_tag, test_log)
        expected_log = "THIS IS THE TAG OF THE TEST LOG: this is the content of the test log"

        with open('logs.txt') as file:
            self.assertTrue(expected_log in file.read())

        os.remove('logs.txt')

    def write_perforated_line(self):
        expected_line = "--------------------"

        with open('logs.txt') as file:
            self.assertTrue(expected_line in file.read())

        os.remove('logs.txt')
