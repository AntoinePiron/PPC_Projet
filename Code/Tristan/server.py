from socket import timeout
import sysv_ipc
import time



ListePid = []
key = 128
debutkey = 100

md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)
md.remove()
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
    
    
        
        
    


if __name__ == "__main__":
    
    debutjeu()
