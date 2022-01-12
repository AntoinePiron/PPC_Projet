from multiprocessing.process import current_process
import os
from multiprocessing import shared_memory
from utils import *

if __name__ == "__main__":
    currentOffers = shared_memory.ShareableList(name="currentOffers")
    pid = os.getpid()
    print("player pid :  ", pid)
    currentOffers[0] = pid.__str__() + ";3"

    currentOffers.shm.close()