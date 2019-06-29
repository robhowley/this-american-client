
import unittest
from unittest.mock import patch, MagicMock
from thisamericanlife.utils.tests import TestHtmlParsingBase
from thisamericanlife.html.episode import EpisodeHtml


class TestHtmlTranscriptParsing(TestHtmlParsingBase):
    def setUp(self):
        self.html_parser_type = EpisodeHtml

    # @patch('thisamericanlife.html.episode.EpisodeHtml.')
    # def test_to_json(self, mock_extract_transcript, mock_extract_episode_title, *args):
    #     res = self.get_mocked_html_parser().to_json()


if __name__ == '__main__':
    unittest.main()
