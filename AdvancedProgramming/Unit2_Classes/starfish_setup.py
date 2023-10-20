###############################
# Program Name: Starfish Game
# Written By: Mr. Jones
# Date: Oct 2023
# Purpose: In-class practice creating/using objects from classes
#
# Note: Run this game from the terminal with this command:
#   python3 -i starfish_setup.py
#   The game will print out instructions
################################
import random
import time

livingStarfish = []
livingHeros = []

class Starfish:
    
    def __init__(self, starfishName):
        self.swingStrength = random.randint(10,30)
        self.biteStrength = random.randint(10,30)
        self.life = random.randint(100,200)
        self.name = starfishName
        self.isAlive = True
        livingStarfish.append(self)
        print("A new starfish has appeared: ", self.name, ".")
        print("I wonder how strong ",self.name," is???")
    
    def getHurt(self,hp):
        if not self.isAlive:
            print("You can't attack ",self.name,". They're already dead!")
        elif self.life <= hp:
            print("The attack killed ",self.name,"!")
            self.alive = False
            livingStarfish.remove(self)
            if len(livingStarfish) == 0:
                print("all the Starfish are defeated. You won the game!")
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

    def swing(self, target):
        target.getHurt(self.swingStrength)

    def bite(self, target):
        target.getHurt(self.biteStrength)

    def starfishAttack():
        print("-------STARFISH TURN-------")
        
        print("Time for the starfish to strike back")
        #a random vampire will attack a random target
        star = random.choice(livingStarfish)
        target = random.choice(livingHeros)
        time.sleep(1.5)   
        if(random.choice(["swing","bite"]) == "swing"):
            print(star.name, "swings at", target.name)
            time.sleep(1.5)
            target.getHurt(star.swingStrength)
        else:
            print(star.name, "bites", target.name)
            time.sleep(1)
            target.getHurt(star.biteStrength)
        print("-------HERO TURN-------")

class Dragon:
    def __init__(self,thisName):
        self.life = 100
        self.attackStrength = random.randint(10,20)
        self.isAlive = True
        self.name = thisName
        livingHeros.append(self)
        print("A new dragon! Life is ", self.life
              ," and breathFire strength is ", self.attackStrength)

    def breatheFire(self,target):
        if not (self.isAlive):
            print("Um, a dead hero can't attack...")
        elif not(isinstance(target,Starfish)):
            print("You can only attack starfish!")
        else:
            target.getHurt(self.attackStrength)
        Starfish.starfishAttack()
    
    def whatCanYouDo(self):
        print(self.name
              , "has one attack: breatheFire(target) with strength "
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

class Crab:
    def __init__(self,thisName):
        self.life = 100
        self.attackStrength = random.randint(10,20)
        self.isAlive = True
        self.name = thisName
        livingHeros.append(self)
        print("A new Crab! Life is ", self.life
              ," and pinch strength is ", self.attackStrength)

    def whatCanYouDo(self):
        print(self.name
            , "has one attack: pinch(target) with strength "
            , self.attackStrength)

    def pinch(self,target):
        if not (self.isAlive):
            print("Um, a dead hero can't attack...")
        elif not(isinstance(target,Starfish)):
            print("You can only pinch starfish!")
        else:
            target.getHurt(self.attackStrength)
        Starfish.starfishAttack()

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

class Shrimp:
    def __init__(self,thisName):
        self.life = 100
        self.attackStrength = random.randint(10,20)
        self.isAlive = True
        self.name = thisName
        livingHeros.append(self)
        print("A new Shrimp! Life is ", self.life
              ," and punch strength is ", self.attackStrength)

    def whatCanYouDo(self):
        print(self.name
            , "has one attack: punch(target) with strength "
            , self.attackStrength)

    def punch(self,target):
        if not (self.isAlive):
            print("Um, a dead hero can't attack...")
        elif not(isinstance(target,Starfish)):
            print("You can only punch starfish!")
        else:
            target.getHurt(self.attackStrength)
        Starfish.starfishAttack()

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
        elif not(isinstance(target,Starfish)):
            print("You can only attack starfish!")
        else:
            target.getHurt(self.attackStrength)
        Starfish.starfishAttack()

    def healingSpell(self,target):
        if not (self.isAlive):
            print("Um, a dead wizard can't cast a healing spell...")
        else:
            target.getHealed(self.healingStrength)
        Starfish.starfishAttack()

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
print('''welcome to the Starfish Battle Game
here's how to play:
    - first, create your enemy starfish and give them names
        sample syntax:
        patrick = Starfish("Patrick")
    - Second, create your heroes. Your heroes come from these classes:
        + Crab
        + Shrimp
        + Wizard
        + Dragon
        Sample syntax:
        puff = Dragon("puff")
    - Then, start issuing commands to your heroes.   
        Sample syntax:
        puff.breatheFire(patrick)
    - If you forget what a hero can do, you can call the function whatCanYouDo()
        Sample:
        puff.whatCanYouDo()
    - After each hero attack, the starfish will fight back!
      (whatCanYouDo() is a free move, it doesn't count as an attack)
    - The game ends when either all the heroes die or all the starfish die''')


#OPTIONAL SETUP CODE
'''
patrick = Starfish("Patrick")
nova = Starfish("Nova")
puff = Dragon("Puff")
mrcrabs = Crab("MrCrabs")
merlin = Wizard("Merlin")
bubba = Shrimp("Bubba")
'''
