from selenium import webdriver
from setup import load_global_configs
from setup.load_global_configs import CONFIGS


class OptionsFetcher:
    def __init__(self):
        self.HEADLESS_ARG = 'headless'
        self.WINDOW_SIZE_ARG = 'window-size=1920x1080'
        self.DISABLE_GPU_ARG = 'disable-gpu'
        self.DISABLE_NOTIFICATIONS_ARG = '--disable-notifications'
        self.NO_SANDBOX_ARG = '--no-sandbox'
        self.VERBOSE_ARG = '--verbose'
        self.PREFs_ARG = 'prefs'
        self.__arguments = [self.HEADLESS_ARG,
                            self.WINDOW_SIZE_ARG,
                            self.DISABLE_GPU_ARG,
                            self.DISABLE_NOTIFICATIONS_ARG,
                            self.NO_SANDBOX_ARG,
                            self.VERBOSE_ARG,
                            self.PREFs_ARG]
        load_global_configs.load_global_configs()
        self.EXPERIMENTAL_ARG = {
                "download.default_directory":
                CONFIGS['downloads_directory'],
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
            }
        self.options = webdriver.ChromeOptions()

    def get_driver_options(self):
        self.add_arguments()
        self.add_experimental_option(self.EXPERIMENTAL_ARG)
        return self.options

    def add_arguments(self):
        for argument in self.__arguments:
            self.options.add_argument(argument)

    def add_experimental_option(self, e_option):
        self.options.add_experimental_option(self.PREFs_ARG, e_option)
