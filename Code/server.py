import sysv_ipc, time, pickle
from multiprocessing import shared_memory
from utils import *
import signal
import os

ListePid = []

key = 128   # Declaration of the key for the message queues
debutkey = 100 #Could be passed to console args ?

semKey = 256
#A semaphore used to protect the sharedMemory
offersSemaphore = sysv_ipc.Semaphore(256, sysv_ipc.IPC_CREAT, initial_value = 1)


#Fonction qui permet de vider les messages queue encore pleine et de reset la shared memory
def clearStart():
    #reload the messages queues
    global md
    md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)
    md.remove()
    md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)
    global mq
    mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
    mq.remove()
    mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

def debutjeu():
    print("Server has been launched, waiting for connections") 
    md = sysv_ipc.MessageQueue(debutkey) #Creating debut message queue
    #While there are less than 3 connection, wait for connection type messages
    while (len(ListePid) < 3):
        connection, t = md.receive(type = 1)
        print("New connection") 
        pid = connection.decode() #When a conncetion is detected, adds its pid to the list
        ListePid.append(pid)
        for i in range(len(ListePid)): #Sends a connection ack to every player
            print(".")
            md.send(str(len(ListePid)).encode(), type = 2)
    #When there are more than 3 players, stops waiting for connections
    
    print("We have 3 players !")
    print("We will now wait for every player to accept the start of the game")
    greenflag = 0
    while (greenflag < len(ListePid)): #Waits for every players to ack the start of the gaame
        value, t = md.receive(type = 3)
        flag = int(value.decode())
        greenflag = flag + greenflag #Value of flag message should always be one (for now)
        print(greenflag)
        
    print("Starting message queue deleted, game starting")
    print("Creating shared memory")
    try:
        _ = shared_memory.ShareableList(["0;0"] * len(ListePid),name="currentOffers")
    except FileExistsError:
        temp = shared_memory.ShareableList(name="currentOffers")
        temp.shm.unlink()
        _ = shared_memory.ShareableList(["0;0"] * len(ListePid), name="currentOffers")

def sendCard():
    mq = sysv_ipc.MessageQueue(key)
    print("Generating hands ... ")
    hands = generateHands(len(ListePid))
    print("Hands generated : ")
    print("Sending hands ...")
    for i in range(len(ListePid)):
        handToSend = hands[i]
        pidToSend = int(ListePid[i])
        byteHand = pickle.dumps(handToSend)
        mq.send(byteHand, type = pidToSend)
    print("Hands sended !")

#Pour l'instant on affiche juste les offres 
def TrackingCurrentOffers():
    global offers
    offers = shared_memory.ShareableList(name="currentOffers")
    while True: 
        print(list(offers))
        winwait()
        time.sleep(5)
        
def winwait():
    win, t = mq.receive(type = 1)
    print("Received win signal, sending termination signal")
    for pid in ListePid:
        os.kill(int(pid), signal.SIGHUP)
        print("Sent signal to" + pid)
        
    for pid in ListePid:
        end, t = mq.receive(type = 2)
    offers.shm.close()
    offers.shm.unlink()
    for pid in ListePid:
        mq.send(str(1).encode(), type = int(pid))
    
    print("Player all left, shutting down")
    os.kill(os.getpid(), signal.SIGKILL)
    print("Implement something to kill me now pls")

if __name__ == "__main__": 
    clearStart()
    debutjeu()
    sendCard()
    TrackingCurrentOffers()
    