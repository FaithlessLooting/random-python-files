#Dylan Jugroop
#Bubble Sort
#03/11/2015
from random import randrange
import sys
from datetime import datetime

numbers=int(input("how many numbers would you like to search"))
# Generate a sorted list of numbers.
print ('Generating sorted random list...')
list = []
for i in range (0,numbers):
    list.append(randrange(numbers))
print (list)
startTime = datetime.now()
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1


shortBubbleSort(list)
print(list)
print (datetime.now() - startTime)

input()
