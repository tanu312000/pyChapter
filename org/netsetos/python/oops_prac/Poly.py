class Bear(object):
    def sound(self):
        print("Groarrr")


class Dog(object):
    def sound(self):
        print("Woof woof!")


def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)
#function without body is abstract and the program with abstract function is interface which is not defined in python