#  Problem 1

# def Maximum(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3    
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3    

# c = Maximum(21,45,11)
# print("The Maximum Number Is :" , c)


#  Problem 2

# def Func(cels):
#     faren = ((cels * 9/5) + 32)
#     return faren

# Temp = Func(30)
# print("The Temperature In Farenheight Is :" , Temp)


#  Problem 3

# print("Hello" , end="")
# print("Have" , end="")
# print("A" , end="")
# print("Nice" , end="")
# print("Day" , end="")


#  Problem 4

# def Res(n):
#     if n==0:
#         return 1
#     else:
#         return n + Res(n-1)    

# sum = Res(4)
# print(sum)


#  Problem 5

# def Star(n):
#     for i in range(n):
#         print("*" * (n-i))

# n= 4 
# Star(n)       


#  Problem 6

# def cm(n):
#     return n * 2.54

# print(cm(4))



#  Problem 7


def Strip(String,word):
    newstr = String.replace(word, " ")
    return newstr


this = "  This  Is Mabtoor Mabx  "
n= Strip(this, " ")
print(n)
print(n.strip())




#  Problem 8

# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i} ")


# table(5)