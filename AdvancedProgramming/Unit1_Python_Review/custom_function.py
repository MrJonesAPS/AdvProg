#import statements

#define functions

def introduce():
    print("I am a friendly chat bot")

def hello():
    print("hello")
    introduce()

def sayHi(name):
    print("Hi", name)


#main
hello()
yourName = input("What's your name?")
sayHi(yourName)