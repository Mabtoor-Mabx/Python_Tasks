#  ROCK PAPER SCISSOR GAME DESIGNED BY MABTOOR MABX
# import random

# def game(comp,you):
#     if comp==you:
#         print("Match Is Tie!!!")
#     elif (comp=="R" and you=="P") or (comp=="P" and you=="S") or (comp=="S" and you=="R"):
#         print("You Win!!!")
#     else:
#         print("You Lose!!!")

# print("Choose Your Number \n  R for Rock, P For Paper, S For Scissor")
# you = (input())
# comp = random.randint(0,2)
# if comp==0:
#     comp="R"
# elif comp==1:
#     comp="P"
# elif comp==2:
#     comp="S" 
# game(comp,you)




# GUESS THE NUMBER GAME DESGINED BY MABTOOR MABX

# import random
# NoOfGuess=0
# print("Enter Your Number! (1-100) \n")
# ActualNo = random.randint(1,100)
# while ActualNo:
#     GuessNo = int(input())
#     if ActualNo>GuessNo:
#         print("Please Select The Higher Number ")
#     elif ActualNo<GuessNo:
#         print("Please Select The Lower Number ")
#     elif ActualNo==GuessNo:
#         print(f"Congratulations! You Get the Number {ActualNo} , Your Score is {NoOfGuess}")  
#         break     
#     NoOfGuess+=1
    


 # BASIC CALCULATOR DESIGNED BY MABTOOR MABX

import math


def Add(num1,num2):
     add = num1+num2
     print(f"The Sum Of {num1} and {num2} is : {add}") 

def Sub(num1,num2):
     sub = num1+num2
     print(f"The Subtraction Of {num1} and {num2} is : {sub}") 
def Mult(num1,num2):
     mult = num1+num2
     print(f"The Multiplication Of {num1} and {num2} is : {mult}") 
def Div(num1,num2):
     div = num1+num2
     print(f"The Division Of {num1} and {num2} is : {div}")           
def SQ(num1):
     SQr = num1*num1
     print(f"The Square Of {num1}  is : {SQr}")  
def SQRT(num1):
     SQrt = math.sqrt(num1)
     print(f"The Square Root Of {num1}  is : {SQrt}")

def Log(num1):
     Log = math.log10(num1)
     print(f"The Logarithm Of {num1}  is : {Log}")

def Raised(num1,num2):
    raised =  math.pow(num1,num2)
    print(f"{num1} Raised To The Power {num2}  is : {raised}")
def Sin(num1):
    sin = math.sin(num1)
    print(f"The Sin Value Of {num1}  is : {sin}")
def Asin(num1):
     asin = math.asin(num1)
     print(f"The Inverse Sin  Of {num1}  is : {asin}")    
def Cos(num1):
    cos =  math.cos(num1)
    print(f"The Cos Value Of {num1}  is : {cos}")    
def Acos(num1):
     acos = math.acos(num1)
     print(f"The Inverse Cos  Of {num1}  is : {acos}")    
def Tan(num1):
    tan =  math.tan(num1)
    print(f"The Tan Value Of {num1}  is : {tan}")   
def Atan(num1):
     atan = math.atan(num1)
     print(f"The Inverse Tan  Of {num1}  is : {atan}")    

op  = input("Choose The Operator ( + , - , *, /, ^, sqr ,sqrt ,log, Sin, Sin- , Cos , Cos- , Tan , Tan-  ) \n")

if op=="+":
    no1 = int(input("Enter The Number \n"))
    no2 = int(input("Enter The Number \n"))
    Add(no1,no2)
elif op=="-":
    no1 = int(input("Enter The Number \n"))
    no2 = int(input("Enter The Number \n"))
    Sub(no1,no2)    
elif op=="*":
    no1 = int(input("Enter The Number \n"))
    no2 = int(input("Enter The Number \n"))
    Mult(no1,no2)
elif op=="/":
    no1 = int(input("Enter The Number \n"))
    no2 = int(input("Enter The Number \n"))
    Div(no1,no2)        
elif op=="sqr":
    no1 = int(input("Enter The Number \n"))
    SQ(no1)
elif op=="sqrt":
    no1 = int(input("Enter The Number \n"))
    SQRT(no1)   
elif op=="log":
    no1 = int(input("Enter The Number \n"))
    Log(no1)     
elif op=="^":
    no1 = int(input("Enter The Number \n"))
    no2 = int(input("Enter The Number \n"))
    Raised(no1,no2) 
elif op=="Sin":
    no1 = int(input("Enter The Number \n"))   
    Sin(no1)     
elif op=="Cos":
    no1 = int(input("Enter The Number \n"))   
    Cos(no1) 
elif op=="Tan":
    no1 = int(input("Enter The Number \n"))   
    Tan(no1)
elif op=="Sin-":
    no1 = int(input("Enter The Number \n"))   
    Asin(no1)                      
elif op=="Cos-":
    no1 = int(input("Enter The Number \n"))   
    Acos(no1)
elif op=="Tan-":
    no1 = int(input("Enter The Number \n"))   
    Atan(no1)                  