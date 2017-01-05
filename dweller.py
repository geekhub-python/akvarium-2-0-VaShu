#!/usr/bin/env python3

from functools import wraps
from random import randint

DWELLER_PREDATOR_EAT = 'RegularFish'
DWELLER_REGULAR_EAT = 'AquaPlant'
DWELLER_COCHLEA_EAT = 'AquaPlant'
DWELLER_PLANT_EAT = 'Oxygen'


def what_eat(*args):
    def eat_decor(f):
        @wraps(f)
        def wrapper(self, prey):
            if prey.__class__.__name__ in args:
                return f(self, prey)
            else:
                return False
        return wrapper

    return eat_decor


class Dweller:  # обитатель

    def __init__(self, weight):
        self.weight = weight
        self.amount_eaten = 0

    def eat(self, dweller):
        self.amount_eaten += 1
        self.weight += dweller.weight

        return True


class RegularFish(Dweller):  # рыба обычная
    MIN_WEIGHT = 1
    MAX_WEIGHT = 9

    def __init__(self, weight):  # используем конструктор
        super().__init__(weight)
        self.weight = weight  # randint(self.MIN_WEIGHT, self.MAX_WEIGHT)
        self.amount_eaten = 0

    @what_eat(DWELLER_REGULAR_EAT)
    def eat(self, eat_prey):
        return super().eat(eat_prey)


class PredatoryFish(Dweller):  # рыба хищник
    PREDATOR_WEIGHT = 10

    def __init__(self, weight, name):  # используем конструктор
        super().__init__(weight)
        self.amount_eaten = 0
        self.name = name
        self.weight = weight  # self.PREDATOR_WEIGHT

    @what_eat(DWELLER_PREDATOR_EAT)
    def eat(self, eat_prey):
        return super().eat(eat_prey)


class AquaCochlea(Dweller):  # улитка
    MIN_WEIGHT = 1
    MAX_WEIGHT = 5

    def __init__(self, weight):
        super().__init__(weight)
        self.weight = randint(self.MIN_WEIGHT, self.MAX_WEIGHT)

    @what_eat(DWELLER_COCHLEA_EAT)
    def eat(self, eat_prey):
        return super().eat(eat_prey)


class AquaPlant(Dweller):  # водоросль
    MIN_WEIGHT = 1
    MAX_WEIGHT = 3

    def __init__(self, weight):
        super().__init__(weight)
        self.weight = randint(self.MIN_WEIGHT, self.MAX_WEIGHT)

    @what_eat(DWELLER_PLANT_EAT)
    def eat(self, fish):
        return super().eat(fish)