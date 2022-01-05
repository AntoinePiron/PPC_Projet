import sys
import multiprocessing
from multiprocessing import Process
from random import random
from utils import Player, Hand

numberOfProcesses = int(input('Please enter number of player : ') )
PlayerArray = []

def GameStart(p_in):
    for _ in range(numberOfProcesses):
        player = Player(  Hand([1,2,3,4,5]) , str(_) )
        PlayerArray.append(player)
        
        with p_in.get_lock():
            p_in.value += 1
                

                
if __name__ == "__main__":
    
    
    p_in = multiprocessing.Value('i', 0, lock=True)
    processes = []
    for i in range(numberOfProcesses):
        processes.append(Process(target=GameStart, args=(p_in)))
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()

    with p_in.get_lock():
        for _ in range(numberOfProcesses):
            print(PlayerArray)