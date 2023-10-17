from random import randint
from typing import NamedTuple, Self

from tuple_space.generic_entities import EntityABC

NECTAR = NamedTuple("Nectar", g=int)
HONEY = NamedTuple("Honey", ml=int)


class Flower(EntityABC):
    def __init__(self, name: str, entities: list[Self]):
        super().__init__(name, entities)
        self.out_format = NECTAR
        self.value: NECTAR

    def __call__(self, space):
        self.value = self.out_format(g=randint(1, 5))
        self._put(space)
        print(f"{self.name} produced {self.value.g}g of nectar")


class Bee(EntityABC):
    def __init__(self, name: str, entities: list[Self]):
        super().__init__(name, entities)
        self.in_format = NECTAR
        self.out_format = HONEY
        self.value: NECTAR | HONEY

    def __call__(self, space):
        self._get(space)

        if self.value:
            print(f"{self.name} got {self.value.g}g of nectar")
            self.value = self.out_format(ml=self.value.g * 2)
            self._put(space)
            print(f"{self.name} produced {self.value.ml}ml of honey")


class Bear(EntityABC):
    def __init__(self, name: str, entities: list[Self]):
        super().__init__(name, entities)
        self.in_format = HONEY
        self.value: HONEY
        self.hunger = -1000

    def __call__(self, space):
        self._get(space)

        if self.value:
            print(f"{self.name} eat {self.value.ml}ml of honey")
            self.hunger += self.value.ml

        if self.hunger >= 0:
            raise StopIteration
