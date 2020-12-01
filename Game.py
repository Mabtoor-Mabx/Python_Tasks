import random
def Game(comp,you):
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
    elif comp == "P" and you == "S":
        return True
    elif comp == "S" and you == "P":
        return False 

print("Computer Turn ! Rock (R)  Paper(P) Scissor (S) : \n ")
randno = random.randint(1,3)
if randno == 1:
    comp = 'R'
elif randno == 2:
    comp == "P"
elif randno == 3:
    comp = "S"  


# print("Comp Turn: Rock(R) Paper(P) or Scissor(S)?")
# randNo = random.randint(1, 3) 
# if randNo == 1:
#     comp = 'R'
# elif randNo == 2:
#     comp = 'P'
# elif randNo == 3:
#     comp = 'S'

you = input("Enter Your Number  Rock(R) Paper(P) or Scissor(S)? : \n")
a= Game(comp,you)

if a == None:
    print("Match is Tie")
elif a:
    print("You Win")
else:
    print("You Lose")        