import sysv_ipc
import time


key = 128
debutkey = 100

mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
md = sysv_ipc.MessageQueue(debutkey, sysv_ipc.IPC_CREAT)

pid = []

while True:
    while len(pid) < 3:
        message, t = md.receive()
        value = message.decode()
        if not (pid.count(value) > 1):
            pid.append(value)
            md.send(len(pid))
    
    