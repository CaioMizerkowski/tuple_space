from random import shuffle

from tuple_space.entities.honey_world import Bear, Bee, Flower
from tuple_space.generic_entities import EntityABC
from tuple_space.space import TupleSpace

entities: list[EntityABC] = list()


def main_loop():
    space = TupleSpace()

    while len(entities) > 1:
        shuffle(entities)

        try:
            for entity in entities:
                entity(space)
        except StopIteration:
            break


if __name__ == "__main__":
    entities.append(Flower("Lar", entities))
    entities.append(Flower("Ran", entities))
    entities.append(Flower("Jeira", entities))

    entities.append(Bee("Abe", entities))
    entities.append(Bee("Bel", entities))
    entities.append(Bee("Elha", entities))

    entities.append(Bear("Zé", entities))
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, exiting...")
    finally:
        print(entities)
