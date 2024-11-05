import random

from wikiquote.exception.tuple_item_error import TupleItemError


class Tuple:
    def __init__(self, lst):
        self._list_ = tuple(lst)

    def all(self):
        if len(self._list_) == 0:
            raise TupleItemError()

        yield from self._list_

    def random(self):
        if len(self._list_) == 0:
            raise TupleItemError()

        return random.choice(self._list_)

    def length(self):
        return len(self._list_)
