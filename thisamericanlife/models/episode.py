
from dataclasses import dataclass
from thisamericanlife.models.basemodel import BaseResource
from thisamericanlife.html.transcript import EpisodeHtml


class EpisodeInstance(object):
    @staticmethod
    def from_html(html):
        return EpisodeInstance(body_json=TranscriptHtml(html).to_json())

    def __init__(self, body_json=None):
        self.body_json = body_json
        self.episode_meta_info = EpisodeMeta.from_raw(self.body_json['episode_title'])


class Episodes(BaseResource):
    def __init__(self, client=None):
        super(Episodes, self).__init__('episode', client=client)

    def get(self, episode_number=None, episode_name=None):
        episode_name = episode_name or self.transcripts.get(episode_number).episode_metadata.title

        return self._get_and_create(EpisodeInstance, episode_number=episode_number, episode_name=episode_name)
