
import unittest
from unittest.mock import patch, MagicMock
from thisamericanlife.models.transcript import Transcripts, TranscriptInstance


class TestHttpClient(unittest.TestCase):

    @patch('thisamericanlife.models.transcript.TranscriptInstance')
    @patch('thisamericanlife.models.transcript.get_full_url_template')
    def test_transcripts_get(self, mock_url, mock_instance):
        mock_http = MagicMock()
        res = Transcripts(mock_http).get(1)

        mock_url.assert_called_once_with('transcript')
        mock_http.get.assert_called_once_with(mock_url().format(episode_number=1))
        self.assertEqual(res, mock_instance.from_html(mock_http.get().content))

    @patch('thisamericanlife.models.transcript.TranscriptHtml')
    def test_transcript_instance_from_html(self, mock_transcript_html):
        res = TranscriptInstance.from_html('some-html')
        mock_transcript_html.assert_called_once_with('some-html')
        mock_transcript_html().to_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
