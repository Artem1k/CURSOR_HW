from __future__ import annotations

from typing import Dict, Any


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        pass


class Predator:

    def eat(self, forest: Forest):
        pass


class Herbivorous:

    def eat(self, forest: Forest):
        pass


AnyAnimal = Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator():
    pass


if __name__ == "__main__":
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass


if __name__ == "__main__":
   nature = animal_generator()

   forest = Forest()
   for i in range(10):
       animal = next(nature)
       forest.add_animal(animal)

   while True:
       if not forest.any_predator_left():
           break
       for animal in forest:
           animal.eat(forest=forest)
       time.sleep(1)