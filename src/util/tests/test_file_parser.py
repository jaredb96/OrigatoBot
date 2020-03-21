import unittest
import inspect
from .. import file_parser


class TestFileParser(unittest.TestCase):
    def test_module_loads_properly(self):
        """
        Checks if FileParser module loads correctly.
        """
        file_parser_loads_properly = inspect.isclass(
            file_parser.FileParser)