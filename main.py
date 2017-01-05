#!/usr/bin/env python3

from random import randint, choice
from aquarium import Aquarium
import dweller

COUNT_ALL_DWELLERS = 100
COUNT_PREDATORS = 2
COUNT_COCHLEA = 3
COUNT_PLANT = 55
COUNT_REGULAR = 40


class SampleError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg

if __name__ == '__main__':
    # создали аквариум, просто один - лучший синглтон
    myAqua = Aquarium()
    try:
        # запустили хищников
        predator_01 = dweller.PredatoryFish(10, 'Anton')
        myAqua.dwellers.append(predator_01)
        predator_02 = dweller.PredatoryFish(10, 'Sam')
        myAqua.dwellers.append(predator_02)
        # запустили обычную рыбу
        for regular in range(COUNT_REGULAR):
            myAqua.dwellers.append(dweller.RegularFish(randint(dweller.RegularFish.MIN_WEIGHT,
                                                               dweller.RegularFish.MAX_WEIGHT)))
        # запустили улиток
        for regular in range(COUNT_COCHLEA):
            myAqua.dwellers.append(dweller.AquaCochlea(randint(dweller.AquaCochlea.MIN_WEIGHT,
                                                               dweller.AquaCochlea.MAX_WEIGHT)))
        # запустили хищников
        for regular in range(COUNT_PLANT):
            myAqua.dwellers.append(dweller.AquaPlant(randint(dweller.AquaPlant.MIN_WEIGHT,
                                                             dweller.AquaPlant.MAX_WEIGHT)))
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
