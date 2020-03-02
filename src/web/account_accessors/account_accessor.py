from . import driver


class AccountAccessor:
    """
    Module that logs into account.
    Author: Jared Barrow
    """
    def __init__(self):
        self.url = ''
        self.__driver = driver.Driver()

    def access_account(self):
        account_driver = self.__driver
        url = self.url
        account_driver.get_url(url)
        account_driver.find_username_and_password_elements()
        account_driver.type_in_username_and_password()

