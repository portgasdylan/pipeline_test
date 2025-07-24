# this is a test file for our main.py file
# imports the libraries we need
import unittest
from main import add

'''Create a test class that will test our app'''
class TextMain(unittest.TestCase):
    '''Lets add three test cases to our test
    class to test the add function'''

    def test_add(self):
        '''Testing this adding two numbers together with the correct result'''
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        '''Testing this adding two numbers together with the correct result'''
        self.assertEqual(add(-1, -2), -3)
    
    def test_add_mixed_numbers(self):
        '''Testing positive and negative numbers together with the correct result'''
        self.assertEqual(add(1, -2), -1)

#start the test runner here
if __name__ == '__main__':
    unittest.main()