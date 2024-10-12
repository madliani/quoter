from urllib.parse import unquote


class AuthorPrinter:
    def __init__(self, pages_scraper):
        self.pages_scraper = pages_scraper

    def print_quotes(self):
        page_count = self.pages_scraper.page_count()
        print(f"Список ссылок на персоналии ({page_count}): ")

        for page in self.pages_scraper.all_pages():
            print(f"https://ru.wikiquote.org/wiki{page}")

    def pprint_quotes(self):
        page_count = self.pages_scraper.page_count()
        print(f"Список ссылок на персоналии ({page_count}): ")

        for page in self.pages_scraper.all_pages():
            print(f"https://ru.wikiquote.org/wiki{unquote(page)}")
