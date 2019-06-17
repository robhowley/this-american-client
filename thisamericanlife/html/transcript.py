
from lxml import html


def get_header_text(el):
    return el.xpath('string(./*[self::h1 or self::h2 or self::h3 or self::h4]/text())')


def get_lines(el):
    return [dict(begin=ln.get('begin'), line=ln.text) for ln in el.xpath('./*[@begin]')]


def _get_act_lines(act_content):
    return [
        dict(speaker_lines, speaker=speaker_block.get('class'))
        for speaker_block in act_content
        for speaker_lines in get_lines(speaker_block)
    ]


class TranscriptHtml(object):
    EPISODE_TITLE_PATH = '//div[@id="content"]//header'
    ACT_PATH = '//div[@class="act"]'
    ACT_SCRIPT_PATH = './div[@class="act-inner"]/div'

    def __init__(self, html):
        self.html = html

    def to_json(self):
        html_tree = html.fromstring(self.html)

        episode_info = html_tree.xpath(TranscriptHtml.EPISODE_TITLE_PATH)
        acts = html_tree.xpath(TranscriptHtml.ACT_PATH)

        return dict(
            episode_title=get_header_text(episode_info[0]) if episode_info else None,
            transcript=[
                dict(
                    transcript_line,
                    act_number=i,
                    act_id=act.get('id'),
                    act_title=get_header_text(act),
                )
                for i, act in enumerate(acts, start=1)
                for transcript_line in _get_act_lines(act.xpath(TranscriptHtml.ACT_SCRIPT_PATH))
            ]
        )
