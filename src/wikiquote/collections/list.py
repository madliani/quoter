import random

from wikiquote.const.list_error import ListError


class List:
    def __init__(self, lst):
        self._list_ = lst

    def all(self):
        if len(self._list_) == 0:
            raise Exception(ListError.NO_LIST_ITEM)

        yield from self._list_

    def random(self):
        if len(self._list_) == 0:
            raise Exception(ListError.NO_LIST_ITEMS)

        return random.choice(self._list_)

    def length(self):
        return len(self._list_)
