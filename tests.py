import unittest
from flask_server import *
from flask_functions import *

# To check test coverage, run the following commands
# coverage run tests.py
# coverage report -m

class TestAPI(unittest.TestCase):
    def setUp(self):
        """Setup client"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test if form is present on homepage"""
        response = self.client.get('/')
        data = response.data
        self.assertIn(b'start', data)

    def test_form_submission(self):
        """Test if successful submission of form returns a plot"""
        response = self.client.post("/get-data",
                                  data={"start_date": "2019-01-01", "end_date": "2019-01-02"})
        data = response.data
        self.assertIn(b'.png', data)

    def test_incorrect_date_submission(self):
        """Test in case data doesnt exist for input dates"""
        response = self.client.post("/get-data",
                                data={"start_date": "2019-02-02", "end_date": "2019-03-02"})
        data = response.data
        self.assertIn(b'No data', data)

    def test_invalid_input(self):
        """Test for invalid date input"""
        response = self.client.post("/get-data",
                                data={"start_date": "YY/MM/DD", "end_date": "YY/MM/DD"})
        data = response.data
        self.assertIn(b'Invalid date', data)

if __name__ == "__main__":
    unittest.main()
