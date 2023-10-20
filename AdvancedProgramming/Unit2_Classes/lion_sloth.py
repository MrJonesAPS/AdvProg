class Lion:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
    
    def eat(self, food):
        self.hunger -= 5
        print("I ate some " + food + " and now my hunger is " + str(self.hunger))
    
    def roar(self):
        print("Roar")

class Sloth:
    def __init__(self, name):
        self.name = name
        self.energy = 0
    
    def sleep(self, time):
        self.energy += time
        print("I slept for " + time + " seconds and now my energy is " + str(self.energy))
    
    def squeak():
        print("Squeak")


class Zebra:
    def __init__(self, name):
        self.name = name
        self.speed = 50
        self.hunger = 20

    def eat(self, food):
        self.hunger -= 5
        print("I ate some " + food + " and now my hunger is " + str(self.hunger))
    
    def run(self):
        print("i'm running! Wee!")    


simba = Lion("simba")
simba.eat("grass")
simba.roar()
