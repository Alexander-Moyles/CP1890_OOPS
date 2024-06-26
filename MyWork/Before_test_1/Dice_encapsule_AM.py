from dataclasses import dataclass
import random


@dataclass
class Die:
    __value: int = 1
    def roll(self):
        self.__value = random.randint(1, 6)

    @property
    def getValue(self):
        return self.__value

class Dice:
    def __init__(self):
        self.__list_die = []

    def addDie(self, die):
        self.__list_die.append(die)

    def rollAll(self):
        for die in self.__list_die:
            die.roll()


    @property
    def read_list(self):
            return tuple(self.__list_die)