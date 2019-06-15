import unittest
from unittest.mock import patch
from thisamericanlife.client import ThisAmericanLife


class TestHttpClient(unittest.TestCase):
    @patch('thisamericanlife.client.HttpClient')
    def test_set_client(self, mock_http):
        self.assertEqual(ThisAmericanLife('http')._http, 'http')
        self.assertEqual(ThisAmericanLife()._http, mock_http())

    @patch('thisamericanlife.client.tal_models')
    def test_create_transcripts(self, mock_models):
        obj = ThisAmericanLife('http').transcripts
        exp_type = mock_models.transcript.Transcripts

        exp_type.assert_called_once_with('http')
        self.assertEqual(obj, exp_type())


if __name__ == '__main__':
    unittest.main()
