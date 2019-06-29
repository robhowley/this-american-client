
from dataclasses import dataclass
from thisamericanlife.models.basemodel import BaseResource
from thisamericanlife.html.episode import EpisodeHtml


class EpisodeInstance(object):
    @staticmethod
    def from_html(html):
        return EpisodeInstance(body_json=EpisodeHtml(html).to_json())

    def __init__(self, body_json=None):
        self.body_json = body_json
        self.episode_metadata = EpisodeMeta.from_raw(self.body_json['episode_title'])


class Episodes(BaseResource):
    def __init__(self, client=None):
        super(Episodes, self).__init__('episode', client=client)

    def get(self, episode_number=None, episode_title=None):
        episode_title = episode_title or self.transcripts.get(episode_number).episode_metadata.title

        return self._get_and_create(EpisodeInstance, episode_number=episode_number, episode_title=episode_title)
