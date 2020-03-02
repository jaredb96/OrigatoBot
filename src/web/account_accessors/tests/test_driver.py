import unittest
import inspect
from .. import driver


class TestDriver(unittest.TestCase):
    """
    NOTE: This class is not unit tested.
    """
    global test_driver
    test_driver = driver.Driver()

    def test_module_creation(self):
        """
        Checks that the Driver module loads properly.
        """
        driver_is_a_class = inspect.isclass(driver.Driver)
        self.assertTrue(driver_is_a_class)

    def test_get_url(self):
        raise NotImplementedError

    def test_find_username_and_password_elements(self):
        raise NotImplementedError

    def test_type_in_username_and_password(self):
        raise NotImplementedError

    def test_enable_headless_download(self):
        """
        Checks the method that enables headless download mode on the
        driver object.
        """
        test_driver.enable_headless_download()
        test_options = test_driver.fetcher.options
        self.assertTrue(test_options.headless)