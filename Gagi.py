import random
def Game(comp,you):
    if comp==you:
        return None
    elif comp=="R" and you == "P":
        return True    
    elif comp == "P" and you == "R":
        return False    
    elif comp ==  "R" and you == "S":
        return False
    elif comp == "S" and  you == "R":
        return True
    elif comp == "P" and you  == "S"  :
        return True
    elif comp == "S" and you == "P" :
        return False                

print("Computer Turn ! Rock (R) , Paper(P) and Scissor(S) \n")
RandNo = random.randint(1,3)

if RandNo == 1:
    comp = "R"
elif RandNo==2:
    comp = "P"
elif RandNo==3:
    comp = "S" 

you = input("Your Turn ! Rock (R) , Paper(P) and Scissor(S) \n ")

a = Game(comp,you)

if a==None:
    print("Match is Tie \n")
elif a:
    print(" Congratulations! You Win") 
else:
    print("Alas! You Lose")       