import math
import random

#random num between 5 and 25
x = 20*random.random()+5

# random num between 5 and 15
x = 10 * random.random() + 5

# random num between -5 and +5
x = 10 * random.random() - 5


#random int
x = random.randint(0,10)


# choose a random from a list
x = random.choice(["heads","tails"],(0.25,0.75))

#x = random.choice(["yes", "no", "maybe", "try again"])

print(x)



