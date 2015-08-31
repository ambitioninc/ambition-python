import unittest

from mock import patch

from ..api_client import ApiClient
from ..configuration import ApiConfiguration

test_dict = {
    'name': 'Test Name',
    'display_name': 'Test Display Name',
    'data_format': 'Test Format',
}

class TestModel(object):
    def __init__(self):
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'data_format': 'str',
        }
        self.attribute_map = {
            'display_name': 'display_name',
            'name': 'name',
            'data_format': 'data_format',
        }
        self.display_name = None
        self.name = None
        self.data_format = None

class ApiClientTest(unittest.TestCase):
    def setUp(self):
        host = 'http://example.com'
        api_key = 'keyboardcat'
        configuration = ApiConfiguration(host, api_key)
        self.client = ApiClient(configuration=configuration)

    def test_sanitization_for_serialization(self):
        """
        Verify that models are properly cast as dicts
        """
        model = TestModel()
        for key in test_dict.keys():
            setattr(model, key, test_dict[key])
        sanitized_model = self.client.sanitize_for_serialization(model)
        self.assertEqual(sanitized_model, test_dict)

    @patch('ambition.api_client.models')
    @patch('ambition.api_client.RESTClient.GET')
    def test_deserialization_single_model(self, rest_get, models):
        """
        Verify that api responses are cast as the right model type
        """
        rest_get.return_value = test_dict
        models.TestModel = TestModel
        model = self.client.call_api('/fake', 'GET', response='TestModel')
        self.assertIsInstance(model, TestModel)
        self.assertEqual(model.display_name, test_dict.get('display_name'))
        self.assertEqual(model.name, test_dict.get('name'))
        self.assertEqual(model.data_format, test_dict.get('data_format'))

    @patch('ambition.api_client.models')
    @patch('ambition.api_client.RESTClient.GET')
    def test_deserialization_multiple_models(self, rest_get, models):
        """
        Verify that list api responses are model iterators
        """
        serialized_response = [test_dict, test_dict]
        rest_get.return_value = serialized_response
        models.TestModel = TestModel
        response = self.client.call_api('/fake', 'GET', response='TestModel')
        self.assertEqual(len(list(response)), 2)
        for model in response:
            self.assertIsInstance(model, TestModel)
