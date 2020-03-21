from. import account_accessor


class MessageSendingAccountAccessor(account_accessor.AccountAccessor):
    def __init__(self):
        pass

    def send_message_to_chat(self, message_content):
        self.access_account()
        self.find_and_click_on_user_chats_element()
        self.find_and_click_on_user_chats_element()
        self.find_and_click_on_message_box()
        self.type_in_message(message_content)
        self.find_and_click_on_message_send_element()

    def find_and_click_on_user_chats_element(self):
        raise NotImplementedError

    def find_and_click_on_chat_element(self):
        raise NotImplementedError

    def find_and_click_on_message_box(self):
        raise NotImplementedError

    def type_in_message(self, message_content):
        raise NotImplementedError

    def find_and_click_on_message_send_element(self):
        raise NotImplementedError