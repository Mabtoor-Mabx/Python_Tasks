import os

print('''
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle little star
How I wonder what you are
''')

from PIL import Image
im = Image.open("Artificial Intelligence Concepts_Certificate of Completion-images.jpg")


print (os.listdir())

# 'git', '.vscode', 'Artificial Intelligence Concepts_Certificate of Completion-images.jpg', 'Assignment_2.py', 'Assignment_3.py', 
# 'First_Assignment.py',
#  'onetothreeassignment.py', 'play.mp3', 'Test.py', 'Variables.py'


a =10
b=20
c= a+b
print(c)


a = 90
b=53
c= a%b
print(c)


c = input()

print(type(c))



a = int(input("Enter First Value"))
b= int(input("Enter Second Value"))
c  =  (a+b) /2
print(c)




a = 34
b= 80

print (a>b)


a = 12

print(a*a)




a = input("Enter Your Name")

print("Good Afternoon! Mr" , a , "Have A Nice Day")


name = input("Enter Your Name")
date = input("Enter Date")

print("Dear" , name , "You Are Selected . Date is" , date)

letter ="You Can   Find  Double  Spaces  in  This Line"
print(letter.find("  "))
print(letter.replace("  " , " "))

letter = "Dear Harry ! This Python Course is Nice. Thanks"
formated = "Dear Harry! \n This Python Course is Nice \n Thanks"

print(formated)