from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import time
import random
import uuid


class Animal(ABC):

    def __init__(self, id, power: int, speed: int):
        self.id = id
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError

    def _strength_restores(self):
        self.current_power *= 1.5
        if self.current_power > self.max_power:
            self.current_power = self.max_power

    def _strength_loses(self):
        self.current_power *= 0.7
        if self.current_power < 0:
            self.current_power = 0


class Predator(Animal):

    def __init__(self, id, power, speed):
        super().__init__(id, power, speed)

    def eat(self, forest: Forest):
        food = forest.animals.get(random.choice(list(forest.animals.keys())))
        while food.current_power == 0:
            food = forest.animals.get(random.choice(list(forest.animals.keys())))
        if self.id == food.id:
            print('he was unlucky and he was left without a dinner')
        else:
            print('tries to catch up')
            if self.speed > food.speed and self.current_power > food.current_power:
                print('Predators eats')
                self._strength_restores()
                food.current_power = 0
            else:
                print('Predator is unlucky')
                self._strength_loses()
                food._strength_loses()


class Herbivorous(Animal):

    def __init__(self, id, power, speed):
        super().__init__(id, power, speed)

    def eat(self, forest: Forest):
        print('Herbivorous is eating')
        self._strength_restores()


AnyAnimal = Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def __iter__(self):
        return list(self.animals.values())

    def add_animal(self, animal: AnyAnimal):
        self.animals[str(animal.id)] = animal

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(str(animal.id))


def animal_generator(quantity):
    item = 0
    while item < quantity:
        item += 1
        yield random.choice(AnyAnimal)(uuid.uuid4(), random.randint(25, 100), random.randint(25, 100))


if __name__ == "__main__":
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
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
