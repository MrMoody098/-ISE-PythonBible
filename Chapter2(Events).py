import threading

#With events we can manage our threads even better
#we can pause our thread and wait for a certain event to happen, in order to continue
event = threading.Event()

def function():
    print("Waiting for event...")
    event.wait()
    print("Continuing")

thread = threading.Thread(target=function)
thread.start()

x = input("Trigger event?")
if(x == "yes"):
    event.set()#this continues the function that has been told to wait by event