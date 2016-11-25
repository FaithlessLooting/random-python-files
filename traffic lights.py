#matthew dove
#traffic lights
#16/09/2015
import time
import random


A= "green"
B= "green"
C= "red"
D= "red"
x=0
button=0
Buttonpressed = False
        

while Buttonpressed == True:
    A = "red"
    B = "red"
    C = "red"
    D = "red"
    print("")
    print("a is",A) 
    print("b is",B)
    print("c is",C)
    print("d is",D)
    print("")
    time.sleep(2)
    Buttonpressed = False

for x in range (1,10):
    A = "green"
    B = "green"
    C = "red"
    D = "red"
    print("")
    print("a is",A) 
    print("b is",B)
    print("c is",C)
    print("d is",D)
    print("")
    button = random.randint(1,5)
    if button==5:
        A = "red"
        B = "red"
        C = "red"
        D = "red"
        print("")
        print("a is",A) 
        print("b is",B)
        print("c is",C)
        print("d is",D)
        print("")
        time.sleep(2)
        x=x+1
else:
        time.sleep(5)
        A = "red"
        B = "red"
        C = "red_and_amber"
        D = "red_and_amber"
        print("")
        print("a is",A) 
        print("b is",B)
        print("c is",C)
        print("d is",D)
        print("")
button = random.randint(1,5)
if button==5:
    A = "red"
    B = "red"
    C = "red"
    D = "red"
    print("")
    print("a is",A) 
    print("b is",B)
    print("c is",C)
    print("d is",D)
    print("")
    time.sleep(2)
    x=x+1
else:
    time.sleep(2)
    A = "red"
    B = "red"
    C = "green"
    D = "green"
    print("")
    print("a is",A) 
    print("b is",B)
    print("c is",C)
    print("d is",D)
    print("")
    time.sleep(5)
    x= x+1
        
