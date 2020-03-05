import unittest
from ya_yeet_logging_stoof_for_jawed import logger
from chat import chat_room, chat_member, message
import datetime


class TestLogger(unittest.TestCase):

    def test_module_creation(self):
        test_item = logger.Logger(chat_room.ChatRoom(), [])
        class_name = 'Logger' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_gen_map_for_chat_data(self):

        test_top_message_1 = message.Message(
            author_name='author1',
            message_id=1,
            text='hello world! 1',
            num_of_reacts=5)
        test_top_message_2 = message.Message(
            author_name='author2',
            message_id=2,
            text='hello world! 2',
            num_of_reacts=3
        )
        test_top_message_3 = message.Message(
            author_name='author3',
            message_id=3,
            text='hello world! 3',
            num_of_reacts=2
        )

        test_chat_member1 = chat_member.ChatMember(
            member_name='author1',
            message_bank=[test_top_message_1]
        )
        test_chat_member2 = chat_member.ChatMember(
            member_name='author2',
            message_bank=[test_top_message_2]
        )
        test_chat_member3 = chat_member.ChatMember(
            member_name='author3',
            message_bank=[test_top_message_3]
        )

        test_top_messages = [
            test_top_message_1,
            test_top_message_2,
            test_top_message_3
        ]
        test_members_list = [
            test_chat_member1,
            test_chat_member2,
            test_chat_member3
        ]

        test_chat_room = chat_room.ChatRoom()
        test_chat_room.set_chat_members(test_members_list)

        test_logger = logger.Logger(test_chat_room, test_top_messages)

        current_timestamp = datetime.datetime.now()
        todays_day = current_timestamp.day
        todays_month = current_timestamp.month
        todays_year = current_timestamp.year
        todays_date = str(todays_month) + ', ' + str(todays_day) + ' ' + str(todays_year)

        num_members_in_chat = 3
        messages_processed = 3
        top_messages_sent = 3

        expected_map = {
            'date executed': todays_date,
            'messages processed': messages_processed,
            'members in chat': num_members_in_chat,
            'number of top messages sent': top_messages_sent
        }

        test_map = test_logger.gen_map_for_chat_data()

        self.assertEqual(test_map, expected_map)

    '''
    log_execution_summary() passes a map to a subroutine in LogWriter
    the map generation is tested in test_gen_map_for_chat_data()
    the subroutine is tested in the TestLogWriter class
    '''
    def test_log_execution_summary(self):
        None

