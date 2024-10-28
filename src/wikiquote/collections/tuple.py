import random

from wikiquote.const.tuple_error import TupleError


class Tuple:
    def __init__(self, lst):
        self._list_ = tuple(lst)

    def all(self):
        if len(self._list_) == 0:
            raise Exception(TupleError.NO_LIST_ITEM)

        yield from self._list_

    def random(self):
        if len(self._list_) == 0:
            raise Exception(TupleError.NO_LIST_ITEMS)

        return random.choice(self._list_)

    def length(self):
        return len(self._list_)
