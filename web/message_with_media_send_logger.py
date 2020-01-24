from web.logger import Logger
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.config import CONFIGS
import time

ORIGATO_CHAT_URL = 'https://www.messenger.com/t/1738204539622881'
ORIGATO_BOT_CHAT_URL = 'https://www.messenger.com/t/origato.bot.5'

DESTINATION_URL = ORIGATO_BOT_CHAT_URL


class MessageWithMediaSendLogger(Logger):

    def __init__(self, messages_to_send):
        self.__messages_to_send = messages_to_send
        self.__driver = Logger.login(self, DESTINATION_URL)
        self.get_driver().maximize_window()

    def send_summary(self):
        print('sending summary message...')
        driver = self.get_driver()
        chat_box = self.get_chat_box()

        greeting_message = CONFIGS['greeting_message']
        farewell_message = CONFIGS['farewell_message']

        ActionChains(driver).move_to_element(chat_box).click(chat_box).perform()
        chat_box.send_keys(greeting_message + '\n')

        self.send_messages()

        chat_box = self.get_chat_box()
        chat_box.send_keys(farewell_message + '\n')

        # wait for messages to fully send
        time.sleep(3)

        print('summary sent! closing...')
        driver.close()
        driver.quit()

    def send_messages(self):
        driver = self.get_driver()
        for message in self.get_messages_to_send():
            chat_box = self.get_chat_box()
            ActionChains(driver).move_to_element(chat_box).click(chat_box).perform()

            message_author = message.get_author()
            message_num_of_reacts = message.get_number_of_reacts()

            chat_box.send_keys(
                '*' + message_author + ', ' +
                str(message_num_of_reacts) + ' react' + ('s:' if message_num_of_reacts > 1 else ':') + '*'
                )
            if message.get_text() != '':
                # send text
                self.send_text_message(message)
            else:
                # send media
                self.send_media_message(message)

    def send_media_message(self, message):
        driver = self.get_driver()
        chat_box = self.get_chat_box()

        # media_uri = 'C:/GitHub/WebScrapeChatBot/' + message.get_media_uri()
        media_uri = os.getcwd() + '/' + message.get_media_uri()

        filename, ext = os.path.splitext(media_uri)
        # using mp4's to mp3's for audio
        if ext == '.mp4' and '/audio' in media_uri:
            media_uri = filename + '.mp3'
        try:
            add_files_elmnt = driver.find_elements_by_xpath("//*[@class='_n _2__f _4e5e']")[1]
        except:
            driver.refresh()
            chat_box = self.get_chat_box()
            add_files_elmnt = driver.find_elements_by_xpath("//*[@class='_n _2__f _4e5e']")[1]
        add_files_elmnt.send_keys(media_uri)
        chat_box.send_keys(Keys.ENTER)

    def send_text_message(self, message):
        chat_box = self.get_chat_box()
        text = self.reformat_string(message.get_text())
        chat_box.send_keys(Keys.SHIFT + Keys.ENTER + Keys.SHIFT + text + Keys.ENTER)

    def reformat_string(self, text):
        return text.replace('\n', Keys.SHIFT + Keys.ENTER + Keys.SHIFT)

    def get_messages_to_send(self):
        return self.__messages_to_send

    def set_messages_to_send(self, messages_to_send):
        self.__messages_to_send = messages_to_send

    def get_driver(self):
        return self.__driver

    def set_driver(self, driver):
        self.__driver = driver

    def get_chat_box(self):
        # for group chats, chat box is 2nd text window
        if DESTINATION_URL == ORIGATO_CHAT_URL:
            return self.get_driver().find_elements_by_xpath("//*[@class='_1mf _1mj']")[1]
        # for private chats, chat box is 1st (and only) text window
        elif DESTINATION_URL == ORIGATO_BOT_CHAT_URL:
            return self.get_driver().find_elements_by_xpath("//*[@class='_1mf _1mj']")[0]
