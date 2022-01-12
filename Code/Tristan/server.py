import sysv_ipc
import time


key = 128

mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
pid = []

while True:
    print(pid)
    message, t = mq.receive()
    value = message.decode()
    print(value)
    if not (pid.count(value) > 1):
        pid.append(value)
    
    