from web.logger import Logger
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ORIGATO_CHAT_URL = "https://www.messenger.com/t/1738204539622881"
ORIGATO_BOT_CHAT_URL = 'https://www.messenger.com/t/origato.bot.5'

DESTINATION_URL = ORIGATO_BOT_CHAT_URL


class MessageSendLogger(Logger):

    def __init__(self, message: str):
        self.message = message

    def send_message(self):
        driver = Logger.login(self, DESTINATION_URL)

        chat_box = self.get_chat_box(driver)
        ActionChains(driver).move_to_element(chat_box).click(chat_box).perform()

        # replace all '\n' with 'shift+enter' keys
        message_to_send = ""
        for line in self.message.split('\n'):
            message_to_send += line + Keys.SHIFT + Keys.ENTER + Keys.SHIFT
        chat_box.send_keys(message_to_send)
        chat_box.send_keys(Keys.ENTER)

        driver.close()
        driver.quit()

    def get_chat_box(self, driver):
        # for group chats, chat box is 2nd text window
        if DESTINATION_URL == ORIGATO_CHAT_URL:
            return driver.find_elements_by_xpath("//*[@class='_1mf _1mj']")[1]
        # for private chats, chat box is 1st (and only) text window
        elif DESTINATION_URL == ORIGATO_BOT_CHAT_URL:
            return driver.find_elements_by_xpath("//*[@class='_1mf _1mj']")[0]


