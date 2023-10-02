from unittest import TestCase
from bin_search import lambda_handler as bin_search_lambda_handler
from council_lambda import lambda_handler as council_lambda_handler
from postcode_search import lambda_handler as postcode_lambda_handler

class Test(TestCase):
    def test_bin_lambda_handler(self):
        event = {'postcode': '3352'}
        result = bin_search_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_council_lambda_handler(self):
        # event = {'council': 'Knox City Council'}
        event = {"council": "Knox City Council"}
        result = council_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)

    def test_postcode_lambda_handler(self):
        event = {'postcode': '3352'}
        result = postcode_lambda_handler(event, None)
        self.assertEqual(result['statusCode'], 200)


