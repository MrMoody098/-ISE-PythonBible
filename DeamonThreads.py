# daemon Threads are a special kind of thread that runs in the background this means that the
# program can be terminated even if this thread is still running4
import threading
import time

# Define the path to the file
path = "C:/Users/ticta/OneDrive/Desktop/file.txt"
# Initialize an empty string to store the text from the file
text = ""

# Function to read the file
def readFile():
    # Declare global variables
    global path, text
    # Continuously read the file
    while True:
        # Open the file and read its content
        with open(path) as file:
            text = file.read()
        # Wait for 3 seconds before reading the file again
        time.sleep(3)

# Function to print the text from the file
def printLoop():
    # Declare global variable
    global text
    # Print the text 30 times
    for x in range(30):
        print(text)
        # Wait for 1 second before printing again
        time.sleep(1)

# Create a daemon thread to read the file
t1 = threading.Thread(target=readFile, daemon=True)
# Create a thread to print the text
t2 = threading.Thread(target=printLoop)

# Start the threads
t1.start()
t2.start()