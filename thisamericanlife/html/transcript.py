
from lxml import html


class TranscriptHtml(object):
    def __init__(self, html):
        self.html = html

    def to_json(self):
        return html.fromstring(self.html).xpath('//div[@class="act"]')
