import sysv_ipc
import time


key = 128

mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
pid = []

while True:
    message, t = mq.receive()
    value = message.decode()
    time.sleep(5)
    print(pid)
    for a in pid:
        if (mq.receive == a):
            mq.send("We already have your pid !")
        else:
            mq.send("Your pid has been received, you are in this game")
            pid.append(message)
    
    