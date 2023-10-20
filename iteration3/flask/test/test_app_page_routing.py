import unittest
from flask import Flask, url_for
from app import app

class FlaskAPageRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client for the app
        self.app.testing = True  # Enable testing mode
        self.headers = {'Authorization': 'Basic Z3Vlc3Q6TVJ6WXBHN3lvblBPOA=='}

    # def test_unauthorized_request(self):
    #     response = self.app.get('/')
    #     self.assertEqual(response.status_code, 401)

    def test_authorized_request_index(self):
        response = self.app.get('/', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_collect_date(self):
        response = self.app.get('/collect-date.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_glass_bottle(self):
        response = self.app.get('/glass-bottle.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_find_your_recycler(self):
        response = self.app.get('/find-your-recycler.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_know_your_area(self):
        response = self.app.get('/know-your-area.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_lamp(self):
        response = self.app.get('/lamp.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_lantern(self):
        response = self.app.get('/lantern.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_plastic_bottle(self):
        response = self.app.get('/plastic-bottle.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_plastic_bottle_coin_storage(self):
        response = self.app.get('/plastic-bottle-coin-storage.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_sort_your_trash(self):
        response = self.app.get('/sort-your-trash.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_authorized_request_resources(self):
        response = self.app.get('/resources.html', headers=self.headers)
        self.assertEqual(response.status_code, 200)


