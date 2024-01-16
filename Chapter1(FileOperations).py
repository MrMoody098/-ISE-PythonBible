#before we read from or write into a file we first need to open a file stream
#this returns the respective file as am object amd allows us to deal with it

file = open("myFile.txt","r") #opens file stream and saves to variable
# takes in two parameters file name and access mode

#--------------Access modes-------------------
#     Letter                      Access Mode
#       r                           Reading
#       r+             reading and writing(no Truncating)
#       rb                      Reading binary file
#       rb+        reading and writing binary file(no truncating)
#       w                           Writing
#       w+              reading and Writing(truncating File)
#       wb                     writing binary File
#       wb+          Reading and Writing Binary File(Truncating)
#       a                           Appending
#       a+                      Reading and appending
#       ab                        Appending binary
#       ab+                     Reading and Appending Binary File

# when we no longer need our file we close the stream(python does
# this automatically sometimes however it is considered good practice)
file.close()

#with statement opens stream runs intended code and closes stream afterwards
with open("myFile.txt","r") as file:
    print(file.read())#reads and prints whole file
    print(file.read(50))#reads and prints first 50 characters

file = open("myFile.txt","w")
print(file.write("Hello World")) #.write used to write to our file
file.flush()#text doesnt get written until we flush our stream kinda like flushing poop down the toilet
file.close()#closing the file automatically flushes the stream

#other Operations
#Os stands for operating system * imports all modules
from os import *
remove("myFile.txt")#deletes file from computer
rename("myFile.txt","newFile.txt") #renames file to dst

rename("newFile.txt","newDir/newFile.txt") # can also be used to move files into different
#directory however Dir needs to already exist it cannot make a new one

mkdir("newDir")#creates a new directory(folder)
chdir("newDir")#chooseDirectory goes into the Directory
chdir("..")#this goes back to the previous directory
rmdir("newDir")#removes/Deletes directory