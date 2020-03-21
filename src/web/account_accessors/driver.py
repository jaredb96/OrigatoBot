from ..account_accessors import options_fetcher
from setup import load_global_configs
from setup.load_global_configs import CONFIGS
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import random


class Driver:
    def __init__(self):
        self.fetcher = options_fetcher.OptionsFetcher()
        self.options = self.fetcher.get_driver_options()
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=self.options)
        self.enable_headless_download()

    def get_url(self, url):
        self.driver.get(url)
        raise NotImplementedError

    def find_username_and_password_elements(self):
        email = self.driver.find_element_by_id('email')
        pass_phrase = self.driver.find_element_by_id('pass')
        username = CONFIGS['usernmae']
        user_pass = CONFIGS['password']

        email.send_keys(username)
        self.sleep_for_a_few_seconds()

        pass_phrase.send_keys(user_pass)
        self.sleep_for_a_few_seconds()

    def sleep_for_a_few_seconds(self):
        length_of_sleeping_time = random.randint(1, 5)
        time.sleep(length_of_sleeping_time)

    def type_in_username_and_password(self):
        self.driver.find_element_by_name('login').click()

    def enable_headless_download(self):
        download_directory = CONFIGS['downloads_directory']
        self.driver.command_executor._commands['send_command'] = \
            ('POST', '/session/$sessionId/chromium/send_command')
        parameters = {
            'cmd': 'Page.setDownloadBehavior',
            'params':
                {'behavior': 'allow',
                 'downloadPath': download_directory}}
        self.driver.execute('send_command', parameters)