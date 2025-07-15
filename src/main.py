import unittest

def hello_world(name):
    """
    Returns a greeting message with the given name.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: The greeting message.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not name.strip():
        return "Hello, there!"
    return f"Hello, {name}!"

class TestHelloWorld(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(hello_world("Alice"), "Hello, Alice!")

    def test_empty_string(self):
        self.assertEqual(hello_world(""), "Hello, there!")

    def test_whitespace_string(self):
        self.assertEqual(hello_world("   "), "Hello, there!")

    def test_non_string_type(self):
        with self.assertRaises(TypeError):
            hello_world(123)

    def test_none_value(self):
        with self.assertRaises(TypeError):
            hello_world(None)

if __name__ == '__main__':
    unittest.main()