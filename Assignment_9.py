#  Problem 1


# f = open("poems.txt" , "r")
# t = f.read()
# if "Twinkle" in t:
#     print("Twinkle Is Present In File")
# else:
#     print("Twinkle Is Not Present In File")    


#  Problem 2

# def Game():
#     return 543

# score = Game()

# with open("hiscore.txt") as f:
#     Hiscore = f.read()

# if Hiscore=="":
#     with open("hiscore.txt", "w") as f:
#         f.write(f"{score}")
# elif int(Hiscore)<score:
#     with open("hiscore.txt", "w") as f:
#         f.write(f"{score}")



# Problem 3

# for i in range(2,21):
#     with open(f"Multiplication table Of {i} is.txt", "w") as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j} = {i*j} \n")



#  Problem 4

# with open("read.txt" ) as f:
#     content = f.read()

# content = content.replace("Donkey", "#$%^&@^&")

# with open("read.txt", "w") as f:
#     f.write(content)



#  Problem 5

# content = ["BC", "MotherFucker", "Asshole", "Bhosdike", "MotherFucker", "Donkey"]

# with open("read.txt") as f:
#     cont= f.read()

# for content in cont:
#     cont = cont.replace(content, "#$%@&*$#$")
#     with open("read.txt", "w") as f:
#         f.write(cont)




#  Problem 6

# with open("log.txt") as f:
#     file= f.read()

# if "python" in file.lower():
#     print("Python Is Present In Log File")
# else:
#     print("Python IS Not Present In Log File")    



#  Problem 7


# content = True
# i =1 

# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if "python" in content.lower():
#             print(f"Python Is Present In Line {i}")
#         i+=1       
# 

#  Problem 8

# with open("read.txt") as f:
#     copy =f.read()

# with open("copy.txt", "w") as f:
#     f.write(copy)



#  Problem 9


# read = "read.txt"
# copy = "copy.txt"

# with open("read.txt") as f:
#     read1 = f.read() 

# with open("copy.txt") as f:
#     read2 = f.read()

# if read1==read2:
#     print("Files Are Identical")
# else:
#     print("Files Are Not Identical")



#  Problem 10


# with open("read.txt", "w") as f:
#     f.write("")



#  Problem 11

import os

with open("read.txt") as f:
    content = f.read()

with open("renamefile.txt", "w") as f:
    f.write(content)

    os.remove("read.txt")