# Weekend_Practice 

#  Assignment_9

#  Problem 1

# file = open("read.txt", "r")
# file=file.read()
# print(file)



#  Problem 2

# def game():
#     return 534424213

# score = game()

# with open("hiscore.txt") as f:
#     Hiscore = f.read()

# if Hiscore=="":
#     with open("hiscore.txt", "w") as f:
#         f.write(str(Hiscore))
# elif int(Hiscore)<score:
#     with open("hiscore.txt", "w") as f:
#         f.write(str(Hiscore))

#  Problem 3

# for i in range(2,21):
#     with open(f"Multiplication Table Of {i}.txt", "w") as f:
#         for j in range(1,11):
#             f.write(f" {i} X {j} = {i*j} \n")



#  Problem 4

# with open("read.txt", "r") as f:
#   content=  f.read()
#   content = content.replace("Donkey", "@#$%^^")
#   with open("read.txt", "w") as f:
#       f.write(content)


#  Problem 5

# content = ["Donkey", "Loser", "Nothing", "Bullshit", "Dumbass", "Jackass"]
# with open("read.txt", "r") as f:
#     content = f.read()
#     for content in "read.txt":
#         content= content.replace(content, "@$#^@*^&#")
#         with open("read.txt", "w") as f:
#             f.write(content)

#  Problem 6

# with open("log.txt") as f:
#     log=f.read()

# if "Python" in log:
#     print("Python is Present In File")
# else:
#     print("Python Is Not Present In This File")   
#   

#  Problem 7

# content = True
# i=1

# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if "python" in content.lower():
#             print(f"Python Is Present In Line {i}")
#         i+=1    


#  Problem 8


# with open("read.txt") as f:
#     content=f.read()

# with open("this.txt", "w") as f:
#     f.write(content)



#  Problem 9


# with open("read.txt") as f:
#     content1 = f.read()
# with open("this.txt") as f:
#     content2 = f.read()

# if content1==content2:
#     print("Files Are Identical")
# else:
#     print("Files Are Not Identical")    



#  Problem 10

# with open("read.txt", "w") as f:
#     f.write("")


#  Problem 11

# import os
# with open("read.txt") as f:
#     content=f.read()

# with open("renameByread.txt" , "w") as f:
#     f.write(content)

# os.remove("read.txt")





#  Assignment 8


#  Problem 1

# def Max(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             print("Num1 is Greatest")
#         else:
#             print("Num3 is Greatest")
#     elif num2>num3:
#         print("Num2 is Greatest") 
#     else:
#         print("Num3 is the Greatest")         


# Max(2212323211,323943649328744, 556445)



#  Problem 2

# def Faren(cels):
#     faren = (cels*9/5)+32
#     return faren


# print(Faren(37))



#  Problem 3

# print("Good Morning!", end=" ")
# print("Good Morning!", end=" ")
# print("Good Morning!", end=" ")
# print("Good Morning!", end=" ")



#  Problem 4

# def Res(n):
#     if n==0:
#         return 0
#     else:
#         return n+ Res(n-1)

# print(Res(4))



#  Problem 5


# def Star(n):
#     for n in reversed(range(1,4)):
#         print("*" * n)
        
        
# Star(2)


#  Problem 6

# def cm(n):
#     Cm = n * 10
#     return Cm

# print(cm(3))


#  Problem 7


# def strip(String, word):
#     newstr = String.replace(word, "")
#     return newstr

# this = "  This  Is Mabtoor Mabx  "
# n= strip(this, " ")
# print(n)
# print(n.strip())



#  Problem 8

# def table(n):
#     for i in range(1,11):
#         print(f" {n} X {i} = {n*i}  ")


# table(4)




#  Assignment 7


#  Problem 1
# n = 6
# for i in range(1,11):
#     print(f" {n} X {i} = {n*i}")


#  Problem 2

# liste = ["Harry", "Shubham", "Sakhsi", "Saraswati"]
# for i in liste:
#     if i.startswith("S"):
#         print(f"Greeting! {i} ")


# Problem 3

# n = 5
# i= 1
# while i<11:
#     print(f" {n} X {i} = {n*i} ")
#     i+=1


#  Problem 4

# no= 2020

# if no%4==0:
#     print("This Is A Prime Number")
# else:
#     print("This is Not A Prime Number")    


#  Problem 5

# no = 4
# sum = 0
# i=0
# while i<=no:
#     sum = sum +i
#     i+=1

# print(sum)



#  Problem 6


# no = 3
# fact = 1

# for i in range(1,no+1):
#     fact*=i

# print(fact)




#  Problem 7

# n = 3
# for i in range(3):
#     print(" " * (n-1-i), end=" ")
#     print("*" * (2*i+1), end=" ")
#     print(" " *(n-i-1) )


#  problem  8

# n = 3
# for i in range(3):
#     print("*" * (i+1))

#  Problem 10


# n = 6

# for i in reversed(range(1,11)):
#     print(f" {n} X {i} = {n*i}")




#  Assignment_6


#  Problem 1

# no1= 23
# no2= 54
# no3= 53

