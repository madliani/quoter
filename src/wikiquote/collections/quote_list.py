import random

from wikiquote.const.exception_message import ExceptionMessage


class QuoteList:
    def __init__(self, quotes):
        self._quotes_ = quotes

    def quotes(self):
        if len(self._quotes_) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        yield from self._quotes_

    def random_quote(self):
        if len(self._quotes_) == 0:
            raise Exception(ExceptionMessage.NO_QUOTES)

        return random.choice(self._quotes_)

    def length(self):
        return len(self._quotes_)
