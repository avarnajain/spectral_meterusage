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

    def test_homepage(self):
        response = self.client.get('/')
        data = response.data
        self.assertIn(b'start', data)

    def test_form_submission(self):
        response = self.client.post("/get-data",
                                  data={"start_date": "2019-01-01", "end_date": "2019-01-02"},
                                  follow_redirects=True)
        data = response.data
        self.assertIn(b'my_plot.png', data)

    def test_incorrect_date_submission(self):
        response = self.client.post("/get-data",
                                data={"start_date": "2019-02-02", "end_date": "2019-03-02"},
                                follow_redirects=True)
        self.assertTrue(response.status_code == 404)

    def test_invalid_input(self):
        response = self.client.post("/get-data",
                                data={"start_date": "YY/MM/DD", "end_date": "YY/MM/DD"},
                                follow_redirects=True)
        self.assertTrue(response.status_code == 404)

if __name__ == "__main__":
    unittest.main()
