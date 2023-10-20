import unittest
from flask import Flask, url_for
from app import app
import json

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client for the app
        self.app.testing = True  # Enable testing mode
        self.headers = {'Authorization': 'Basic Z3Vlc3Q6TVJ6WXBHN3lvblBPOA=='}

    def test_collect_date_api(self):
        json_input = {
            "longitude": 144.962974,
            "latitude": -37.810294,
            "current_date": "2023-10-30",
            "suburb": "Burwood",
            "region": "Victoria",
            "street": "Ardenne Close"
        }

        request = json.dumps(json_input)

        response = self.app.post('/api/rest/collect-date',
                                 headers=self.headers,
                                 json=request)
        print(str(response.data))
        self.assertEqual(response.status_code, 200)