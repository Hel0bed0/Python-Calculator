#!/usr/bin/env python3
#↑↑ use python3 to run code ↑↑

#Time
import time
#Define values
on = 1
ctk = 273.15
ctfm = 1.8
ctfa = 32
mtf = 3.28084
mty = 1.093613
khtms = 0.2777778
khtmh = 0.6213712
khtfts = 0.9113444
mhtkh = 1.609344
mhtfs = 1.466667
mhtms = 0.44704
ftm = 0.3048
fti = 12
ftcm = 30.48
#np is percentage
n10 = 100
#debug


#Start Menu
print("Start")
debug = int(input("debug: 1 = On Other = Off|: "))   
crs = int(input("crs: 1 = On Other = Off (LEAVE OFF IF YOU DON'T KNOW WHAT THIS DOSE!)|: "))

#Loop 
while(True):
#UI
 #Selector (master)
    #debug
    if debug == 1 :
        print("debug:]")
        
    print("1 - Convert\n"
          "2 - Calculate\n")
    cms1 = int(input("Enter: "))
    print("OK:",cms1,"|")

    #Selector (Con)
    if cms1 == 1 :
        print("What do you want to do? \n"
              "1. Convert Celsius \n"
              "2. Convert Metre \n"
              "3. Convert KPH \n"
              "4. Convert MPH \n"
              "5. Convert Feet \n")
        if cms1 == 1 :      
            sel2 = int(input("Enter 1 - 5 (crashes in NaN): "))
            print("/////////////////////////////////////")
            #Subselect
            while(True):
                    if sel2 == 1 :
                        print("Convert to \n"
                             "From Celsius \n"
                             "1. Kelvin \n"
                             "2. Fahrenheit \n")
                    elif sel2 == 2 :
                        print("Convert to \n"
                            "From Metre \n"
                            "1. Feet \n"
                            "2. Yard \n")
                    elif sel2 == 3 :
                        print("Convert to \n"
                            "From KPH \n"
                              "1. MPH \n"
                              "2. M/S \n"
                              "3. F/S \n")
                    elif sel2 == 4 :
                        print("Convert to \n"
                            "From MPH \n"
                              "1. KPH \n"
                              "2. Ft/S \n"
                              "3. M/S \n")
                    elif sel2 == 5 :
                        print("Convert to \n"
                            "From Feet \n"
                              "1. Metre \n"
                              "2. Inch \n"
                              "3. Centimetre \n")
                    sel3 =int(input("Enter Value: "))
                    print("→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←")
                    print("OK:",sel3)
                    n1 = float(input("Enter Value: "))
                    print("→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←")
                    ok2 = int(input("1 - Convert - Other - Cancel: "))
                    if ok2 == 1 :
                        time.sleep(0.2)
                        break
                    #debug
                    if debug == 1 :
                        print("debug:]")
        #Tell selected
        print(sel2,"|",sel3,)

#Calculator sel master
    if debug == 1 :
        print("debug:]")
    if cms1 == 2 :
        print("What do you want to do? \n"
             "1. Addition\n"
             "2. Subtraction\n"
             "3. Multiplication\n"
             "4. Division\n"
             "5. Percentage\n"
             "6. Exit\n")
    #Selector (Cal)
    if cms1 == 2 :
        time.sleep(0.15)
        sel1 = int(input("Enter 1 - 6 (crashes if NaN): "))
        if sel1 > 6 :
            print("IDK how to do that.")
        elif sel1 < 1 :
            print("IDK how to do that.")
        elif sel1 == 6 :
            ex = int(input("Are you sure you want to exit? Enter 1 to exit: "))
            if ex == 1 :
                exit()
        elif sel1 < 6 :
            while(True):
                print("→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←")
                n1 = float(input("First Number (crashes if NaN): "))
                print("→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←")
                n2 = float(input("Second Number (crashes if NaN): "))
                #Back function
                print("→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←→←")
                ba = int(input("1 - Calculate - Other - Cancel: "))
                if ba == 1 : 
                    break
#Valid Input Checker
    #debug
    if debug == 1 :
        print("debug")
    #1
    if cms1 == 1 :
        if sel2 < 1 :
            print ("...")
        elif sel2 > 2 :
            print ("...")
    #2
    if cms1 == 2 :
        if sel1 < 1 :
            print ("...")
        elif sel1 > 5 :
            print ("...")
    #debug
    if debug == 1 :
        print("debug")

#Percentages
    if cms1 == 2 :
        def calper(n2, n10):
            return n2 / n10
        np = calper(n2, n10)
#Calculator
    if cms1 == 2 :
        def add(n1, n2):
            return n1 + n2
    
        def sub(n1, n2):
            return n1 - n2
    
        def mul(n1, n2):
            return n1 * n2
    
        def div(n1, n2):
            return n1 / n2
    
        def per(n1, np):
            return n1 * np
