# Read The File Through Read Mode Open Function
# 
#  File = open("another.txt" , "r")
# Fill= File.read()
# print(Fill)
# File.close()


#  ReadLine Function Is Used To Read A Single Line In File I/O
f = open("another.txt")
print(f.readline())
# Write Something in File Through Write Mode in Open Function

# f = open("another.txt", "w")
# fiel = f.write("Hello guys! My Name Is Mabtoor Ul Shafiq")
# fiel = f.write("This Is Going to Be Really Amazing!")
# f.close()

#  Add Text In The Last Through Append Mode In Open Function

# f = open("another.txt", "a")
# f.write("Please Subscribe My Channel And Press The Bell Icon For More Updates")
# f.close()


#  Using With Function Instead Of Open Function So That It can Close The File Automatically


# with open("another.txt", "w") as f:
#     Close=f.write("Hello Pakistanio!")