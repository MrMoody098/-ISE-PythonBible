#daemon Threads are a special kind of thread that runs in the background this means that the
#program can be terminated even if this thread is still running4

import threading
import time

path = "C:/Users/ticta/OneDrive/Desktop/file.txt"
text = ""

def readFile():
    global path,text
    while True:
        with open(path) as file:
            text = file.read()
        time.sleep(3)

def printLoop():
    global text
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile,daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()