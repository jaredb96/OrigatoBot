import unittest, inspect
from chat import react_builder, react


class TestReactBuilder(unittest.TestCase):
    def test_module_creation(self):
        # Make sure class is being created
        self.assertTrue(inspect.isclass(react_builder.ReactBuilder))

    def test_getters_and_setters(self):
        # Test all getter and setters
        item = react_builder.ReactBuilder()
        test_reaction_data_map = {
          'reaction': '\u00f0\u009f\u0091\u008d',
          'actor': 'Alice'
        }
        item.set_reaction_data_map(test_reaction_data_map)
        self.assertEqual(
            test_reaction_data_map,
            item.get_reaction_data_map())

    def test_create_react_object(self):
        # Test the creation of react objects
        item = react_builder.ReactBuilder()
        test_reaction_data_map = {
          'reaction': '\u00f0\u009f\u0091\u008d',
          'actor': 'Alice'
        }
        item.set_reaction_data_map(test_reaction_data_map)
        test_react = react.React('laugh', 'Alice')
        react_to_check = item.create_react_object()
        self.assertEqual(test_react, react_to_check)



