import unittest
from mock import patch, MagicMock


class RestClientObjectTest(unittest.TestCase):
    def setUp(self):
        pass

    @patch('ambition.rest.RESTClientObject.agent')
    def test_content_types(self, rest_agent):
        """
        Verify that the rest client supports the extended set of content types
        """
        request_mock = MagicMock(return_value=MagicMock(status=200, data=''))
        rest_agent.return_value.request = request_mock
        from ..rest import RESTClient
        test_headers = {
            'Content-Type': 'application/vnd.ms-excel'
        }
        RESTClient.POST('fake_url', headers=test_headers)
        request_mock.assert_called_with(
            'POST', 'fake_url', body=None, headers=test_headers)


    @patch('ambition.rest.RESTClientObject.agent')
    def test_get_query_params(self, rest_agent):
        """
        Verify that the rest client supports the extended set of content types
        """
        request_mock = MagicMock(return_value=MagicMock(status=200, data=''))
        rest_agent.return_value.request = request_mock
        from ..rest import RESTClient
        query_params = {'foo': 'bar'}
        RESTClient.GET('fake_url', query_params=query_params)
        request_kwargs = {
            'fields': query_params,
            'headers': {
                'Content-Type': 'application/json',
            },
        }
        request_mock.assert_called_with('GET', 'fake_url', **request_kwargs)
