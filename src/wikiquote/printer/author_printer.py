from urllib.parse import unquote


class AuthorPrinter:
    def __init__(self, pages_scraper):
        self.author_scraper = pages_scraper

    def print_all(self):
        author_count = self.author_scraper.get_count()
        print(f"Список ссылок на персоналии ({author_count}): ")

        for page in self.author_scraper.get_authors():
            print(f"https://ru.wikiquote.org/wiki{page}")

    def pprint_all(self):
        author_count = self.author_scraper.get_count()
        print(f"Список ссылок на персоналии ({author_count}): ")

        for page in self.author_scraper.get_authors():
            print(f"https://ru.wikiquote.org/wiki{unquote(page)}")
