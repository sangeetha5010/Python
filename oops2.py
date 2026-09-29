class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber=accountNumber
        self.__balance=balance

    def bl(self):
        print(f"Balance : {self.__balance}")

    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited Amount : {amount}. New Balance : {self.__balance}")

    def withdraw(self,amount):
        self.__balance-=amount
        print(f"Withdraw Amount : {amount}. New Balance : {self.__balance}")


ba=BankAccount(12234,2000)
ba.bl()
ba.deposit(3000)
ba.withdraw(500)


class Phone:
    def __init__(self,brand):
        self.brand=brand

    def call_contact(self,name):
        print(f"Calling to {name}.")

    def take_picture(self):
        print("Lets take a photo for a memories")

p=Phone("iPhone")
p.call_contact("Sangeetha")
p.take_picture()

class Vehical:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print("The Car started now!")


class Bike(Vehical):
    def ride(self):
        print("The bike is riding!")

b=Bike("xyz")
b.ride()
b.start()



class Shape:
    def area(self,r,l,b):
        self.r=r
        self.l=l
        self.b=b

class Circle(Shape):
    def area(self,r,l,b):
        cal_area=3.14*r*r
        print(f"Area of Circle : {cal_area}")

class Rectangle(Shape):
    def area(self,r,l,b):
        cal_area=l*b
        print(f"Area of rectangle : {cal_area}")

shapes=[Circle(),Rectangle()]
for Shape in shapes:
    Shape.area(3,4,5)
    
