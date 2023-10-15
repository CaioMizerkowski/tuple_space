from typing import Any, NamedTuple, Self
from abc import ABC, abstractmethod
from tuple_space.space import TupleSpace


class EntityABC(ABC):
    def __init__(self, name: str, entities: list[Self]):
        self.format: NamedTuple = None
        self.value: self.format | None = None
        self.name = name
        self.entities = entities

    @abstractmethod
    def __call__(self, space: TupleSpace):
        pass

    def put(self, space: TupleSpace):
        space.put(self.value)

    def get(self, space: TupleSpace):
        self.value = space.get(self.format)
        if self.value is None:
            print(f"{self.name} failed to get {self.format}")

    def __str__(self) -> str:
        return self.name


class ConsumerABC(EntityABC):
    def __call__(self, space):
        self.get(space)
        print(f"{self.value} consumed by {self}")


class ProducerABC(EntityABC):
    def __init__(self, name: str, entities: list):
        super().__init__(name, entities)
        self.format = NamedTuple("A", a=str, b=int)
        self.value: self.format = self.format(a="", b=0)

    def __call__(self, space):
        self.value = self.format(a="a", b=1)
        self.put(space)
        print(f"{self.value} produced by {self}")


class ProsumerABC(EntityABC):
    def __init__(self, name: str, entities: list):
        super().__init__(name, entities)
        self.format = NamedTuple("B", a=str, b=int)
        self.value: self.format = self.format(a="", b=0)

    def __call__(self, space):
        self.get(space)
        if self.value:
            old_value = self.value
            self.value = self.value._replace(a="b", b=self.value.b + 1)
            self.put(space)
            print(f"{old_value} transformed by {self} in {self.value}")

class Eater(ConsumerABC):
    def __call__(self, space):
        self.get(space)
        print(f"{self.value} consumed by {self}")
        try:
            entity = self.entities.pop(0)
            print(f"{entity} consumed by {self}")
        except Exception as e:
            print(e)
