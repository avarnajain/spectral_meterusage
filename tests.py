import unittest
from flask_server import *
from flask_functions import *

# To check test coverage, run the following commands
# coverage run tests.py
# coverage report -m

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_users(self):
        response = self.client.get('/')
        data = response.data
        self.assertIn(b'start', data) 

if __name__ == "__main__":
    unittest.main()
