from random import randrange
import sys #importing some useful modules
from datetime import datetime
numbers=int(input("how many numbers would you like to search"))
# Generate a sorted list of numbers.
print ('Generating sorted random list...')
list = []  #empty list
for i in range (0,numbers): #for each of how many numbers we want 
    list.append(randrange(numbers)) #add a random number to the list
print (list) 
startTime = datetime.now()
def insertionSort(list): 
   for index in range(1,len(list)): #for letter in list

     currentvalue = list[index] #works out which number youre checking
     position = index

     while position>0 and list[position-1]>currentvalue: #while we're checking a value in the list and its smaller than the one before it
         list[position]=list[position-1] #move it back one
         position = position-1

     list[position]=currentvalue 

insertionSort(list)
print(list)
print (datetime.now() - startTime)
