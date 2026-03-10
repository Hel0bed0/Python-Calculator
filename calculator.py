#!/usr/bin/env python3
#↑↑ use python3 to run code ↑↑

#Time
import time
#Define values
n3 = 3
#n9 is percentage
n10 = 100
#Loop 
while(n3 == 3):
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
        time.sleep(0.15)
        sel = int(input("Enter 1 - 6 (crashes if NaN): "))
        if sel > 6 :
            print("IDK how to do that.")
        elif sel < 1 :
            print("IDK how to do that.")
        elif sel == 6 :
            ex = int(input("Are you sure you want to exit? Enter 1 to exit: "))
            if ex == 1 :
                exit()
        elif sel < 6 :
            while(True):
                n1 = float(input("First Number (crashes if NaN): "))
                n2 = float(input("Second Number (crashes if NaN): "))
                #Back function
                ba = int(input("1 to calculate, other to cancel: "))
                if ba == 1 : 
                    break
            break
  
#Valid Input Checker 
    if sel < 1 :
        print ("...")
    elif sel > 5 :
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

    if sel > 0 :
        print("Done")
    elif sel < 6 :
        print("Done")

#Better Loop
    while(True):
    
       time.sleep(0.15)
       print("Another calculation?\n"
             "Press 1 to calculate more\n" 
             "Press 2 to exit\n" 
             "Press 3 to sleep for 10 sec\n")
        
       mr = int(input("Enter Number: "))
       if mr == 1 :
           time.sleep(0.15)
           print("OK")
           time.sleep(0.4)
           break
    #Valid Input Checker and Exit Function
       elif mr == 10 :
           print("Easter Egg")
       elif mr > 3 :
           print("Enter Only 1, 2 or 3")
       elif mr < 1 :
           print("Enter Only 1, 2 or 3")  
       elif mr == 2 :
          sr = int(input("Are you sure you want to exit? Enter 1 to exit: "))
          if sr == 1 :
            time.sleep(0.15)
            exit()
       elif mr == 3 :
            time.sleep(10)

       time.sleep(0.5)
