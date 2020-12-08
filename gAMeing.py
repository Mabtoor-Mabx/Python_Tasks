import random

def GQME(comp,you):
    if comp==you:
        return None
    elif comp == "R" and you == "P":
        return True
    elif comp == "P" and you == "R":
        return False
    elif comp == "R" and you == "S":
        return False
    elif comp == "S" and you == "R":
        return True
    elif comp == "P"  and you == "S":
        return True
    elif comp == "S" and you == "P":
        return False

print("Computer Choose !  Rock(R) , Paper(P) , Scissor (S) \n ")
randNo = random.randint(1,3)
if randNo==1:
    comp = "R"
elif randNo==2:
    comp = "P"
elif randNo==3:
    comp = "S"        

you=input("Your Turn ! Rock (R) , Paper (P), Scissor(S) ")
b= GQME(comp,you)
if None:
    print("Match Is Tie")
elif b:
    print("Congratulation! You Win The Match")
else:
    print("Alas! You Lose")       
