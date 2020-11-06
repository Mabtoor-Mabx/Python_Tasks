# Problem No 1


name = input("Enter Your Name \n")
print("Good After-Noon! Dear : " , name)


# Problem N0 2

letter= ''' Dear <|Name|> ! It is Very Pleasent To Inform You That
 You Are Selected
 Date : <|Date|>
'''

name = input("Enter Your Name \n" )
date = input("Enter Date \n")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|Date|>" , date)
print(letter)



# Problem 3

Name = "This  is very Pleasent  To Tell You That"
name = Name.find("  ")
print(name)

# Problem 4
name = "This  Is Very Pleasent To  Inform  You  That  We  Are   Here"
name = name.replace("  ", " ")
print(name)


# Problem 5

Letter = "Dear Harry! This Python Course Is Nice. Thanks"

Letter_Format = "Dear Harry\nThis Python Course is Nice\nThanks"

print(Letter_Format)