import unittest
import inspect
from .. import account_accessor


class TestAccountAccessor(unittest.TestCase):
    def test_module_creation(self):
        """
        Checks that the AccountAccessor module is loading properly.
        """
        account_accessor_is_a_class = inspect.isclass(
            account_accessor.AccountAccessor)
        self.assertTrue(account_accessor_is_a_class)

    def test_access_account(self):
        """
        Checks the method that accesses the account.
        """
        raise NotImplementedError

