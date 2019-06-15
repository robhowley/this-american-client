
from thisamericanlife.endpoints import get_full_url_template


class TranscriptInstance(object):
    def __init__(self, payload):
        self.payload = payload

    @property
    def episode_number(self):
        return self.payload['episode_number']

    def episode(self):
        from thisamericanlife.models.episode import EpidsodeInstance
        return Epidsodes().get(self.episode_number)


class Transcripts(object):
    def __init__(self, http_client=None):
        self.http_client = http_client
        self._endpoint = get_full_url_template('transcript')

    def get(self, episode_number):
        self.http_client.get(self._endpoint.format(episode_number=episode_number))
