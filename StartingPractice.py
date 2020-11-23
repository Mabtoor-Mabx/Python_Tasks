no1 = int(input("Enter Your Number \n")) 
no2 = int(input("Enter Your Number \n"))
no3 = int(input("Enter Your Number \n")) 
no4 = int(input("Enter Your Number \n")) 

if no1>no4:
    final1 =no1
else:
    final1 = no4

if no2>no3:
    final2 = no2
else:
    final2 = no4    

if final1>final2:
    print("Final1 Is Winner")
else:
    print("Final2 Is Winner")





# no1 = int(input( "Enter Your Marks \n"))  
# no2 = int(input( "Enter Your Marks \n")) 
# no3 = int(input( "Enter Your Marks \n"))


# if no1<33 or no2<33 or no3<33:
#     print("You Are Fail Because Your Marks Are Lesser Than 30 %")
# elif (no1+no2+no3)/300 <40:
#     print("You are Fail Because Your Average Is Lesser Than 40%")
# else:
#     print("You Are Pass")







# text = input("Enter Any Text")

# if "Makes A lot Of Money " in text:
#     spam = True
# elif "Subscribe This" in text:
#     spam = True
# elif "Buy Now" in text:
#     spam = True
# elif "Click This" in text:
#     spam = True
# else:
#     spam = False

# if spam:
#     print("Spam is Exist in Text")
# else:
#     print("Spam Does not Exist In Text")







# marks = int(input("Enter Your Marks"))

# if marks>90:
#     grade = "EX"
# elif marks>80 and marks<=90:
#     grade = "A"
# elif marks > 70 and marks <=80:
#     grade = "B" 
# elif marks > 60 and marks <=70:
#     grade = "C"
# elif marks > 50 and marks <=60:
#     grade = "D"
# elif marks > 40 and marks <=50:
#     grade  = "E"
# else:
#      grade = "F"        

# if grade:
#     print ("Your Grade is " , grade)






# text = input("Enter Post")
# if "Harry" in text:
#     print("This Post Is Talk About Harry")
# else:
#     print("This Post Does not Talk About Harry")   
#  



# dic = {
#     "Pankha" : "Fan" ,
#     "Darwaza" : "Door",
#     "Maiz" : "Table"

# }
# print("Options Are :", dic.keys())
# name = input("Choose Your Choice \n")

# print(dic[name])



# a = int(input("Enter Your Number")) 
# b = int(input("Enter Your Number"))
# c = int(input("Enter Your Number"))
# d = int(input("Enter Your Number")) 
# e = int(input("Enter Your Number")) 
# f = int(input("Enter Your Number"))
# g = int(input("Enter Your Number"))
# h = int(input("Enter Your Number"))


# i = {a,b,c,d,e,f,g,h}

# print(i)






# s = {}

# print(type(s))



# lang = {}

# fr1 = input("Enter Your Language \n ") 
# fr2 = input("Enter Your Language \n ")
# fr3 = input("Enter Your Language \n ")
# fr4 = input("Enter Your Language \n ")


# lang["waqas"] = fr1
# lang["Horair"] = fr2
# lang["Waheed"] = fr3
# lang["Hasnat"] = fr4


# print(lang)





# fr1 = input("Enter Fruit Name \n")
# fr2 = input("Enter Fruit Name \n")
# fr3 = input("Enter Fruit Name \n")
# fr4 = input("Enter Fruit Name \n")
# fr5 = input("Enter Fruit Name \n")
# fr6 = input("Enter Fruit Name \n")
# fr7 = input("Enter Fruit Name \n")

# liste = [fr1,fr2,fr3,fr4,fr5,fr6,fr7]

# print(liste)







marks1 =int(input("Enter Your Marks"))
marks2 =int(input("Enter Your Marks"))
marks3 =int(input("Enter Your Marks"))
marks4 =int(input("Enter Your Marks"))
marks5 =int(input("Enter Your Marks"))
marks6 =int(input("Enter Your Marks"))


Tmarks = [marks1,marks2,marks3,marks4,marks5,marks6]


Tmarks.sort()

print(Tmarks)





