import pickle
from utils import *
import os
import sysv_ipc
from multiprocessing import shared_memory
import signal
import sys
import time

global playerID 
playerPID = os.getpid()
key = 128 # Declaration of the key for the message queues
debutkey = 100 #Could be passed to console args ?
semKey = 256
myHand = Hand([0,0,0,0,0])


    

    #Handle the joining the server, and sending the process' pid
def joinserver(pid):
    print("Hello and Welcome to the Cambiecolo game !")
    
    try: #Will try to join an existing debut queue, starting connnection if succesful 
        md = sysv_ipc.MessageQueue(debutkey)
        print("Your pid will now be sent to the server for you to be in the game")
        type = checkInput(1,1,"1 for sending pid, pressing another key will result in termination : ")
        if type != 1:
            print("Leaving game")
            exit(0)    
        else: #IF user,types one, sends pid to server, than wait for ack of connection
            md.send(str(pid).encode(), type = 1)
            nbjoueur, t = md.receive(type = 2)
            value = int(nbjoueur.decode()) #Receive ack, with value being the number of player already connected
            wait(value, md)          
    except sysv_ipc.ExistentialError:     #If the debut MessageQueue is not found, exits the process
        print("Could no connect to server")
        print("Either server not launched, or game already staarted")
        print("Exiting")
        exit(1)

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
    while True:
        flag = checkInput(1,2,"Enter 1 to start game, 2 to wait for another player ")
        if (flag == 1):
            print("You will now all wait for all players to accept the start of the game")
            md.send(str(1).encode(),type = 3)   #Sends a type 3 message, to ack the start of the game
        if (flag == 2):
            print("Waiting for all players to send their choice...")
            md.send(str(2).encode(),type = 3)
            
        start, t = md.receive(type = 4)
        value = int(start.decode())
        if (value == 1):
            print("Game starting")
            break
        else:
            print("Someone decided to wait")
            waiting, t = md.receive(type = 2)  # Waits for connection ack type messages
            value = int(waiting.decode()) 
            print("New connection detected")
            print("There are now " + str(value) + " players connected")
            continue
        
        

def receiveHands():
    print("Receiving hand ...")
    global mq
    mq = sysv_ipc.MessageQueue(key)
    byteHand, _ = mq.receive(type = os.getpid())
    global myHand
    myHand = pickle.loads(byteHand)
    print("Hand received")

#Fonction qui bah est ton code pelo mdr
def TrackingCurrentOffers():
    currentOffers = shared_memory.ShareableList(name="currentOffers")
    offersSemaphore = sysv_ipc.Semaphore(semKey)
    pid = os.getpid()
    playerID = 0
    for i in range(len(list(currentOffers))):
        offersSemaphore.acquire()
        if currentOffers[i] == "0;0" and playerID == 0:
            playerID = i + 1
            currentOffers[i] = pid.__str__() + ";0" 
            print("Your player id is " + str(playerID) + " for this game")
        offersSemaphore.release()
  
    
    while True:       
        choice = checkInput(1,3,"Enter 1 to propose an offer, 2 to choose from an existing offer, 3 if you think you won ! : ")
        if choice == 1:
            offer = checkInput(1,5,"Number of cards in [1,5]: ")
            offersSemaphore.acquire()
            currentOffers[playerID-1] = pid.__str__() + ";" + offer.__str__()
            offersSemaphore.release()
            offersent(offer)   
        if choice == 2:
            print("The offers list is : %s"%(list(currentOffers)))
            offer= int(input("Choice the number of the offer you want to accept : "))  
            cardnumber = int(currentOffers[offer -1].partition(';')[2])
            tradePID = int(currentOffers[offer -1].partition(';')[0])
            print(cardnumber + tradePID)     
            offeracepted(cardnumber, tradePID)
        if choice == 3: #J'ai testé ta méthode mais ça marche pas :(
            a = 0
            for i in range(5):
                if myHand.getCard(0) == myHand.getCard(i):
                    a = a +1
            if a == 5:
                mq.send(str(1).encode(),type = 1)
            else:
                print("Your hand is not a winning")
            
                


def offersent(offer):
    mq = sysv_ipc.MessageQueue(key) #Joining main message queue
    HisHand = Hand([0] * 5)
    accept, _ = mq.receive(type = playerPID)
    traderPID = int(accept.decode())
    print("Someone accepted your offer ! You now need to choose what cards to send")
    for i in range(offer):
        while True:
            card = checkInput(1,5,"Choose the nomber of the card you want to send in [1,5] : ")
            if myHand.getCard(card-1) == 0:
                print("You have chosen a card you already sent... thats not very nice, please choose another.")
                continue
            else:
                mq.send(str(myHand.getCard(card-1)).encode(), type = traderPID)
                myHand.setCard(0, card-1)
                break 
    print("Cards sent ! waiting for reply")
    for i in range(offer):
        cardreceived, _ = mq.receive(type = playerPID)
        HisHand.setCard(int(cardreceived.decode()), i)
    print("Hand received ! Adding it to your own hand")
    myHand.fuzeHands(HisHand.myHand)       
    print("Your hand is now " +  myHand.__str__())
    #On pense à remettre les offres à zérp 
    currentOffers = shared_memory.ShareableList(name="currentOffers")
    offersSemaphore = sysv_ipc.Semaphore(semKey)
    offersSemaphore.acquire()
    currentOffers[playerPID-1] = (os.getpid()).__str__() + ";0"
    offersSemaphore.release()

    
def offeracepted(offer, traderPID):
    mq = sysv_ipc.MessageQueue(key) #Joining main message queue
    print("You have accepted an offer, the player will soon send it to you")
    HisHand = Hand([0] * 5)
    mq.send(str(playerPID).encode(), type = traderPID)
    for i in range(offer):
        card, t = mq.receive(type = playerPID)     
        cardnum = int(card.decode())
        HisHand.setCard(cardnum, i)
    print("Cards received")
    print("Now send him your cards")
    for i in range(offer):
        while True:
            card = checkInput(1,5,"Choose the nomber of the card you want to send in [1,5] : ")
            if myHand.getCard(card-1) == 0:
                print("You have chosen a card you already sent... thats not very nice, please choose another.")
                continue
            else:
                mq.send(str(myHand.getCard(card-1)).encode(), type = traderPID)
                myHand.setCard(0, card-1)
                break 
    myHand.fuzeHands(HisHand.myHand)
    print("Your hand is now " +  myHand.__str__())

def handler(signum, frame):
    offersSemaphore = sysv_ipc.Semaphore(semKey)
    print("\n OH no game ended now i will die ")
    time.sleep(2)
    mq.send(str(1).encode(), type = 2)
    mq.receive(type = playerPID)
    print("Message reçu")
    offersSemaphore.acquire()
    try:
        _ = shared_memory.ShareableList(["0;0","0;0","0;0"],name="currentOffers")
    finally:
        temp = shared_memory.ShareableList(name="currentOffers")
        temp.shm.unlink()
    offersSemaphore.release()

    os.kill(playerPID, signal.SIGKILL)    
    

if __name__ == "__main__":
    signal.signal(signal.SIGHUP, handler)
    joinserver(playerPID)
    receiveHands()
    print(myHand.__str__())
    TrackingCurrentOffers()
    
  