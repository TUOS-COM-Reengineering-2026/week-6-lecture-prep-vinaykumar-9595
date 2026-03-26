import unittest
from lecture import randomised_function
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    @patch('lecture.is_small')  # Mock the is_small function
    def test_randomised_function_with_mock1(self, mymock_is_small):
        mymock_is_small.return_value = True  # Set the return value of the mock
        self.assertEqual('software', randomised_function())

    @patch('lecture.is_small')  # Mock the is_small function
    def test_randomised_function_with_mock2(self, mymock_is_small):
        mymock_is_small.return_value = False  # Set the return value of the mock
        self.assertEqual('engineering', randomised_function())
