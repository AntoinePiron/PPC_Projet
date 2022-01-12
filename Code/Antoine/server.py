from multiprocessing import shared_memory
import time
from utils import *
import os

if __name__ == "__main__":
    pid = os.getpid()
    print("main pid : ", pid)
    currentOffers = shared_memory.ShareableList(["0;0","0;0","0;0"], name="currentOffers", create=True)
    print(list(currentOffers))
    while True: 
        time.sleep(5)
        print(list(currentOffers))



    
