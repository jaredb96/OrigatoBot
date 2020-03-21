import unittest
import inspect
from .. import message_ranker


class TestMessageRanker(unittest.TestCase):
    def test_module_loads_properly(self):
        """
        Checks that MessageRanker module loads properly.
        """
        message_ranker_loads_properly = inspect.isclass(
            message_ranker.MessageRanker)