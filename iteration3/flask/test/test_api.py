from unittest import TestCase
from api_lambda_py.know_your_area import lambda_handler as know_your_area_lambda_handler
from api_lambda_py.sort_your_trash import lambda_handler as sort_your_trash_lambda_handler


class Test(TestCase):

    def test_know_your_area_lambda_handler_200(self):
        # event = {'council': 'Knox City Council'}
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
        self.assertEqual(result['statusCode'], 200)

    def test_sort_your_trash_lambda_handler_400(self):
        event = {'postcode': '999'}
        result = sort_your_trash_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)

    def test_sort_your_trash_lambda_handler_404(self):
        event = {'postcode': '1000'}
        result = sort_your_trash_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 404)
