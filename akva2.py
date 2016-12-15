#!/usr/bin/env python3

from random import randint, choice
from functools import wraps

COUNT_ALL_DWELLERS = 100
COUNT_PREDATORS = 2
COUNT_COCHLEA = 3
COUNT_PLANT = 55
COUNT_REGULAR = 40

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


class SampleError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg


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


class Aquarium:
    MIN_NUMBER = 20
    MAX_NUMBER = 100

    def __init__(self):
        # Как аквариум может знать хищная рыба это или нет? ето не его отвественность
        self.dwellers = []


if __name__ == "__main__":
    # создали аквариум, просто один - лучший синглтон
    myAqua = Aquarium()
    try:
        # запустили хищников
        predator_01 = PredatoryFish(10, 'Anton')
        myAqua.dwellers.append(predator_01)
        predator_02 = PredatoryFish(10, 'Sam')
        myAqua.dwellers.append(predator_02)
        # запустили обычную рыбу
        for regular in range(COUNT_REGULAR):
            myAqua.dwellers.append(RegularFish(randint(RegularFish.MIN_WEIGHT, RegularFish.MAX_WEIGHT)))
        # запустили улиток
        for regular in range(COUNT_COCHLEA):
            myAqua.dwellers.append(AquaCochlea(randint(AquaCochlea.MIN_WEIGHT, AquaCochlea.MAX_WEIGHT)))
        # запустили хищников
        for regular in range(COUNT_PLANT):
            myAqua.dwellers.append(AquaPlant(randint(AquaPlant.MIN_WEIGHT, AquaPlant.MAX_WEIGHT)))
        # Raise an exception with argument

        qqq = 100
        if len(myAqua.dwellers) > COUNT_ALL_DWELLERS:
            raise SampleError

    except SampleError('Dwellers more than is necessary'):
        # Catch the custom exception
        print('This is a CustomError')

    # цикл поедания
    print("Congratulations! All is correctly.")
    while len(myAqua.dwellers) > COUNT_PREDATORS + COUNT_COCHLEA:
        dweller_eater = choice(myAqua.dwellers)
        dweller_prey = choice(myAqua.dwellers)

        if dweller_eater.eat(dweller_prey):
            number_prey = myAqua.dwellers.index(dweller_prey)
            del myAqua.dwellers[number_prey]

        # проверяем если едок - обычная рыба, а жертва - хищник, то делаем обратку.
        # Хищник поедает обычную рыбу
        if (dweller_eater.__class__.__name__ == 'RegularFish' and dweller_prey.__class__.__name__ == 'PredatorFih'):
            dweller_prey.eat(dweller_eater)
            number_regular = myAqua.dwellers.index(dweller_eater)
            del myAqua.dwellers[number_regular]

    # вывод результатов
    # myAqua.dwellers.sort(key=lambda dweller: dweller.weight, reverse=True)
    # for fin in myAqua.dwellers:
    # or
    finalists = sorted(myAqua.dwellers, key=lambda dweller: dweller.weight, reverse=True)
    for finalist in finalists:
        print(finalist.__class__.__name__ + " \"" + "\", weight: " + str(
            finalist.weight) + ", amount_eaten: " + str(finalist.amount_eaten))
