from multiprocessing.process import current_process
import os
from multiprocessing import shared_memory
from utils import *

if __name__ == "__main__":
    currentOffers = shared_memory.ShareableList(name="currentOffers")
    pid = os.getpid()
    id = 0
    while True:
        try:
            id = int(input("Number of player: "))
            if id < 1 or id > len(list(currentOffers)) :
                print("Please enter a valid number : [1,%s]"%(len(list(currentOffers))))
            else:
                if currentOffers[id-1] == "0;0":
                    currentOffers[id-1] = pid.__str__() + ";0"
                    break
                else:
                    print("Number already attributed")
        except:
            print("Please enter a valid number.")
    while True:
        pass