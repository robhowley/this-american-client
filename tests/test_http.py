
import unittest
from unittest.mock import patch
from thisamericanlife.http import HttpClient


class TestHttpClient(unittest.TestCase):
    @patch('thisamericanlife.http.requests')
    def test_get(self, mock_requests):
        res = HttpClient().get('some-endpoint/{some}', some='kwarg')

        mock_requests.get.assert_called_once_with('some-endpoint/kwarg')
        mock_requests.get().raise_for_status.assert_called_once()
        self.assertEqual(mock_requests.get(), res)


if __name__ == '__main__':
    unittest.main()
