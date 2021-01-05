#  Problem 1
# class Employee:
#     def __init__(self, name, company):
#         self.name = name
#         self.company=company

#     def Show(self):
#         print(f"The Name Of The Person is {self.name} and The Company Of The Person is {self.company}")



# Mabx = Employee("Mabtoor", "Youtube")
# Waqas = Employee("Waqas", "Google")
# Harry = Employee("Horair", "Microsoft")
# Waheed = Employee("Waheed", "Apple") 
# Mabx.Show()
# Harry.Show()
# Waheed.Show()
# Waqas.Show()


#  Problem 2


# class Calculator:
#     def __init__(self , number):
#         self.number= number
#     def Square(self):
#         print(f"The Square of {self.number} is {self.number**2}")

#     def SquareRoot(self):
#         print(f"The Square Root of {self.number} is {self.number**0.5}")
    
#     def Cube(self):
#         print(f"The Cube Of {self.number} is {self.number**3}")


# Calc = Calculator(4)
# Calc.Square()
# Calc.SquareRoot()
# Calc.Cube()





#  Problem 3

# class Sample:
#     company = "Google"


# Object = Sample()
# Sample.company= "Microsoft"
# Object.company= "Youtube"

# print(Sample.company)
# print(Object.company)


#  Problem 4


# class Calculator:
#     def __init__(self,number):
#         self.number = number

#     def Square(self):
#         print(f"The Square Of {self.number} is {self.number**2}")
#     def SquareRoot(self):
#         print(f"The Square Root Of {self.number} is {self.number**0.5}")
#     def Cube(self):
#         print(f"The Cube Of {self.number} is {self.number**3}")

#     @staticmethod
#     def greet():
#         print("**** WELCOME TO THE MASTER CALCULATOR *******")


# Calc = Calculator(5)
# Calc.greet()
# Calc.Square()
# Calc.SquareRoot()
# Calc.Cube()




#  Problem 5

 
class Train:
    def __init__(self, Name, Seats, Fare):
        self.Name= Name
        self.Seats = Seats
        self.Fare = Fare

    def Status(self):
        print(f"The Name Of The Train is {self.Name}")
        print(f"The Seats Avalible in Train is {self.Seats} ")
    
    def FareInfo(self):
        print(f"The Price Of The Ticket is {self.Fare}")

    def BookTicket(self):
        if (self.Seats)>0:
            print(f"Your Seat Has Booked! Your Seat No is  {self.Seats}")
            self.Seats = self.Seats -1
        else:
            print("Sorry! This Train Is Full")


Millat = Train("MillatExpress", 21, 12000)
Millat.Status()
Millat.FareInfo()
Millat.BookTicket()
Millat.Status()



#  Problem 6


# class Sample:
#     def Greet(Mabx):
#         print("Good Morning")

# Mabx = Sample()
# Mabx.Greet()