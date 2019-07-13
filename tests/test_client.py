import unittest
from unittest.mock import patch
from thisamericanlife.client import ThisAmericanLife


class TestHttpClient(unittest.TestCase):
    @patch('thisamericanlife.client.HttpClient')
    def test_set_client(self, mock_http):
        self.assertEqual(ThisAmericanLife('http').http_client, 'http')
        self.assertEqual(ThisAmericanLife().http_client, mock_http())

    @patch('thisamericanlife.client.tal_models')
    def test_create_transcripts(self, mock_models):
        tal = ThisAmericanLife('http')

        property_res = tal.transcripts
        expected_type = mock_models.transcript.Transcripts
        expected_type.assert_called_once_with(tal)

        self.assertEqual(property_res, expected_type())


if __name__ == '__main__':
    unittest.main()
