from dataclasses import dataclass


@dataclass
class Animal:

    name:str
    species:str

    def animInfo(self, name, species):
        self.name = name
        self.species = species
        return self.name, self.species

    def speak(self):
        print("This animal meows/woofs.")


class Dog(Animal):


    def __init__(self, name="", species="", breed=""):
        Animal.__init__(self, name, species)
        self.breed = breed

    # def breed(self, dogBreed):
    #     self.dogBreed = dogBreed
    #     return self.dogBreed

    def speak(self):
        print("Woof!")


class Cat(Animal):


    def __init__(self, name="", species="", color=""):
        Animal.__init__(self, name, species)
        self.color = color

    def speak(self):
        print("Meow!")



# dog = Dog("Max", "Dog", "Golden Retriever")
# cat = Cat("Whiskers", "Cat", "Orange")
#
# print("Dog:")
# print("Name:", dog.name)
# print("Species:", dog.species)
# print("Breed:", dog.breed)
# print("Sound:", end=" ")
# dog.speak()
#
# print("\n")
#
# print("Cat:")
# print("Name:", cat.name)
# print("Species:", cat.species)
# print("Color:", cat.color)
# print("Sound:", end=" ")
# cat.speak()
