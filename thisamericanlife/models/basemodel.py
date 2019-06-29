
from thisamericanlife.endpoints import get_full_url_template


class BaseResource(object):

    def __init__(self, path_name, client=None):
        self.client = client
        self._endpoint = get_full_url_template(path_name)

    def _get_and_create(self, instance_type, **kwargs):
        resp = self.client.http_client.get(self._endpoint.format(**kwargs))

        return instance_type.from_html(resp.content)
