from multiprocessing.process import current_process
import os
from multiprocessing import shared_memory
import time
from utils import *

playerID = 0
pid = 0

def updateOffers(numberOfCards, shm):
    shm[playerID-1] = pid.__str__() + ";" + numberOfCards.__str__()

if __name__ == "__main__":
    currentOffers = shared_memory.ShareableList(name="currentOffers")
    pid = os.getpid()
    while True:
        try:
            playerID = int(input("Number of player: "))
            if playerID < 1 or playerID > len(list(currentOffers)) :
                print("Please enter a valid number : [1,%s]"%(len(list(currentOffers))))
                continue
            else:
                if currentOffers[playerID-1] == "0;0":
                    currentOffers[playerID-1] = pid.__str__() + ";0"
                    break
                else:
                    print("Player number already attributed")
                    continue
        except:
            print("Please enter a valid number.")
    while True:
        answer = input("Update offer ? [y/n]")
        answer = answer.lower()
        if answer == "y":
            while True:
                try:
                    cards = int(input("Number of cards : "))
                    if cards < 1 or cards > 5 :
                        print("Please enter a valid number : [1,5]")
                        continue
                    else:
                        updateOffers(cards, currentOffers)
                        break
                except:
                    print("Please enter a valid number.")
        else:
            time.sleep(5)
