
from thisamericanlife.endpoints import get_full_url_template
from thisamericanlife.html.transcript import TranscriptHtml


class TranscriptInstance(object):
    @staticmethod
    def from_html(html):
        return TranscriptInstance(body_json=TranscriptHtml(html).to_json())

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Transcripts(object):
    def __init__(self, http_client=None):
        self.http_client = http_client
        self._endpoint = get_full_url_template('transcript')

    def get(self, episode_number):
        resp = self.http_client.get(self._endpoint.format(episode_number=episode_number))

        return TranscriptInstance.from_html(resp.content)
