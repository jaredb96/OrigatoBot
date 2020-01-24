"""
test_json_reader.py - Unit test class for message container class.
@author: Jared Barrow
"""
from web import json_reader
import unittest
import inspect


class TestJsonReader(unittest.TestCase):
    def test_module_creation(self):
        """
        desc: Tests that the chat_scraper class is actually a class.
        """
        test_item = json_reader.JsonReader()
        class_name = 'JsonReader' == test_item.__class__.__name__
        self.assertTrue(class_name)

    def test_all_getters_and_setters(self):
        test_item = json_reader.JsonReader()
        test_json = open('test_json_file.json')
        test_item.set_json_file(test_json)
        self.assertEqual(test_json, test_item.get_json_file())

        test_members_names = ['Alice', 'Bob', 'Carol']
        test_item.set_member_names(test_members_names)
        self.assertEqual(
            test_members_names,
            test_item.get_member_names())

        test_names_to_message_data = {
            'Alice': [1, 'Test1', 3],
            'Bob': [2, 'Test2', 1],
            'Carol': [3, 'Test3', 0]}
        test_item.set_name_to_message_data_map(
            test_names_to_message_data)
        self.assertEqual(
            test_names_to_message_data,
            test_item.get_name_to_message_data_map())
        test_json.close()

    def test_make_json_data_map(self):
        test_item = json_reader.JsonReader()
        test_json = open('test_json_file.json')
        test_item.set_json_file(test_json)
        check_map = {
            'Alice': [
                (1572995131170, 'Hello', 1),
                (1572993597519, 'I agree.', 0)],
            'Bob': [(1572993597519, 'This is nice', 0)],
            'Carol': [],
            'Dan': [(1572994091161, 'Hello World!', 0)],
            'Edgar': [(1572994272138, 'Hi Alice', 3)],
            'Frank': [(1572994272138, 'Nice weather', 3)],
            'George': [(1572994091161, 'True', 0)],
            'Harry': [(1572995131170, 'It is', 1)]}
        self.assertEqual(check_map, test_item.make_json_data_map())
        test_json.close()








