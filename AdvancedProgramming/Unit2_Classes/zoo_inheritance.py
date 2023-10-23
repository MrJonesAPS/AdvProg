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
    def __init__(self, name, mass):

        self.name = name
        self.mass = mass
        #We should read the double underscores
        # as "PLEASE LEAVE ALONE"
        self.__hunger = 100
        self.energy = 50
        

    def eat(self, food):
        self.__hunger -= 20
        print(self.name + " ate some " + food)

    def sleep(self, time):
        self.energy += time
        print(self.name + " slept for " + str(time))

    def createScat(self):
        print("everybody poops")

    def __str__(self):
        return self.name + " is a " \
            + type(self).__name__ \
            + " who weighs " \
            + str(self.mass) + "kg."
    

class Lion(ZooAnimal):
    #Constructor
    def __init__(self, name, mass):
        super().__init__(name, mass)
        

    def roar(self):
        print("roar")

    
class Sloth(ZooAnimal):
    #Constructor
    def __init__(self, name, mass):
        super().__init__(name, mass)

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