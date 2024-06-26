from dataclasses import dataclass


class Fruit:
    __slots__ = ["name", "calories"]
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'This is a {self.name} with {self.calories} calories.'


banana = Fruit('Banana', 10)
banana2 = Fruit('Banana', 10)
apple = Fruit('Apple', 20)

print(apple.calories)

@dataclass(frozen=True)(slots=True)
class FruitD:
    name: str
    calories: float


bananad = FruitD('Banana', 10)
banana2d = FruitD('Banana', 10)
appled = FruitD('Apple', 20)

print(appled.calories)

print(banana == banana2)
print(bananad == banana2d)

print(apple)
print(appled)

try:
    bananad.calories = 60
except:
    print("@dataclass in frozen")
finally:
    print(bananad.calories)
