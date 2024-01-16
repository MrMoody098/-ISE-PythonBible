# there a serveral different data types in python

#String
myString = "string"
#Integers
myInt = 1
#Float
myFloat = 1.4
#Complex numbers
realPart = 1
imaginaryPart = 3
ComplexNumber = complex(realPart,imaginaryPart)

#SequenceTypes
list #Collection of Values
tuple # Immutable list
dict # List of Key-Value pairs

#Logical Operators
false = True and False # and returns true when a and b are true
true = False or True # or returns true if either a or b is true
false = True and not True # not negates output

#user Input
StringInput = input("Please input something") #reads in userinput as a string
IntegerInput = int(input("Please input a number")) # we have to cast the input if we want to store it as an integer

#Loops
    #while loop
number  = 0
while number < 10:
    number+=1

    #for loop
        #loops for each element in a sequence
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

        #loops setting x for each number in range of 0-100
for x in range (100):
    print(x)

        #loops setting x for each number between 20,80
for x in range (20,80):
    print(x)

#List
firstNum = numbers[0]
middleThree = numbers[1:4] #returms the middle three numbers
#List functions
len(list) #returns length of list
max(list) #returns the item with the maxiumum value
min(list) #returns the item with the minimum value
list(element) #Typecasts element into list
#List methods
list.append(element) #appends element to the list
list.count(element) #counts how many times an element appears in the list
list.index(element)#returns the first given index at which the given element occurs
list.pop() #removes and returns the last element
list.reverse() #reverse the order of the elements
list.sort() #Sorts the elements of a list

#Functions
def sumOfTwoNum (a,b):
    return a+b
print(sumOfTwoNum(1,2))

def sumOfSequence(*numbers):
    sum = 0
    for x in numbers:
        sum+=x
    return sum
print(sumOfSequence(1,4,6,2))

#Tuple
tpl = (10,20,30)#defined by parenthisis instead of brackets only difference
                #between a  list is that it cant be manipulated

#Dictionaries

dct ={"Name":"john", #also known as hash map it is a sequence of key-value pairs
      "Age":25,
      "Height":6.1}