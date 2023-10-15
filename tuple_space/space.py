from random import shuffle
from typing import NamedTuple


class TupleSpace:
    """Based on:
    https://en.wikipedia.org/wiki/Tuple_space
    https://github.com/pSpaces/Programming-with-Spaces/blob/master/tutorial-tuple-spaces.md
    """

    def __init__(self) -> None:
        self._space = list()

    def put(self, item: NamedTuple) -> None:
        self._space.append(item)
        shuffle(self._space)

    def get(self, template: NamedTuple) -> NamedTuple:
        # pop the first item that matches the template

        if len(self) == 0:
            return None

        if template is None:
            # return anything
            return self._space.pop(0)

        for item in self._space:
            if self._match(template, item):
                self._space.remove(item)
                return item

    def query(self, template: NamedTuple) -> NamedTuple:
        # return the first item that matches the template
        for item in self._space:
            if self._match(template, item):
                return item

    def query_all(self, template: NamedTuple) -> NamedTuple:
        # return all items that match the template
        items = list()
        for item in self._space:
            if self._match(template, item):
                items.append(item)
        return items

    def get_all(self, template: NamedTuple) -> NamedTuple:
        # pop all items that matches the template
        items = list()
        for item in self._space:
            if self._match(template, item):
                items.append(item)
                self._space.remove(item)

    def _match(self, template: NamedTuple, item: NamedTuple) -> bool:
        # check if the template fields match the item fields
        return template._fields == item._fields

    def __len__(self):
        return len(self._space)
