from unittest import TestCase
import json
from api_lambda_py.know_your_area import lambda_handler as know_your_area_lambda_handler
from api_lambda_py.sort_your_trash import lambda_handler as sort_your_trash_lambda_handler
from api_lambda_py.calendar_db import check_schedule as collect_date_lambda_handler

class TestApiCode(TestCase):

    def test_know_your_area_lambda_handler_200(self):
        event = {"council": "Knox City Council"}
        result = know_your_area_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_know_your_area_lambda_handler_400(self):
        event = {'council': 'avbc'}
        result = know_your_area_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)

    def test_know_your_area_lambda_handler_404(self):
        event = {'council': 'ggggg'}
        result = know_your_area_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 404)

    def test_sort_your_trash_lambda_handler_200(self):
        event = {'postcode': '3352'}
        result = sort_your_trash_lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)

    def test_sort_your_trash_lambda_handler_400(self):
        event = {'postcode': '999'}
        result = sort_your_trash_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)

    def test_sort_your_trash_lambda_handler_404(self):
        event = {'postcode': '1000'}
        result = sort_your_trash_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 404)

    def test_collect_date_lambda_handler_200(self):
        json_input = {
            "longitude": 144.962974,
            "latitude": -37.810294,
            "current_date": "2023-10-20",
            "suburb": "Burwood",
            "region": "Victoria",
            "street": "Ardenne Close"
        }
        # result = collect_date_lambda_handler(json.dumps(json_input))
        result = collect_date_lambda_handler(json_input)
        self.assertEqual(result['statusCode'], 200)

    def test_collect_date_lambda_handler_200_json(self):
        json_input = {
            "longitude": 144.962974,
            "latitude": -37.810294,
            "current_date": "2023-10-20",
            "suburb": "Burwood",
            "region": "Victoria",
            "street": "Ardenne Close"
        }
        result = collect_date_lambda_handler(json.dumps(json_input))
        # print(result)
        #result = collect_date_lambda_handler(json_input)
        self.assertEqual(result['statusCode'], 200)



    def test_collect_date_lambda_handler_400(self):
        json_input = {
            "longitude": 144.962974,
            "latitude": -37.810294,
            "current_date": "2023-10-20",
            "suburb": "Burwood",
            "region": "NSW",
            "street": "Ardenne Close"
        }
        result = collect_date_lambda_handler(json.dumps(json_input))
        self.assertEqual(result['statusCode'], 400)

    def test_collect_date_lambda_handler_404(self):
        json_input = {
            "longitude": 144.962974,
            "latitude": -37.810294,
            "current_date": "2023-10-20",
            "suburb": "gGsgwegs",
            "region": "Victoria",
            "street": "Ardenne Close"
        }
        result = collect_date_lambda_handler(json.dumps(json_input))
        self.assertEqual(result['statusCode'], 404)


