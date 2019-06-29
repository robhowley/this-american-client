
import unittest
from unittest.mock import patch, MagicMock
from thisamericanlife.models.episode import Episodes, EpisodeInstance


class TestEpisodeModels(unittest.TestCase):

    @patch('thisamericanlife.models.episode.Episodes._get_and_create')
    def test_episodes_get(self, mock_get_create):
        # mock_http = MagicMock()
        kwargs = dict(episode_number=1, episode_name='new-beginnings')
        res = Episodes().get(**kwargs)

        mock_get_create.assert_called_once_with(EpisodeInstance, **kwargs)
        self.assertEqual(res, mock_get_create())

    @patch('thisamericanlife.models.episode.Episodes._get_and_create')
    def test_episodes_get_with_name_looked_up(self, mock_get_create):
        episodes = Episodes(transcripts=MagicMock())

        kwargs = dict(episode_number=1)
        res = episodes.get(**kwargs)

        # self.transcripts.get(episode_number).episode_metadata.title
        episode_title = episodes.transcripts.get(kwargs['episode_number']).episode_metadata.title
        kwargs.update(episode_title=episode_title)

        mock_get_create.assert_called_once_with(EpisodeInstance, **kwargs)
        self.assertEqual(res, mock_get_create())
    #
    # @patch('thisamericanlife.models.transcript.TranscriptInstance')
    # @patch('thisamericanlife.models.transcript.TranscriptHtml')
    # def test_transcript_instance_from_html(self, mock_transcript_html, mock_instance):
    #     res = TranscriptInstance.from_html('some-html')
    #     mock_transcript_html.assert_called_once_with('some-html')
    #     mock_transcript_html().to_json.assert_called_once()
    #     mock_instance.assert_called_once_with(body_json=mock_transcript_html().to_json())
    #     self.assertEqual(mock_instance(), res)


if __name__ == '__main__':
    unittest.main()
