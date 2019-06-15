
from thisamericanlife.http import HttpClient


class ThisAmericanLife(object):
    def __init__(self, http_client=None):
        self._http = http_client or HttpClient()
