#  PRACTICE ______

# class Name:
#     def Func(self):
#         return self.a+self.b
    
# add= Name()

# add.a  = 76
# add.b  = 10
# s = add.a+ add.b
# print(s)



#  PRACTICE _______


class Employee:
    company ="Google"
    Salary = 232122

Mabx = Employee()
Harry=Employee()
Waqas = Employee()
print(Mabx.company)
print(Harry.company)
print(Waqas.company)

Employee.company = "Youtube"   # Class Attribute
print(Mabx.company)
print(Harry.company)
print(Waqas.company)

Mabx.company= "Whatsapp"          # Instance Attribute
print(Mabx.company)
print(Harry.company)
print(Waqas.company)

Mabx.Salary = 233333

print(Mabx.Salary)
print(Harry.Salary)
print(Waqas.Salary)