#Converter
    if cms1 == 1 :
    
        #debug
        if debug == 1 :
            print("debug:]")
            
        def ctka(n1, ctk):
            return n1 + ctk
            
        def ctfa1(n1, ctfm, ctfa):
            return (n1 * ctfm) + ctfa
        
        def mtf1(n1, mtf):
            return n1 * mtf
        
        def mty1(n1, mty):
            return n1 * mty
            
        def khtms1(n1, khtms):
            return n1 * khtms
            
        def khtmh1(n1, khtmh):
            return n1 * khtmh
            
        def khtfts1(n1, khtfts):
            return n1 * khtfts
            
        def mhtkh1(n1, mhtkh):
            return n1 * mhtkh
            
        def mhtfs1(n1, mhtfs):
            return n1 * mhtfs
        
        def mhtms1(n1, mhtms):
            return n1 * mhtms
            
        def ftm1(n1, ftm):
            return n1 * ftm
        
        def fti1(n1, fti):
            return n1 * fti
        
        def ftcm1(n1, ftcm):
            return n1 * ftcm
#Breakup UI to be nicer on eyes
    print("////////////////////////////////////////////////////////////////////")
#Output ans
    time.sleep(0.15)
    if cms1 == 2 :
        if sel1 == 1:
            print(n1, "+", n2, "=", add(n1, n2))
    
        elif sel1 == 2:
           print(n1, "-", n2, "=", sub(n1, n2))
    
        elif sel1 == 3:
            print(n1, "*", n2, "=", mul(n1, n2))
    
        elif sel1 == 4:
            print(n1, "/", n2, "=", div(n1, n2))
    
        elif sel1 == 5:
            print(n1, "%", n2, "=", per(n1, np))
    if cms1 == 1 :

        if sel2 == 1:
            if sel3 == 1 :
                print(n1, "Celsius is", ctka(n1, ctk), "Kelvin")
            elif sel3 == 2 :
                print(n1, "Celsius is", ctfa1(n1, ctfm, ctfa), "Farenheit",)
            
        elif sel2 == 2:
            if sel3 == 1 :
                print(n1, "Meters is", mtf1(n1, mtf), "Feet" ,)
            elif sel3 == 2 :
                print(n1, "Meters is", mty1(n1, mty), "Yards" ,)
                
        elif sel2 == 3:
            if sel3 == 1 :
                print(n1, "KPH is", khtms1(n1, khtms), "M/S" ,)
            elif sel3 == 2 :
                print(n1, "KPH is", khtmh1(n1, khtmh), "MPH" ,)
            elif sel3 == 3 :
                print(n1, "KPH is", khtfts1(n1, khtfts), "Ft/S" ,)
                
        elif sel2 == 4:
            if sel3 == 1 :
                print(n1, "MPH is", mhtkh1(n1, mhtkh), "KPH" ,)
            elif sel3 == 2 :
                print(n1, "MPH is", mhtfs1(n1, mhtfs), "Ft/S" ,)
            elif sel3 == 3 :
                print(n1, "MPH is", mhtms1(n1, mhtms), "M/S" ,)
            
        
        elif sel2 == 5:
            if sel3 == 1 :
                print(n1,  "Feet is", ftm1(n1, ftm), "Metre" ,)
            elif sel3 == 2:
                print(n1, "Feet is", fti1(n1, ftm), "Inch" ,)
            elif sel3 == 3:
                print(n1, "Feet Is", ftcm1(n1, ftcm), "Centimetre" ,)
#Breakup UI to be nicer on eyes
    print("////////////////////////////////////////////////////////////////////")
#Print "Done"
    if cms1 == 2 :
        if sel1 > 0 :
            print("Done")
        elif sel1 < 6 :
            print("Done")
    if cms1 == 1 :
        if sel2 > 0 :
            print("Done")
        elif sel2 < 4 :
            print("Done")
#Better Loop and next task ask
    while(True):
    
       time.sleep(0.15)
       #Breakup UI to be nicer on eyes
       print("------------------------------------------------------------------\n"
             "------------------------------------------------------------------\n")
             
       #Ask for command
       print("Another calculation?\n"
             "Press 1 to calculate more\n" 
             "Press 2 to exit\n" 
             "Press 3 to sleep for 10 sec\n")
             
       #Command enter
       mr = int(input("Enter 1 - 3: "))
       if mr == 1 :
           time.sleep(0.15)
           print("------------------------------------------------------------------\n"
                 "OK\n")
           time.sleep(0.4)
           break
    #Valid Input Checker and Exit Function
       elif mr == 10 :
           print("Easter Egg :]")
       elif mr > 3 :
           print("------------------------\n"
                 "Enter Only 1, 2 or 3\n"
                 "------------------------\n")
       elif mr < 1 :
           print("------------------------\n"
                 "Enter Only 1, 2 or 3\n"
                 "------------------------\n") 
       elif mr == 2 :
          sr = int(input("Are you sure you want to exit? Enter 1 to exit: "))
          if sr == 1 :
            time.sleep(0.15)
            exit()
       elif mr == 3 :
            time.sleep(10)

       time.sleep(0.5)
    if debug == 1 :
      print("debug:]")
    if crs == 1 :
        exit()
