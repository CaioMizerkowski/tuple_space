from random import shuffle

from tuple_space.entities import (
    Eater,
    EntityABC,
    GenericConsumer,
    GenericProducer,
    GenericProsumer,
)
from tuple_space.space import TupleSpace

entities: list[EntityABC] = list()


def main_loop():
    space = TupleSpace()
    eaters = 0

    while len(entities) > 1:
        shuffle(entities)
        for entity in entities:
            entity(space)

        if len(space) > 500:
            entities.append(Eater(f"Eater {eaters}", entities))
            eaters += 1


if __name__ == "__main__":
    entities.append(GenericProducer("producer A", entities))
    entities.append(GenericProducer("producer B", entities))
    entities.append(GenericConsumer("consumer A", entities))
    entities.append(GenericProsumer("prosumer A", entities))
    entities.append(GenericProsumer("prosumer B", entities))
    entities.append(GenericProsumer("prosumer C", entities))
    entities.append(GenericProsumer("prosumer D", entities))
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected, exiting...")
    finally:
        print(entities)
