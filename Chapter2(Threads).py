#Threads
import threading
import time
#we make a function that we want to call
def hello():
    print("hello world")
#make a thread and set its target function to our hello function
t1 = threading.Thread(target=hello)
#start runs threads simultanously
t1.start()

def function1():
    for x in range (100):
        print("1 runs simultanously")
def function2():
    for x in range(100):
        print("2 runs simulatnously")
def function3():
    for x in range (10):
        print("Three runs serially")
def function4():
    for x in range (10):
        print("four runs serially")

ones = threading.Thread(target=function1)
twos = threading.Thread(target=function2)
threes = threading.Thread(target=function3)
fours = threading.Thread(target=function4)
#function 3 and 4 run serially as in one by one
threes.run()
fours.run()
#function 1 and 2 run in parallel
ones.start()
twos.start()

#locking with threads can be used to lock access to resources whilst a thread is running

x = 8192
#lock object
lock = threading.Lock()

def halve():
    #access global variables
    global x,lock
    #this locks the resources
    lock.acquire()
    while(x>1):
        x /= 2
        print(x)
        time.sleep(1)
    print("END")
    #this releases the lock on resources and allows another thread to lock/ acccess resources
    lock.release()

def double():
    global x,lock
    lock.acquire()
    while(x<16384):
        x *=2
        print(x)
        time.sleep(1)
    print("END!")
    lock.release()
thread1 = threading.Thread(target=halve)
thread2 = threading.Thread(target=double)
thread1.start()
thread2.start()

#semaphores allow us not to completely lock a resource but limits the amount of accesses or threads
semaphore = threading.BoundedSemaphore(value=5)#allows 5 parrell accesses
def access(thread_number):
    print("{}: Trying ACCESS".format(thread_number))
    semaphore.acquire()
    print("{}:  Access granted!".format(thread_number))
    print("{}: waiting 5 seconds".format(thread_number))
    time.sleep(5)
    semaphore.release()
    print("{}: realeasing".format(thread_number))

for thread_number in range (10):
    t = threading.Thread(target=access,args=(thread_number,))
    t.start()