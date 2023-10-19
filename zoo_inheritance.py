#imports


##WARMUP:
# Add one more function to ZooAnimal 
# that each other class will inherit

#define classes
class ZooAnimal:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.energy = 50
        print(self)

    def eat(self, food):
        self.hunger -= 20
        print(self.name + " ate some " + food)

    def sleep(self, time):
        self.energy += time
        print(self.name + " slept for " + str(time))

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
