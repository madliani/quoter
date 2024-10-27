import requests
from bs4 import BeautifulSoup


class AuthorLinkScraper:
    def __init__(self, config):
        self._url_ = config.BASE_URL
        self._category_word_ = config.CATEGORY_WORD

    def fetch(self):
        response = requests.get(self._url_, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        author_link_elements = soup.select("div.mw-category-group ul li a")
        author_links = []

        for author_link_elem in author_link_elements:
            link = author_link_elem.get("href")

            if link and self._category_word_ not in link:
                author_links.append(link)

        return author_links

    def scrape(self):
        html = self.fetch()

        return self.parse(html)
