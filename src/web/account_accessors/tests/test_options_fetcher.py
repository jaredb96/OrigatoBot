import unittest
import inspect
from .. import options_fetcher
from setup.load_global_configs import CONFIGS


class TestOptionsFetcher(unittest.TestCase):
    global fetcher
    fetcher = options_fetcher.OptionsFetcher()

    def test_module_creation(self):
        """
        Checks that the Options module loads properly.
        """
        options_fetcher_is_a_class = inspect.isclass(
            options_fetcher.OptionsFetcher)
        self.assertTrue(options_fetcher_is_a_class)

    def test_get_driver_options(self):
        """
        Checks that the get driver method works.
        """
        test_experimental_option = {
            "download.default_directory":
                CONFIGS['downloads_directory'],
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        }
        fetcher.add_experimental_option(test_experimental_option)
        fetcher.add_arguments()
        expected_options = fetcher.options
        actual_options = fetcher.get_driver_options()
        expected_options_is_actual = expected_options == actual_options
        self.assertTrue(expected_options_is_actual)

    def test_add_arguments(self):
        """
        Checks that the method that adds arguments to options works.
        """
        fetcher.add_arguments()
        test_options = fetcher.options
        actual_argument = test_options.arguments
        expected_argument = ['headless',
                             'window-size=1920x1080',
                             'disable-gpu',
                             '--disable-notifications',
                             '--no-sandbox',
                             '--verbose',
                             'prefs']
        expected_argument_is_actual = \
            expected_argument == actual_argument
        self.assertTrue(expected_argument_is_actual)

    def test_add_experimental_option(self):
        """
        Checks the method that adds the experimental option to the
        options class.
        """
        test_experimental_option = {
                "download.default_directory":
                CONFIGS['downloads_directory'],
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
            }
        fetcher.add_experimental_option(test_experimental_option)
        test_options = fetcher.options
        expected_experimental_options = {'prefs': {
                "download.default_directory":
                CONFIGS['downloads_directory'],
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
            }}
        experimental_option_added_correctly = \
            test_options.experimental_options == \
            expected_experimental_options
        self.assertTrue(experimental_option_added_correctly)