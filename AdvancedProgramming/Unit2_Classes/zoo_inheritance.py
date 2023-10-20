###############################
# Program Name: Zoo Inheritance
# Written By: Mr. Jones
# Date: Oct 2023
# Purpose: In-class demonstration:
#   + creating classes
#   + Creating objects of classes
#   + Inheritance
#   + Private Variables
################################


#imports


#define classes
class ZooAnimal:
    def __init__(self, name):

        self.name = name
        #PLEASE LEAVE ALONE
        self.__hunger = 100
        self.energy = 50
        print(self)

    def eat(self, food):
        self.__hunger -= 20
        print(self.name + " ate some " + food)

    def sleep(self, time):
        self.energy += time
        print(self.name + " slept for " + str(time))

    def createScat(self):
        print("everybody poops")

    def __str__(self):
        return self.name + " is a " + type(self).__name__

class Lion(ZooAnimal):
    #Constructor
    def __init__(self, name):
        super().__init__(name)
        

    def roar(self):
        print("roar")

    
class Sloth(ZooAnimal):
    #Constructor
    def __init__(self, name):
        super().__init__(name)

    def squeak(self):
        print("squeak")

    
#define functions


#main
duck = Lion("duck")
simba = Lion("simba")

simba.roar()
duck.eat("grass")


sleepy = Sloth("sleepy")
sleepy.squeak()
sleepy.sleep(10)

print("sleepy's hunger is",sleepy._ZooAnimal__hunger)
print("but i'm going to change it")
sleepy._ZooAnimal__hunger = 10
print("now sleepy's hunger is",sleepy._ZooAnimal__hunger)
