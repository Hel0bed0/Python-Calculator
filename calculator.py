#!/usr/bin/env python3
#Time
import time
#Define values
n3 = 4
n4 = 5
n5 = 2
n6 = 1
n7 = 0
n8 = 6
#n9 is percentage
n10 = 100
n11 = 7
n12 = 3
#Loop 
while(n3 == 4):
#UI Loop
    while(True):
    #UI 
        print("What do you want to do? \n"
             "1. Addition\n"
             "2. Subtraction\n"
             "3. Multiplication\n"
             "4. Division\n"
             "5. Percentage\n"
             "6. Exit\n")

#Selector
        sel = int(input("Enter 1 - 6: "))
        if sel > n8 :
            print("IDK how to do that.")
        elif sel < n6 :
            print("IDK how to do that.")
        elif sel == n8 :
            ex = int(input("Are you sure you want to exit? Enter 1 to exit: "))
            if ex == n6 :
                exit()
        elif sel < n8 :
            n1 = float(input("First Number (crashes if NaN): "))
            n2 = float(input("Second Number (crashes if NaN): "))
            break
        
#Better Loop (pt1)
    if sel < n6 :
        print ("...")
    elif sel > n4 :
        print ("...")

#Percentages
    def calper(n2, n10):
        return n2 / n10
    n9 = calper(n2, n10)
#Calculator
    def add(n1, n2):
        return n1 + n2
    
    def sub(n1, n2):
        return n1 - n2
    
    def mul(n1, n2):
        return n1 * n2
    
    def div(n1, n2):
        return n1 / n2
    
    def per(n1, n9):
        return n1 * n9
    
#Output
    time.sleep(0.15)

    if sel == 1:
        print(n1, "+", n2, "=", add(n1, n2))
    
    elif sel == 2:
        print(n1, "-", n2, "=", sub(n1, n2))
    
    elif sel == 3:
        print(n1, "*", n2, "=", mul(n1, n2))
    
    elif sel == 4:
        print(n1, "/", n2, "=", div(n1, n2))
    
    elif sel == 5:
        print(n1, "%", n2, "=", per(n1, n9))
#Print "Done"

    if sel > n7 :
        print("Done")
    elif sel < n8 :
        print("Done")

#Better Loop (pt2)
    while(True):
    
       time.sleep(0.5)
       mr = int(input("Another calculation? Press 1 to calculate more, press 2 to exit, and 3 to sleep for 10 sec: "))
       if mr == n6 :
           time.sleep(0.15)
           print("OK")
           break
    # If input invalid
       elif mr > n12 :
           print("Enter Only 1, 2 or 3")
       elif mr < n6 :
           print("Enter Only 1, 2 or 3")
            
       elif mr == n5 :
          sr = int(input("Are you sure you want to exit? Enter 1 to exit: "))
          if sr == n6 :
            time.sleep(0.15)
            exit()
       elif mr == n12 :
            time.sleep(10)

       time.sleep(0.5)
