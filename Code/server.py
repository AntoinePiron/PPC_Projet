import sysv_ipc
import time
from multiprocessing import shared_memory


ListePid = []

key = 128   # Declaration of the key for the message queues
debutkey = 100 #Could be passed to console args ?

#Shared Memory used to track current offrers 
currentOffers = shared_memory.ShareableList(["0;0","0;0","0;0"], name="currentOffers")
semKey = 256
#A semaphore used to protect the sharedMemory
offersSemaphore = sysv_ipc.Semaphore(256, sysv_ipc.IPC_CREAT, initial_value = 1)

mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT) #Creating main message queue

#Fonction qui permet de vider les messages queue encore pleine
def clearStart():
    md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)
    md.remove()

def debutjeu():
    print("Server has been launched, waiting for connections") 
    md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT) #Creating debut message queue
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
    md.remove()
    game()
        
        
#Fonction game, placeholder for now
def game():
    TrackingCurrentOffers()

def TrackingCurrentOffers():
    while True: 
        time.sleep(5)
        print(list(currentOffers))

if __name__ == "__main__": 
    clearStart()
    debutjeu()
