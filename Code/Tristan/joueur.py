from ast import While
import multiprocessing
import time
from utils import *
import os
import sysv_ipc

key = 128
debutkey = 100


md = sysv_ipc.MessageQueue(debutkey)


def wait(value):
    while(value < 3):
        print("You are now in a queue, waiting for at least 3 players to join")
        print("There are currently " + str(value) + " players connected")
        waiting, t = md.receive(type = 1)
        value = int(waiting.decode())

        if t == 1:
            print("New connection detected")
            print("There are now " + str(value) + " players connected")
    print("There are enough players to start the game")
    game()
                     

def game():
    while True:
        pass
    
    
    
    
if __name__ == "__main__":
    print("Hello and Welcome to the Cambiecolo game !")
    print("Your pid will now be sent to the server for you to be in the game")
    try:
        type = int(input("1 for sending pid, else termination : "))
        if type != 1 and type != 2:
            print("Wrong values")
            exit(1)
    except:
        print("An error occured")
        exit(1)
            
    if type == 1:
        md.send(str(os.getpid()).encode(), 0)
        nbjoueur, t = md.receive(type = 1)
        value = int(nbjoueur.decode())
        wait(value)
        
  