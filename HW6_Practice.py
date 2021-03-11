# import dataclasses
from abc import ABC, abstractmethod

VEGETABLES = ['Red_tomato', 'Yellow_tomato', 'Cherokee', 'Cherry']
FRUITS = ['Golden', 'Light', 'Green_apple', 'Red_apple']

states = {0: 'nothing', 1: 'flowering', 2: 'green', 3: 'red', 4: 'rotten'}


class GardenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.__vegetables = vegetables
        self.__fruits = fruits
        self.__pests = pests
        self.__gardener = gardener

    def show_the_garden(self):
        print(f'The garden has such vegetable bushes: {self.__vegetables}')
        print(f'Also garden has such fruit trees: {self.__fruits}')
        print(f'And such pests: {self.__pests}')
        print(f'The maintainer of the garden is {self.__gardener}')


'''
@dataclasses.dataclass()
class PlantsStates:
    nothing: int
    flowering: int
    green: int
    red: int
    rotten: int
    '''


class Vegetables(ABC):
    # Here was state in init
    def __init__(self, vegetable_type, name):
        # self.state = state
        self._vegetable_type = vegetable_type
        self._name = name

    @property
    def vegetable_type(self):
        return self._vegetable_type

    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if vegetable_type in VEGETABLES:
            self._vegetable_type = vegetable_type
            # print('all ok')
        else:
            raise Exception(f'There is no such vegetable in the list. '
                            f'Your vegetable: {vegetable_type} and list {VEGETABLES}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')


class Fruits(ABC):
    # Here was state in init
    def __init__(self, fruit_type, name):
        # self.state = state
        self._fruit_type = fruit_type
        self._name = name

    @property
    def fruit_type(self):
        return self._fruit_type

    @fruit_type.setter
    def fruit_type(self, fruit_type):
        if fruit_type in FRUITS:
            self._fruit_type = fruit_type
            # print('all ok')
        else:
            raise Exception(f'There is no such fruit in the list. '
                            f'Your fruit {fruit_type} and list {FRUITS}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('The method is missing.')


class Gardener(ABC):
    def __init__(self, name, plants):
        self._name = name
        self._plants = plants

    @abstractmethod
    def harvest(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def poison_pests(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('The method is missing.')


class Pests(ABC):
    def __init__(self, pests_type, quantity):
        self._pests_type = pests_type
        self._quantity = quantity

    @abstractmethod
    def eat(self, plants):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def poison(self):
        raise NotImplementedError('The method is missing.')


class Tomato(Vegetables):
    instances = []

    def __new__(cls, index, vegetable_type, name):
        if vegetable_type in VEGETABLES:
            return super().__new__(cls)
        raise Exception(f'There is no such vegetable in the list. '
                        f'Your vegetable {vegetable_type} and list {VEGETABLES}')

    def __init__(self, index, vegetable_type, name):
        super().__init__(vegetable_type, name)
        self._index = index
        self._vegetable_type = vegetable_type
        self._state = 0
        Tomato.instances.append(self)

    def __repr__(self):
        return f'({self._index}, {self._vegetable_type}, {self._name})'

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self.print_state()

    def print_state(self):
        print(f'{self._name} {self.vegetable_type} {self._index} is {states[self._state]}')


class TomatoBush:
    def __init__(self, num, vegetable_type, name):
        self._num = num
        self._vegetable_type = vegetable_type
        self._name = name
        self._tomatoes = [Tomato(index, vegetable_type, name) for index in range(1, num + 1)]

    def __iter__(self):
        return iter(self._tomatoes)

    def __repr__(self):
        return f'{self._num} {self._vegetable_type} {self._name}'

    def __del__(self):
        del self

    @property
    def num(self):
        return self._num

    # def __str__(self):
    #     return f'({self.vegetable_type} {self.name})'

    def grow_all(self):
        for tomato in self._tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self._tomatoes])

    def provide_harvest(self):
        self._tomatoes = []
        # self._num = 0

    def pests_eating(self):
        self._tomatoes = []
        self._num = 0


class Apple(Fruits):
    instances = []

    def __new__(cls, index, fruit_type, name):
        if fruit_type in FRUITS:
            return super().__new__(cls)
        raise Exception(f'There is no such fruit in the list. '
                        f'Your fruit {fruit_type} and list {FRUITS}')

    def __init__(self, index, fruit_type, name):
        super().__init__(fruit_type, name)
        self._index = index
        self._fruit_type = fruit_type
        self._state = 0
        Apple.instances.append(self)

    def __repr__(self):
        return f'({self._index}, {self.fruit_type}, {self._name})'

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self.print_state()

    def print_state(self):
        print(f'{self._name} {self.fruit_type} {self._index} is {states[self._state]}')


class AppleTree:
    def __init__(self, num, fruit_type, name):
        self._num = num
        self._fruit_type = fruit_type
        self._name = name
        self._apples = [Apple(index, fruit_type, name) for index in range(1, num + 1)]

    def __iter__(self):
        return iter(self._apples)

    def __repr__(self):
        return f'{self._num} {self._fruit_type} {self._name}'

    def __del__(self):
        del self

    @property
    def num(self):
        return self._num

    # def __str__(self):
    #     return f'({self.fruit_type} {self.name})'

    def grow_all(self):
        for apple in self._apples:
            apple.grow()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self._apples])

    def provide_harvest(self):
        self._apples = []
        # self._num = 0

    def pests_eating(self):
        self._apples = []
        self._num = 0


