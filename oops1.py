class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display_info(self):
        print(f"Brand={self.brand}, Price={self.price}")

brand1=mobile("iPhone",120000)
brand2=mobile("Redmi",15000)

brand1.display_info()
brand2.display_info()


class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"{self.name} scored {self.marks} marks.")

name1=Students("Sangeetha",97)
name2=Students("Keerthana",95)

name1.display_info()
name2.display_info()


class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating

    def info(self):
        print(f"The title of the movie is {self.title} and its rating is {self.rating}.")

title1=Movie("Askash",1000)
title2=Movie("Rajakumara",10000)

title1.info()
title2.info()



class Employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary

    def info(self):
        print(f"Employee Name : {self.name} , designation : {self.designation} , salary : {self.salary}")

n1=Employee("Sangeetha","Manager",3600000)
n2=Employee("Keerathana","Data Analyist",3100000)
n3=Employee("Yashu","Web Development")

n1.info()
n2.info()
n3.info()
