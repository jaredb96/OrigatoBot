import unittest, inspect
from chat import react


class TestReact(unittest.TestCase):
    def test_module_creation(self):
        # Make sure class is being created
        self.assertTrue(inspect.isclass(react.React))

    def test_getters_and_setters(self):
        # Test the simple getters and setters in class.
        item = react.React()
        test_reaction_type = 'upvote'
        test_actor = 'Alice'

        item.set_reaction_type(test_reaction_type)
        item.set_actor(test_actor)

        self.assertEqual('upvote', item.get_reaction_type())
        self.assertEqual('Alice', item.get_actor())


if __name__ == '__main__':
    unittest.main()