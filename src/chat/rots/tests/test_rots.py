import unittest
import inspect
from .. import rots


class TestRots(unittest.TestCase):
    def test_module_creation(self):
        """
        Checks that the Rots module loads properly.
        """
        rots_loads_properly = inspect.isclass(rots.Rots)
        self.assertTrue(rots_loads_properly)

