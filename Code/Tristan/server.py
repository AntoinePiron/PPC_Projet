import sysv_ipc
import time


key = 128
debutkey = 100

mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)

pid = []
debut = False

while True:
    print(pid)
    while debut == False:
        message, t = md.receive()
        value = message.decode()
        pid.append(value)
        md.send(str(len(pid)).encode(), 1)
        print(pid)
        if (len(pid) >= 3):
            print("WE HAve 3 players")
            md.send(str(len(pid)).encode(), 2)
            md.remove()
            debut == True
    while True:
        pass    
    
            
    

    