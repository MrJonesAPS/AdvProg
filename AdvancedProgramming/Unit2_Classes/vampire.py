
#Vampire(Damage From brainEating, damage from BloodDrinking)
myRange = range(1,2,3)

Bart = Vampire(30, 15)
Alucard = Vampire(35, 20)
Nadja = Vampire(40, 25)

#
Korben = Hunter(10)
Adam = Wizard(15)
Sean = Archer(10)
Jair = Orc(20)
Naser = Wizard(20)

#Vampires strike first
Bart.drinkBlood(Sean) #15
Alocard.eatBrains(Adam) #35
Nadja.drinkBlood(Naser) #25

#we attack the vamps
Korben.stab(Bart) #10
Adam.attackSpell(Alocard) #15 
Sean.arch(Aalocard) #10 
Jair.punch(Alocard) #20
Naser.healSpell(Adam) #20

#vampires attack back
Bart.eatBrains(Jair) #30
Alocard.eatBrains(Jair) #35
Nadja.drinkBlod(Adam) #25

#Heros
Korben.Stab(Alocard) #10
Adam.healSpell(Adam) #15
Sean.arch(Alocard) #10
Jair.punch(Alocard) #20
Naser.healSpell(Jair) #25

#Vampires
Bart.drinkBlood(Korben) #15
Nadja.eatlBrains(Korben) #40

#Heros
Korben.stab(Bart,rage=True) #11 
Adam.healingSpell(Korben) #15
Sean.arch(Nadja) #10
Jair.punch(Naja) #20
Naser.healingSpell(Naser) #25

#Vampires
Bart.eatBrains(Korben) #30

#
Korben.stab(Bart, enrage=True,super=True) #12
Adam.attackSpell(Bart) #15
Sean.arch(Bart, critical=True) #30
Jair.punch(Bart) #30
Naser.