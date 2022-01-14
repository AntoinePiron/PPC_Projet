from ast import While
import multiprocessing
import time
from utils import *
import os
import sysv_ipc

key = 128
debutkey = 100
Pid = os.getpid



def wait(value, md):
    while(value < 3):
        print("You are now in a queue, waiting for at least 3 players to join")
        print("There are currently " + str(value) + " players connected")
        waiting, t = md.receive(type = 1)
        value = int(waiting.decode())

        if t == 1:
            print("New connection detected")
            print("There are now " + str(value) + " players connected")
    print("There are enough players to start the game")
    print("Sending a acceptation message")
    
    md.send(str(1).encode(),type = 2)
    
    print("Starting game")
    game()
                     
#Fonction game, placeholder for now
def game():
    while True:
        pass
    #Handle the joining the server, and sending the process' pid
    
    
    
def joinserver(pid):
    print("Hello and Welcome to the Cambiecolo game !")
    try: #Will try to join an existing debut queue, starting connnection if succesful 
        md = sysv_ipc.MessageQueue(debutkey)
        print("Your pid will now be sent to the server for you to be in the game")
        try:
            type = int(input("1 for sending pid, pressing another key will result in termination : "))
            if type != 1 and type != 2:
                print("Wrong values")
                exit(1)
        except:
            print("An error occured")
            exit(1)
            
        if type == 1:
            md.send(str(pid).encode())
            nbjoueur, t = md.receive(type = 1)
            value = int(nbjoueur.decode())
            wait(value, md)
    except sysv_ipc.ExistentialError:     
        print("Could no connect to server")
        print("Either server not launched, or game already staarted")
        print("Exiting")
        exit(1)
    
if __name__ == "__main__":
    joinserver(Pid)
    
  