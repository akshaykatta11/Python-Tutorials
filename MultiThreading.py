# MultiThreading = Running Methods Simultaneously on Different Cores.
# For Threading we need Inherit every class with "Thread" and also import threading and as our PCs are way to fast we need to import sleep from time.

from time import sleep
from threading import *

class Hello(Thread):

    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)        # After Printing each "Hello" sleep for 1second

class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()      # start() is used to start the execution of threads
sleep(0.2)      # To avoid collision
t2.start()

# join() =  Telling the Main thread to wait until both the threads terminate.
t1.join()
t2.join()

print("Bye")       # If join() is not used the "Main thread would have executed this "BYE" statement in the middle.
