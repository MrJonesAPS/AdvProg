# This is a battle against 3 starfish

anders = Starfish(25)
joe = Starfish(25)
sarah = Starfish(25)

# Here's our battle force

gabe = Dragon(50)
owen = Shrimp(5)
nas = Shrimp(10)
cole = Crab(20)
lehiem = wizard(25)

#Here goes the battle
nas.punch(joe)

anders.bite(gabe)

owen.punch(sarah)

sarah.swing(cole)

cole.pinch(sarah)
lehiem.attackSpell(anders)

#anders is dead

joe.swing(cole)
joe.swing(gabe)

nas.punch(sarah)
cole.pinch(joe)
owen.punch(sarah)
gabe.breatheFire(sarah)

#sarah is down to 4 limbs
print(sarah.numLimbs)
print(sarah.howDoing())

Sarah.regenerateLimb()
Joe.bite(lehiem)

nas.punch(sarah)
cole.pinch(joe)
lehiem.healSpell(lehiem)

joe.bite(cole)
sarah.swing(gabe)

gabe.breatheFire(sarah)
lehiem.attackSpell(joe)

#sarah is dead
Joe.swing(gabe)

nas.punch(joe)