# if no1>no2:
#     if no1>no3:
#         print("No1 is the Biggest!!!")
#     else:
#         print("No3 is The Biggest!!!")    
# elif no2>no3:
#     print("No2 is The Greatest!!!")        
# else:
#     print("No3 is The Greatest!!!")    



#  Problem 2


# no1 = 33
# no2 = 64
# no3 = 34

# if no1<33 or no2<33 or no3<33:
#     print("You Are Fail Because Your Marks Are lesser Than 33")
# elif no1+no2+no3<40:
#     print("You Are Fail Because Your Marks Are Lesser Than 40%")
# else:
#     print("You Are Pass")    


#  Problem 3

# spam = "If You Makes A Lot Of Money, Then Click This, Buy Now And Subscibe Our Channel "

# if "Makes A Lot Of Money":
#     spam = True
# elif "Click This":
#     spam = True
# elif "Buy Now":
#     spam = True
# elif "Subscobe Channel":
#     spam = True
# else:
#     spam = False    


# if spam:
#     print("Spam Is Present In Text")
# else:
#     print("Spam Is Not Present In text")    



#  Problem 5


# liste = ["Mabtoor", "Harry", "Christopher", "Angelina"]
# if "Python" in liste:
#     print("Name Is Present In Array")
# else:
#     print("Name is Not Present In Array")



#  Problem 6

# no1= 43
# if no1>90:
#     print("EX")
# elif no1>80 and no1<=90:
#     print("A+")
# elif no1>70 and no1<=80:
#     print("A")
# elif no1>60 and no1<=70:
#     print("B")    
# elif no1>50 and no1<=60:
#     print("C")
# elif no1>40 and no1<=50:
#     print("D")
# elif no1>=33 and no1<=40:
#     print("E")
# else:
#     print("F")            



#  Problem 7

# name = "Harry is Such A Nice Boy"
# if "harry" in name.lower():
#     print("This Post Is talk About Harry")
# else:
#     print("This Post Is Not Talk About Harry")    


#  Assignment_5


#  Problem 1

# dic = {
#     "Pankha" : "Fan",
#     "Maiz" : "Table" ,
#     "Darwaza" : "Door"
# }

# print(dic.keys())
# a = input("Choose Your choice \n")
# print(dic[a])



#  Problem 2

# a = int(input("Enter Your Number \n"))
# b = int(input("Enter Your Number \n"))
# c =  int(input("Enter Your Number \n"))
# d =  int(input("Enter Your Number \n"))
# e =  int(input("Enter Your Number \n"))
# f =  int(input("Enter Your Number \n"))
# g = int(input("Enter Your Number \n"))
# h = int(input("Enter Your Number \n"))

# j = {a,b,c,d,e,f,g,h}

# print(j)


#  Problem 3



#  Problem 6

# dic = {}
# lang1 =(input("Enter Language Name \n"))
# lang2 =(input("Enter Language Name \n"))
# lang3 =(input("Enter Language Name \n"))
# lang4 =(input("Enter Language Name \n"))

# dic[lang1] = "mabtoor"
# dic[lang2] = "Muneeb"
# dic[lang3] = "Mansoor"
# dic[lang4] = "Moiz"

# print(dic)



# #  Problem 7
# dic = {}
# lang1 =(input("Enter Language Name \n"))
# lang2 =(input("Enter Language Name \n"))
# lang3 =(input("Enter Language Name \n"))
# lang4 =(input("Enter Language Name \n"))

# dic[lang1] = "mabtoor"
# dic[lang2] = "Muneeb"
# dic[lang3] = "Moiz"
# dic[lang4] = "Moiz"

# print(dic)




#  Assignment_4


#  Problem 1

# fr1 = input("Enter Fruits Name \n")
# fr2 = input("Enter Fruits Name \n")
# fr3 = input("Enter Fruits Name \n") 
# fr4 = input("Enter Fruits Name \n")
# fr5 = input("Enter Fruits Name \n")
# fr6 = input("Enter Fruits Name \n")
# fr7 = input("Enter Fruits Name \n")
# fr8 = input("Enter Fruits Name \n")

# liste = [fr1,fr2,fr3,fr4,fr5,fr6,fr7,fr8]
# print(liste)



#   Problem 2

# fr1 = int(input("Enter Students Marks \n"))
# fr2 = int(input("Enter Students Marks \n"))
# fr3 = int(input("Enter Students Marks \n")) 
# fr4 = int(input("Enter Students Marks \n"))
# fr5 = int(input("Enter Students Marks \n"))
# fr6 = int(input("Enter Students Marks \n"))
# fr7 = int(input("Enter Students Marks \n"))
# fr8 = int(input("Enter Students Marks \n"))

# liste=[fr1,fr2,fr3,fr4,fr5,fr6,fr7,fr8]
# liste.sort()
# print(liste)



#  Problem 3


# liste = (21,2,13,2,343,3,2,23,2)
# liste[2] = 23
# print(liste)


#  Problem 4


# liste = [2,12,31,2,32,231,2,12,1,21]
# print(sum(liste))


#  Problem 5


# a = (7,0,8,0,9,0)
# print(a.count(0))



#  Assignment 3


#  Problem 1


# name =input("Enter Your Name \n")

# print("Greet" + str(name))


#Problem 2
