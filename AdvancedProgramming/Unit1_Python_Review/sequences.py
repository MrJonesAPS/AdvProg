#a sequence has lots of little parts
#and those parts have an order

myName = "Chris"
myFavoriteThings = ["cats", "food", "music", 3, True]
myRange = range(5)

#access individual items via indexing
#print(myName[2])
#print(myRange[2])

#we can add and delete
#myFavoriteThings.append("school")
#print(myFavoriteThings)

#myFavoriteThings.remove("school")
#print(myFavoriteThings)

#we can slice sequences
#print(myName[2:4])


#more about ranges
myRange = range(2,5,2)
#print(*myRange)


#for x in range(10):
#    print(x)

for thing in myFavoriteThings:
    print("I love", thing)