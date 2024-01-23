# This code creates two queues. The first queue is filled with numbers from 0 to 4,
# and these numbers are then extracted and printed. The second queue is used in conjunction
# with worker threads that calculate and print the factorial of numbers.
# The numbers are added to the queue, and the worker threads extract them, calculate their factorial,
# and print the result. When all tasks are done, None is added to the queue to signal the workers to stop.

import threading
import math
import queue

# Create an instance of the queue class
q = queue.Queue()

# Add elements to the queue
for x in range(5):
    q.put(x)

# Extract and print elements from the queue
for x in range(5):
    print(q.get(x))

# Create another queue
q1 = queue.Queue()
threads = []


# Define a worker function that calculates and prints the factorial of numbers
def worker():
    while True:
        item = q1.get()
        if item is None:
            break
        print(math.factorial(item))
        q1.task_done()


# Start worker threads
for x in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# List of numbers
zahlen = [13400, 14, 5, 300, 98, 88, 11, 23]

# Add numbers to the queue
for item in zahlen:
    q1.put(item)

# Wait for all tasks to be done
q1.join()

# Add None to the queue to signal the workers to stop
for i in range(5):
    q1.put(None)
