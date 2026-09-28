class Amount:
    def __init__(self,id,holder_account):
        self.id=id
        self.holder_account=holder_account
        self._balance=0

    def check_balance(self):
        print(f"Balance : {self._balance}")

    def deposit(self,amount):
        self._balance+=amount
        print(f"Deposited Sucessfully.The total balance is : {self._balance}")

    def withdraw(self,amount):
        if self._balance>=0:
            self._balance-=amount
            print("The amount is sucessfully withdraw")
            print(f"The total balance is : {self._balance}")
        else:
            print("Your balance is zero")


class SavingAmount(Amount):
    def cal_intrest(self):
        interest_rate=0.04
        interest=self._balance*interest_rate
        print(f"Interest : {interest}")


class CurrentAmount(Amount):
    def withdraw(self,amount):
        overdraft_limit=1000
        if self._balance + overdraft_limit>=amount:
            self._balance-=amount
            print("The amount is sucessfully withdraw")
            print(f"The total balance is : {self._balance}")
        else:
            print("Your balance is zero")


class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={}

    def create_acc(self,id,holder_name,type):
        if type=="saving":
            new_acc=SavingAmount(id,holder_name)
        elif type=="current":
            new_acc=CurrentAmount(id,holder_name)
            self.__account[id]=new_acc
            print("Account Created successfully")
            return new_acc
        
    def get_acc(self):
        if id not in self.__account:
            print("ID not found")
            return None
        else:
            account=self.__account[id]
            print(f"ID : {account.id}\n Holder Name : {account.holder_name}\n Type : {account.type}")
            return account    

sbk=Bank("sangeetha bank of Karnataka","Bangalore")


s1=sbk.create_acc("1","Keertahna","saving")
c1=sbk.create_acc("2","Yashu","current")

s1.deposit(1000)
c1.deposit(10)

s1.withdraw(4000)
c1.withdraw(50)

s1.cal_intrest()



#4
class Student:
    def __intit__(self,roll_no,name):
        self.name=name
        self.roll_no=roll_no
        self.__marks={}

    def get_marks(self):
        return self.__marks

    def add_marks(self,subject,marks):
        self.__marks[subject]=marks

    def calculate_avg(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
        avg=total/len(self.__marks)
        return avg

    def is_passed(self):
        is_passed=all(mark<35 for mark in self.__marks.values())
        if is_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calculate_grade(self):
        print("Grade: ",end="")
        percentage=self.calculate_avg()*100
        if percentage>=90:
            print("A")
        elif percentage>=75 and percentage<90:
            print("B")
        else:
            print("C")

class ReportCard:
    @staticmethod
    def generate(student:Student):
        student_marks=student.get_marks()
        print(f"Name : {student.name}\t Roll No. {student.roll_no}")
        print("---Marks------")
        for subject,marks in student_marks.items():
            print(f"{subject} : {marks}")
        print("-----")
        print(f"Average: {student.calucalate_avg()}")
        student.is_passed
        student.calculate_grade()


a=Student(1,"Sangeetha")
a.add_marks("math",95)
a.add_marks("science",95)

ReportCard.generate()





