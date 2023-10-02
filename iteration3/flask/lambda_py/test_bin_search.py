from unittest import TestCase
from bin_search import lambda_handler as bin_search_lambda_handler
from council_lambda import lambda_handler as council_lambda_handler
from postcode_search import lambda_handler as postcode_lambda_handler

class Test(TestCase):
    def test_bin_lambda_handler_200(self):
        event = {'postcode': '3352'}
        result = bin_search_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_bin_lambda_handler_400(self):
        event = {'postcode': '999'}
        result = bin_search_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)

    def test_council_lambda_handler_200(self):
        # event = {'council': 'Knox City Council'}
        event = {"council": "Knox City Council"}
        result = council_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_council_lambda_handler_404(self):
        event = {'council': 'ggggg'}
        result = council_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 404)

    def test_postcode_lambda_handler_200(self):
        event = {'postcode': '3352'}
        result = postcode_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_postcode_lambda_handler_400(self):
        event = {'postcode': '999'}
        result = postcode_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 400)



