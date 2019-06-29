
from thisamericanlife.html.base import BaseHtmlParser


def all_text_of_first_item(el):
    txt = None

    try:
        txt = el[0].text_content().strip()
    except:
        pass

    return txt


class EpisodeHtml(BaseHtmlParser):
    EPISODE_METADATA_PATH = '//div[@id="content"]//header[@class="episode-header"]'

    def _parse_ep_number_and_date(self, el):
        res = dict.fromkeys(['episode_number', 'date_on_air'])

        el_text = all_text_of_first_item(el) or ''

        split_parts = el_text.split(' ')
        if split_parts:
            if split_parts[0].strip().isdigit():
                res['episode_number'] = int(split_parts[0].strip())

            if len(split_parts) > 1:
                res['date_on_air'] = ' '.join(split_parts[1:])

        return res


    def extract_episode_metadata(self):
        header_element = self.document_tree.xpath(EpisodeHtml.EPISODE_METADATA_PATH)[0]

        return dict(
            self._parse_ep_number_and_date(header_element.xpath('.//div[@class="meta"]')),
            title=all_text_of_first_item(header_element.xpath('.//div[@class="episode-title"]')),
            description=all_text_of_first_item(header_element.xpath('.//div[contains(@class,"field-name-body")]'))
        )

    def to_json(self):
        print(self.extract_episode_metadata())
        return dict(
            episode_metadata=self.extract_episode_metadata()
        )
