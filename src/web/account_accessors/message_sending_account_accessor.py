from . import account_accessor
from setup.load_global_configs import CONFIGS
from src.chat.factory_classes.message_classes import text_message

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time

ORIGATO_CHAT_URL = 'https://www.messenger.com/t/1738204539622881'

HUSSAIN_CHAT_URL = 'https://www.messenger.com/t/hussain.humadi'
SEAN_CHAT_URL = 'https://www.messenger.com/t/sean.britton'
JARED_CHAT_URL = 'https://www.messenger.com/t/tobisenjumara'

GROUP_CHAT_URLS = [ORIGATO_CHAT_URL]
INDIVIDUAL_CHAT_URLS = [HUSSAIN_CHAT_URL, SEAN_CHAT_URL, JARED_CHAT_URL]

DESTINATION_URL = ORIGATO_CHAT_URL


class MessageSendingAccountAccessor(account_accessor.AccountAccessor):
    def __init__(self):
        super(MessageSendingAccountAccessor, self).__init__()
        self.url = DESTINATION_URL
        self.__driver = self.access_account().driver

    def send_summary_to_chat(self, summary):
        top_messages = summary.top_three_messages

        self.send_greeting_message()
        for message in top_messages:
            self.send_message(message)
        self.send_farewell_message()

    def send_greeting_message(self):
        greeting_message = CONFIGS['greeting_message']
        self.send_text_content(greeting_message)

    def send_farewell_message(self):
        farewell_message = CONFIGS['farewell_message']
        self.send_text_content(farewell_message)

    def send_message(self, message):
        self.type_message_meta_information(message)
        if isinstance(message, text_message.TextMessage):
            self.send_text_content(message.text)
        else:
            self.send_media_content(message.media_uri)

    def type_message_meta_information(self, message):
        chat_box = self.find_and_click_on_user_chats_element()
        message_author = message.author
        message_num_of_reacts = message.get_number_of_reacts()

        chat_box.send_keys(
            '*' + message_author + ', ' +
            str(message_num_of_reacts) + ' react' + ('s:' if message_num_of_reacts > 1 else ':') + '*'
        )

    def send_text_content(self, text_content):
        text_content = self.reformat_string(text_content)
        chat_box = self.find_and_click_on_user_chats_element()
        chat_box.send_keys(Keys.SHIFT + Keys.ENTER + Keys.SHIFT + text_content + Keys.ENTER)

    def reformat_string(self, text):
        return text.replace('\n', Keys.SHIFT + Keys.ENTER + Keys.SHIFT)

    def send_media_content(self, media_uri):
        full_media_uri = os.getcwd() + '/' + media_uri

        filename, ext = os.path.splitext(full_media_uri)

        # converting audio mp4's to mp3's
        if ext == '.mp4' and '/audio' in media_uri:
            full_media_uri = filename + '.mp3'
        try:
            add_files_elmnt = self.__driver.find_elements_by_xpath("//*[@class='_n _2__f _4e5e']")[1]
        except:
            self.__driver.refresh()
            add_files_elmnt = self.__driver.find_elements_by_xpath("//*[@class='_n _2__f _4e5e']")[1]
        add_files_elmnt.send_keys(full_media_uri)

        chat_box = self.find_and_click_on_user_chats_element()
        chat_box.send_keys(Keys.ENTER)

        # wait longer for videos to send
        _, ext = os.path.splitext(full_media_uri)
        if ext == '.mp4':
            time.sleep(15)
        else:
            time.sleep(2)

    def find_and_click_on_user_chats_element(self):
        if DESTINATION_URL in GROUP_CHAT_URLS:
            chat_box = self.get_chat_box_from_group_chat()
        elif DESTINATION_URL in INDIVIDUAL_CHAT_URLS:
            chat_box = self.get_chat_box_from_individual_chat()

        ActionChains(self.__driver).move_to_element(chat_box).click(chat_box).perform()

        return chat_box

    def get_chat_box_from_group_chat(self):
        # for group chats, chat box is 2nd text window
        return self.__driver.find_elements_by_xpath("//*[@class='_1mf _1mj']")[1]

    def get_chat_box_from_individual_chat(self):
        # for private chats, chat box is 1st (and only) text window
        return self.__driver.find_elements_by_xpath("//*[@class='_1mf _1mj']")[0]

    def find_and_click_on_chat_element(self):
        raise NotImplementedError

    def find_and_click_on_message_box(self):
        raise NotImplementedError

    def find_and_click_on_message_send_element(self):
        raise NotImplementedError
