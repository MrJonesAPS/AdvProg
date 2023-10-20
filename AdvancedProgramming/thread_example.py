import threading
import time

demandCount = 0

def demand_thread():
    global demandCount
    while(True):
        print("demand!")
        demandCount += 1
        print(demandCount)
        time.sleep(2)


t1 = threading.Thread(target=demand_thread, daemon=True)



'''
while(True):
    print("demand met!")
    demandCount -= 1
    print("new demand count", demandCount)
    time.sleep(5)
'''

def meetDemand():
    global demandCount
    demandCount -= 1
    print("new demand: ", demandCount)

print("starting!")
t1.start()