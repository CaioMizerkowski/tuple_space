from abc import ABC, abstractmethod
from random import randint
from typing import NamedTuple, Self

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

    def _die(self):
        self.entities.remove(self)
        print(f"{self} died")


class GenericConsumer(EntityABC):
    def __init__(self, name: str, entities: list[Self]):
        super().__init__(name, entities)
        self.hungry = 0

    def __call__(self, space):
        self.get(space)
        if self.value:
            print(f"{self.value} consumed by {self}")
            self.hungry = 0
            return

        self.hungry += 1
        if self.hungry > 10:
            self._die()


class GenericProducer(EntityABC):
    def __init__(self, name: str, entities: list):
        super().__init__(name, entities)
        self.format = NamedTuple("A", a=str, b=int)
        self.value: self.format = self.format(a="", b=0)
        self.epochs = 0
        self.sons = 0

    def __call__(self, space):
        self.value = self.format(a="a", b=1)
        self.put(space)
        print(f"{self.value} produced by {self}")
        self.epochs += 1

        if self.epochs > randint(10, 50):
            self.sons += 1
            self.entities.append(
                GenericProducer(f"S{self.sons} of {self}", self.entities)
            )
            self.epochs = 0


class GenericProsumer(EntityABC):
    def __init__(self, name: str, entities: list):
        super().__init__(name, entities)
        self.format = NamedTuple("B", a=str, b=int)
        self.value: self.format = self.format(a="", b=0)
        self.hungry = 0

    def __call__(self, space):
        self.get(space)

        if self.value and self.value.b < 100:
            old_value = self.value
            self.value = self.value._replace(a="b", b=self.value.b + 1)
            self.put(space)
            print(f"{old_value} transformed by {self} in {self.value}")
            self.hungry = 0
            return

        self.hungry += 1
        if self.hungry > 10:
            self._die()


class Eater(GenericConsumer):
    def __call__(self, space):
        self.get(space)
        print(f"{self.value} consumed by {self}")
        try:
            entity = self.entities.pop(0)
            if entity is not self:
                print(f"{entity} consumed by {self}")
            else:
                self.entities.append(self)
        except Exception as e:
            print(e)
