fruit1 = input("Enter Fruit Name")
fruit2 = input("Enter Fruit Name")
fruit3 = input("Enter Fruit Name")
fruit4 = input("Enter Fruit Name")
fruit5 = input("Enter Fruit Name")
fruit6 = input("Enter Fruit Name")
fruit7 = input("Enter Fruit Name")

fruits = [fruit1 , fruit2 , fruit3 , fruit4 , fruit5 , fruit6 , fruit7]
print(fruits)


m1 = int(input("Enter Ist Marks \n"))
m2 = int(input("Enter 2nd Marks \n"))
m3 = int(input("Enter 3rd Marks \n"))
m4 = int(input("Enter 4th Marks \n"))
m5 = int(input("Enter 5th Marks \n"))
m6 = int(input("Enter 6th Marks \n"))

marks = [m1,m2,m3,m4,m5,m6]
marks.sort()
print(marks)




# mrks = (21,12,34,54,4,4,3,1,21)
# mrks[0]= 31
# print(mrks)


num = [31,21,32,43]
print(sum(num))

a=(7,0,8,0,0,9)
print(a.count(0))

Word = {
    "Pankha" : "Fan",
    "Darwaza" : "Door",
    "Kursi" : "Chair",
    "Maiz" : "Table",
    "Kanghi": "Comb"
}

print('''  Choose Any Word To Get Its English Mean.
        The Options Are :
''' , Word.keys())

a = input()

print(Word[a])



m1 = int(input("Enter Ist Number"))
m2 = int(input("Enter 2nd Number"))
m3 = int(input("Enter 3rd Number"))
m4 = int(input("Enter 4th Number"))
m5 = int(input("Enter 5th Number"))
m6 = int(input("Enter 6th Number"))
m7 = int(input("Enter 7th Number"))
m8 = int(input("Enter 8th Number"))


numbers = {m1,m2,m3,m4,m5,m6,m7,m8}
print(numbers)



dic = {18,"18"}
print(dic)


S= set()
S.add(20)
S.add(20.0)
S.add("20")

print(S)


S= {}

print(type(S))



Fac = {}
fr1 = input("Enter Your Language")
fr2 = input("Enter Your Language")
fr3 = input("Enter Your Language")
fr4 = input("Enter Your Language")
Fac["Waqas"] = fr1
Fac["Waheed"] = fr2
Fac["Horair"] = fr3
Fac["Hasnat"] = fr4

print(Fac)
