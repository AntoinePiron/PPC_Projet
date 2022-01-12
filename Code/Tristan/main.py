import multiprocessing
import utils
import os
import sysv_ipc

key = 128

mq = sysv_ipc.MessageQueue(key)
pid = int(os.getpid())
mq.send(pid)
