import os
from multiprocessing import Process
import time

print('Processing (%s) start...'%os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just create a child process (%s).' % (os.getpid(),pid))
