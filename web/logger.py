from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from setup.load_global_configs import CONFIGS
import time
import random

# set HEADLESS to True if you don't want a browser to open up
# set HEADLESS to False if you want a browser to open up
HEADLESS = True

class Logger:
    def __init__(self):
        None

    def login(self, url: str):
        driver = self.driver_setup()
        driver.get(url)

        username = driver.find_element_by_id("email")
        password = driver.find_element_by_id("pass")

        user_username = CONFIGS['username']
        user_password = CONFIGS['password']

        username.send_keys(user_username)
        self.sleep_up_to_5_secs()

        password.send_keys(user_password)
        self.sleep_up_to_5_secs()

        # simulates the press of the login button.
        driver.find_element_by_name("login").click()

        return driver

    def driver_setup(self):
        options = self.get_browser_options()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        # enable downloads and set download directory
        if HEADLESS:
            self.enable_headless_download(driver)
        return driver

    def get_browser_options(self):
        options = webdriver.ChromeOptions()

        # if we don't want a browser to open up, configure for 'headless'
        if HEADLESS:
            download_dir = CONFIGS['downloads_directory']
            options.add_argument('headless')  # enable headless browser navigation
            options.add_argument('window-size=1920x1080')  # set window size
            options.add_argument('disable-gpu')
            options.add_argument("--disable-notifications")
            options.add_argument('--no-sandbox')
            options.add_argument('--verbose')
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,  # set download directory
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
            })

        return options

    def enable_headless_download(self, driver):
        download_dir = CONFIGS['downloads_directory']

        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        driver.execute("send_command", params)
        print('set download directory to: ' + download_dir)

    def sleep_up_to_5_secs(self):
        time_to_sleep = random.randint(1, 5)

        time.sleep(time_to_sleep)
