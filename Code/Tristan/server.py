from socket import timeout
import sysv_ipc
import time



ListePid = []
debutkey = 100

#Cette création ne sert à rien, elle est simplement là pour vider la message queue du début pour éviter les problèmes, c'est temporaire
def debutjeu():
    print(ListePid)
    print("Server has been launched, waiting for connections")
    md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)

    while (len(ListePid) < 3):
        connection, t = md.receive(type = 0)
        print("New connection")
        pid = connection.decode()
        ListePid.append(pid)
        for i in range(len(ListePid)):
            print(".")
            md.send(str(len(ListePid)).encode(), type = 1)
    print("We have 3 players !")
    print("We will now wait for every player to accept the start of the game")
    greenflag = 0
    while (greenflag < len(ListePid)):
        value, t = md.receive(type = 2)
        flag = int(value.decode())
        greenflag = flag + greenflag
        print(greenflag)
    print("Starting message queue deleted, game starting")
    md.remove()
    game()
        
        
def game():
    while True:
        pass    


if __name__ == "__main__":
    
    debutjeu()
