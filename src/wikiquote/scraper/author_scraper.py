import random

import requests
from bs4 import BeautifulSoup


class AuthorScraper:
    def __init__(self, config):
        self.url = config.BASE_URL
        self.category_word = config.CATEGORY_WORD
        self.authors = []

    def fetch(self):
        response = requests.get(self.url, timeout=1)
        response.raise_for_status()

        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        author_links = soup.select("div.mw-category-group ul li a")

        for author_link in author_links:
            link = author_link.get("href")

            if link and self.category_word not in link:
                self.authors.append(link)

    def scrape(self):
        html = self.fetch()
        self.parse(html)

    def get_authors(self):
        yield from self.authors

    def get_author(self, index):
        if len(self.authors) > 0:
            return self.authors[index]

        raise Exception("No author!")

    def get_random_author(self):
        return random.choice(self.authors)

    def get_count(self):
        return len(self.authors)
