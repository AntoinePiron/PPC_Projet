import multiprocessing
import time
from utils import *
import os
import sysv_ipc

key = 128
debutkey = 100
md = sysv_ipc.MessageQueue(debutkey)


mq = sysv_ipc.MessageQueue(key)

def debut(nbjoueur):
    time.sleep(2)
    print("In the game, there are currently %s players"%(nbjoueur))
    if nbjoueur < 3:
        while True:
            print("You will now wait until there are at least 3 players")
            wait, t = md.receive()
            message = wait.decode
            if (message == "debut"):
                print("There are enough players, game will start soon !")
                time.sleep(2)
                break
            
            
if __name__ == "__main__":
    while True:
        
        print("Hello and Welcome to the Cambiecolo game !")
        time.sleep(2)
        print("Your pid will now be sent to the server for you to be in the game")
        try:
            type = int(input("1 for sending pid else termination : "))
            if type != 1 and type != 2:
                print("Wrong values")
                exit(1)
        except:
            print("An error occured")
            exit(1)
        if type == 1:
            pid = str((os.getpid())).encode()
            md.send(pid, 1)
            nbjoueur, t = md.receive()
            value = nbjoueur.decode()
            debut(int(value))
        else:
            exit(1)


    
        
            
            
    
    