class StarGardener(Gardener):
    def __init__(self, name, *plants):
        super().__init__(name, plants)
        self._name = name
        self._plants = plants

    def __repr__(self):
        return f'{self._name}'

    def harvest(self):
        print('Gardener is harvesting...')
        for plant in self._plants:
            if plant.all_are_ripe() and plant.num > 0:
                plant.provide_harvest()
                print(f'Harvesting {plant} is finished.')
            elif plant.num == 0:
                print(f'Your {plant} is empty!')
            else:
                print(f'Too early! Your {plant} is not ripe.')

    def handling(self):
        print('Gardener is working...')
        for plant in self._plants:
            plant.grow_all()
        print('Gardner is finished')

    def poison_pests(self, *pests):
        print('Poisoning pests!')
        for pest in pests:
            pest.poison()

    def check_states(self):
        # return all([plant.state == 3 for all_plants in self.plants for plant in all_plants])
        print('Checking states!')
        for all_plants in self._plants:
            for plant in all_plants:
                plant.print_state()


class Pest(Pests):
    def __init__(self, pests_type, quantity):
        super().__init__(pests_type, quantity)
        self._pests_type = pests_type
        self._quantity = quantity

    def __repr__(self):
        return f'{self._quantity} {self._pests_type}'

    def __del__(self):
        del self

    def eat(self, *plants):
        if len(plants) == 0:
            raise Exception('Why did you called pests!')
        if self._quantity > 0:
            print('Pest are eating!')
            for plant in plants:
                plant.pests_eating()

    def poison(self):
        self._quantity = 0


apple_tree_steve = AppleTree(2, 'Golden', 'steve')
tomato_bush_steve = TomatoBush(2, 'Red_tomato', 'steve')
gardener_steve = StarGardener('Steve', apple_tree_steve, tomato_bush_steve)
pests_beetle = Pest('beetle', 1)
fruits_stock = []  #
vegetables_stock = []  #
fruits_stock.append(apple_tree_steve)  #
vegetables_stock.append(tomato_bush_steve)  #
my_garden = Garden(vegetables_stock, fruits_stock, pests_beetle, gardener_steve)

print('\n1. Show the garden\n')
my_garden.show_the_garden()
print('\n2. Steve is checking states\n')
gardener_steve.check_states()
print('\n3. Steve is handling\n')
gardener_steve.handling()
print('\n4. Steve is trying to harvest\n')
gardener_steve.harvest()
print('\n5. Steve is checking states again\n')
gardener_steve.check_states()
print('\n6. Steve is handling again\n')
gardener_steve.handling()
print()
gardener_steve.handling()
print('\n7. Steve is try to handling\n')
gardener_steve.handling()
print('\n8. Showing all the fruits and vegetables\n')
print(Apple.instances)
print(Tomato.instances)
print('\n9. Show the garden\n')
my_garden.show_the_garden()
print('\n10. Pests are eating a tomato\n')
pests_beetle.eat(tomato_bush_steve)
print('\n11. Steve are harvesting\n')
gardener_steve.harvest()
print('\n12. Show the garden\n')
my_garden.show_the_garden()
print('\n13. Steve is poisoning pests\n')
gardener_steve.poison_pests(pests_beetle)
print('\n14. Show the garden\n')
my_garden.show_the_garden()
