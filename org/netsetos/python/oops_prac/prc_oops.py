class Animal:
    _number_of_legs = 0
    _pairs_of_eyes = 0

    def __init__(self, age):
        self._age = age
        print("Animal created")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def print_legs_and_eyes(self):
        print("I have " + str(self._number_of_legs) + " legs and " + str(self._pairs_of_eyes * 2) + " eyes.")

    def print_age(self):
        print("I am " + str(self._age) + " years old.")