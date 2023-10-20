#import


#functions
def timesTwo():
    global x
    x = x * 2
    

#main
x = int(input("X?"))
y = int(input("Y?"))
x = timesTwo(x)
print(x)