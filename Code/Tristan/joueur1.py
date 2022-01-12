import multiprocessing
import time
from utils import *
import os
import sysv_ipc

key = 128

mq = sysv_ipc.MessageQueue(key)

if __name__ == "__main__":
    while True:
        print("Hello and Welcome to the Cambiecolo game !")
        time.sleep(2)
        print("Your pid will now be sent to the server for you to be in the game")
        try:
            type = int(input("1 for sending pid, 2 for termination : "))
            if type != 1 and type != 2:
                print("Wrong values")
                exit(1)
        except:
            print("An error occured")
            exit(1)
        if type == 1:
            pid = str((os.getpid())).encode()
            mq.send(pid)
        else:
            exit(1)


    
