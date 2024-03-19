"""
Assignment 2

Classes
"""

from dataclasses import dataclass
from random import randint

# Question 1:
@dataclass
class Person:
    fname: str
    lname: str
    email: str
    
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"


@dataclass
class Customer(Person):
    number: str


@dataclass
class Employee(Person):
    ssn: str


# Question 2:
def rand_int():
    """
    Generates a random integer from 1 to 100
    
    Returns
    -------
    Integer
        A random integer from 1-100.
    """
    return randint(1, 100)

class RandomIntList(list):
    def __init__(self, num=0):
        num = int(num)
        while num > 0:
            self.append(rand_int())
            num -= 1

    @property
    def count(self):
        return len(self)

    @property
    def total(self):
        x = 0
        for i in self:
            x += i
        return x

    @property
    def average(self):
        return float(self.total / self.count)
    
    def __str__(self):
        string = ''
        for i in self:
            string += f'{i}, '
        return string


# Question 4:
class Event:

    def __init__(self, name='', location='', start_date='', end_date=''):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def duration(self):
        return self.end_date - self.start_date

class Conference(Event):
    def __init__(self, name='', location='', start_date='', end_date='', attendees=''):
        Event.__init__(self, name, location, start_date, end_date)

        self.attendees = attendees