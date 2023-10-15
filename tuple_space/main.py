from tuple_space.space import TupleSpace
from random import shuffle
from tuple_space.entities import ProducerABC, ConsumerABC, ProsumerABC, EntityABC, Eater

entities: list[EntityABC] = list()

def main_loop():
    space = TupleSpace()
    eaters = 0

    while len(entities) > 1:

        for entity in entities:
            entity(space)

        shuffle(entities)

        if len(space) > 100:
            entities.append(Eater(f"Eater {eaters}", entities))
            eaters += 1



if __name__ == "__main__":
    entities.append(ProducerABC("producer A", entities))
    entities.append(ProducerABC("producer B", entities))
    entities.append(ConsumerABC("consumer A", entities))
    entities.append(ProsumerABC("prosumer A", entities))
    entities.append(ProsumerABC("prosumer B", entities))
    entities.append(ProsumerABC("prosumer C", entities))
    entities.append(ProsumerABC("prosumer D", entities))
    main_loop()
