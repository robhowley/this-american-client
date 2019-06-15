
import requests
import thisamericanlife as tal


class HttpClient(object):
    def __init__(self):
        self._base_url = tal.endpoints.BASE_URL

    def _full_url(self, api_path, **kwargs):
        return '/'.join([self._base_url, api_path]).format(**kwargs)

    def get(self, api_path, **kwargs):
        requests.get(self._full_url(api_path, **kwargs))
