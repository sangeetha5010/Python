class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        self.__balance+=amount
        if self.__balance>0:
             print(f"Balance : {self.__balance}")
        else:
            print("Your Balance is zero")

b=BankAccount(0)
print(b.get_balance())
print(b.set_balance(400))



class Calculator:
    def multiply(self,a,b,c=1):
        return a*b*c
    
c=Calculator()
print(c.multiply(1,2))
print(c.multiply(1,2,3))


class Shape:
    def draw(self):
        print("Drawing Shapes")
    
class Circle(Shape):
    def draw(self):
        print("Drawing circle")


c=Circle()
c.draw()



from abc import ABC, abstractmethod
class Empolyee(ABC):
    @abstractmethod
    def cal_salary(self):
        pass
class Post(Empolyee):
    def cal_salary(self):
        return super().cal_salary()
        print("Post's salary is calculated")
