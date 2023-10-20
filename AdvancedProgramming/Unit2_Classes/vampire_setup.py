###############################
# Program Name: Vampire Game
# Written By: Mr. Jones
# Date: Oct 2023
# Purpose: In-class practice creating/using objects from classes
#
# Note: Run this game from the terminal with this command:
#   python3 -i vampire_setup.py
#   The game will print out instructions
################################


import random
import time

livingVamps = []
livingHeros = []

class Vampire:
    
    def __init__(self, vampName):
        self.eatBrainStrength = random.randint(10,30)
        self.suckBloodStrength = random.randint(10,30)
        self.life = random.randint(100,200)
        self.name = vampName
        self.isAlive = True
        livingVamps.append(self)
        print("A new vampire has appeared: ", self.name, ".")
        print("I wonder how strong ",self.name," is???")
    
    def getHurt(self,hp):
        if not self.isAlive:
            print("You can't attack ",self.name,". They're already dead!")
        elif self.life <= hp:
            print("The attack killed ",self.name,"!")
            self.alive = False
            livingVamps.remove(self)
            if len(livingVamps) == 0:
                print("all the vampires are defeated. You won the game!")
                exit(0)
        else: 
            self.life -= hp
            print("Your attack was successful!")
            time.sleep(1.5)
            print("...but",self.name, " still looks fine")
            time.sleep(1.5)


    def getHealed(self, hp):
        if not self.isAlive:
            print("You can't heal ",self.name,". They're already dead!")
        else: 
            self.life += hp
            print("The healing spell worked!")
            print(self.name + "'s remaining life is " , self.life)

    def suckBlood(self, target):
        target.getHurt(self.suckBloodStrength)

    def eatBrain(self, target):
        target.getHurt(self.eatBrainStrength)

    def vampAttack():
        print("-------VAMPIRE TURN-------")
        
        print("Time for the vampires to strike back")
        #a random vampire will attack a random target
        vamp = random.choice(livingVamps)
        target = random.choice(livingHeros)
        time.sleep(1.5)   
        if(random.choice(["blood","brains"]) == "blood"):
            print(vamp.name, "sucks blood from", target.name)
            time.sleep(1.5)
            target.getHurt(vamp.suckBloodStrength)
        else:
            print(vamp.name, "eats the brains of", target.name)
            time.sleep(1)
            target.getHurt(vamp.eatBrainStrength)
        print("-------HERO TURN-------")

class Hunter:
    def __init__(self,thisName):
        self.life = 100
        self.attackStrength = random.randint(10,20)
        self.isAlive = True
        self.name = thisName
        livingHeros.append(self)
        print("A new hunter! Life is ", self.life
              ," and stab strength is ", self.attackStrength)

    def stab(self,target):
        if not (self.isAlive):
            print("Um, a dead hero can't attack...")
        elif not(isinstance(target,Vampire)):
            print("You can only stab vampires!")
        else:
            target.getHurt(self.attackStrength)
        Vampire.vampAttack()
    
    def whatCanYouDo(self):
        print(self.name
              , "has one attack: stab(target) with strength "
              , self.attackStrength)

    def getHurt(self,hp):
        if self.life <= hp:
            print("The attack killed this hero!")
            self.isAlive = False
            livingHeros.remove(self)
            if len(livingHeros) == 0:
                print("All the heros have been defeated. You lost the game!")
                exit(0)
        else: 
            self.life -= hp
            print(self.name + "'s remaining life is " , self.life)

    def getHealed(self, hp):
        if not self.isAlive:
            print("You can't heal ",self.name,". They're already dead!")
        else: 
            self.life += hp
            print("The healing spell worked!")
            print(self.name + "'s remaining life is " , self.life)

class Archer:
    def __init__(self,thisName):
        self.life = 100
        self.attackStrength = random.randint(10,20)
        self.isAlive = True
        self.name = thisName
        livingHeros.append(self)
        print("A new Archer! Life is ", self.life
              ," and arch strength is ", self.attackStrength)

    def whatCanYouDo(self):
        print(self.name
            , "has one attack: arch(target) with strength "
            , self.attackStrength)

    def arch(self,target):
        if not (self.isAlive):
            print("Um, a dead hero can't attack...")
        elif not(isinstance(target,Vampire)):
            print("You can only stab vampires!")
        else:
            target.getHurt(self.attackStrength)
        Vampire.vampAttack()

    def getHurt(self,hp):
        if self.life <= hp:
            print("The attack killed this hero!")
            self.isAlive = False
            livingHeros.remove(self)
            if len(livingHeros) == 0:
                print("All the heros have been defeated. You lost the game!")
                exit(0)
        else: 
            self.life -= hp
            print(self.name + "'s remaining life is " , self.life)

    def getHealed(self, hp):
        if not self.isAlive:
            print("You can't heal ",self.name,". They're already dead!")
        else: 
            self.life += hp
            print("The healing spell worked!")
            print(self.name + "'s remaining life is " , self.life)

class Wizard:
    def __init__(self,thisName):
        self.life = 100
        self.attackStrength = random.randint(10,20)
        self.healingStrength = random.randint(10,20)
        self.isAlive = True
        self.name = thisName
        livingHeros.append(self)
        print("A new Wizard! Life is ", self.life
              ," and attack spell strength is ", self.attackStrength
              ," and healing spell strength is", self.healingStrength)

    def whatCanYouDo(self):
        print(self.name
              , "has two attacks attack: attackSpell(target) with strength "
              , self.attackStrength
              , "and healingSpell(target) with strength"
              , self.healingStrength)

    def attackSpell(self,target):
        if not (self.isAlive):
            print("Um, a dead hero can't attack...")
        elif not(isinstance(target,Vampire)):
            print("You can only stab vampires!")
        else:
            target.getHurt(self.attackStrength)
        Vampire.vampAttack()

    def healingSpell(self,target):
        if not (self.isAlive):
            print("Um, a dead wizard can't cast a healing spell...")
        else:
            target.getHealed(self.healingStrength)
        Vampire.vampAttack()

    def getHurt(self,hp):
        if self.life <= hp:
            print("The attack killed this hero!")
            self.isAlive = False
            livingHeros.remove(self)
            if len(livingHeros) == 0:
                print("All the heros have been defeated. You lost the game!")
                exit(0)
        else: 
            self.life -= hp
            print(self.name + "'s remaining life is " , self.life)

    def getHealed(self, hp):
        if not self.isAlive:
            print("You can't heal ",self.name,". They're already dead!")
        else: 
            self.life += hp
            print("The healing spell worked!")
            print(self.name + "'s remaining life is " , self.life)



###Main
print('''welcome to the vampire game
here's how to play:
    - first, create your enemy vampires and give them names
        sample syntax:
        dracula = Vampire("dracula")
    - Second, create your heroes. Your heroes come from these classes:
        + Wizard
        + Archer
        + Hunter
        Sample syntax:
        sean = Archer("sean")
    - Then, start issuing commands to your heroes.   
        Sample syntax:
        sean.arch(dracula)
    - If you forget what a hero can do, you can call the function whatCanYouDo()
        Sample:
        Sean.whatCanYouDo()
    - After each hero attack, the vampires will fight back!
      (whatCanYouDo() is a free move, it doesn't count as an attack)
    - The game ends when either all the heroes die or all the vampires die''')


#OPTIONAL SETUP CODE
'''
dracula = Vampire("Dracula")
gisela = Vampire("Gisela")
sean = Archer("Sean")
jair = Hunter("Jair")
adam = Wizard("Adam")
'''
