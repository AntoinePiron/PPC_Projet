
import time
from utils import *
import os
import sysv_ipc
from multiprocessing import shared_memory



playerID = 0
pid = 0

key = 128 # Declaration of the key for the message queues
debutkey = 100 #Could be passed to console args ?

Pid = os.getpid

def updateOffers(numberOfCards, shm):
    shm[playerID-1] = pid.__str__() + ";" + numberOfCards.__str__()

#Fonction self-explainatory, waits for enough ppl to join the game
def wait(value, md):
    while(value < 3):
        print("You are now in a queue, waiting for at least 3 players to join")
        print("There are currently " + str(value) + " players connected")
        waiting, t = md.receive(type = 2)  # Waits for connection ack type messages
        value = int(waiting.decode()) 

        if t == 1: # If a connection type message is detected, update the number of player in the game
            print("New connection detected")
            print("There are now " + str(value) + " players connected")
        
    #If there are more than 3 players, breaks the loop   
    print("There are enough players to start the game")
    print("Sending a acceptation message")
    
    md.send(str(1).encode(),type = 3)   #Sends a type 3 message, to ack the start of the game
    
    print("Starting game")
    game()
                     
#Fonction game, placeholder for now
def game():
    Antoine()
    
    
    #Handle the joining the server, and sending the process' pid
def joinserver(pid):
    print("Hello and Welcome to the Cambiecolo game !")
    
    try: #Will try to join an existing debut queue, starting connnection if succesful 
        md = sysv_ipc.MessageQueue(debutkey)
        print("Your pid will now be sent to the server for you to be in the game")
        try: #Ask player to send its pid, easy stuff
            type = int(input("1 for sending pid, pressing another key will result in termination : "))
            if type != 1 and type != 2:
                print("Wrong values")
                exit(1)
        except:
            print("An error occured")
            exit(1)
            
        if type == 1: #IF user,types one, sends pid to server, than wait for ack of connection
            md.send(str(pid).encode(), type = 1)
            nbjoueur, t = md.receive(type = 2)
            value = int(nbjoueur.decode()) #Receive ack, with value being the number of player already connected
            wait(value, md)
            
    except sysv_ipc.ExistentialError:     #If the debut MessageQueue is not found, exits the process
        print("Could no connect to server")
        print("Either server not launched, or game already staarted")
        print("Exiting")
        exit(1)

#Fonction qui bah est ton code pelo mdr
def Antoine():
    mq = sysv_ipc.MessageQueue(key) #Joins the main message queue
    
    memorycreated, t = mq.receive(type = 1) #Waits for an ack that the shared memory has been created
    created = memorycreated.decode()
    
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

if __name__ == "__main__":
    joinserver(Pid)
    
  