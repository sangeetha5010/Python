'''class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display_info(self):
        return f"Name-{self.name},Grade-{self.grade}"
s=Student("Riya",19)
print(s.display_info())


d1={"name":"Sangeetha","age":19}
d2=d1.copy()
d2['name']="Poornima"
print(d1)
print(d2)

d1={"name":"Sangeetha","age":19}
d2=d1
d2["age"]=21
print(d1)
print(d2)

import numpy as np
ls=np.linspace(0,1,7)
print(ls)

import numpy as np
s=np.array([1,5,8,10,2,3])
print(s.shape)


import numpy as np
num=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
num[1:8:2]=16
print(num)


import numpy as np
students=np.array([50,97,89,78])
bonus=5
final=students+bonus
for num in final:
    if num>=100:
        num-=5
        print(num)
        final.append(num)
print(final)


import csv
with open("sample.csv") as f:
    data=list(csv.DictReader(f))
print("Column-",list(data[0].keys()))
col=input("Enter the column name: ")
nums=[]
for row in data:
    try:
        nums.append(float(row[col]))
    except:
        pass
op=input("Type(max/min/avg): ")
if op=="max":
    print("Maximum: ",max(nums))
elif op=="min":
    print("Minimum: ",min(nums))
elif op=="avg":
    print("Average: ",sum(nums)/len(nums))
else:
    print("Incorrect Input")


a={"name":"Sangeetha","marks":90}
b=a.copy()
b["name"]="Keer"
print(a)
print(b)

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.zeros((2,3))
c=np.ones((1,2))
d=np.arange(0,20,1)
e=np.linspace(0,1,4)
print(a)
print(b)
print(c)
print(d)
print(e)


s=np.array([[1,2,3],[8,2,6]])
print(s.shape)

k=np.array([1,2,3,4,5,6])
a=k.reshape(2,3)
print(a)

import numpy as np
marks = np.array([85, 97, 78, 92])
bonus = 5
final = []
for i in marks:
    if i+bonus<=100:
        final.append(int(i+bonus))
    else:
        final.append(int(i))
print(final)

with open("friends.txt", "r") as input_file:
    all_lines = input_file.readlines()
all_lines.sort() 
with open("sortedfriends.txt", "w") as output_file: 
  for line in all_lines:
    output_file.write(line) 

print("Divisible by 3 or 5 and not both are:")
for i in range(1, 101):

    # Skip numbers divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        continue

    # Print numbers divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        print(i,end=" ")
n=int(input("Enter the number"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
n=int(input("Enter the number"))
if n>0:
    print("Even number")
elif n<0:
    print("Negative number")
elif n==0:
    print("Number is zero")
else:
    print("Invalid input")


n=int(input("Enter the number"))
num=[]
for i in range(n):
    value=int(input("Enter the number: "))
    num.append(value)
print(num)
eve_num=[]
for i in num:
    if i%2==0:
       eve_num.append(i)
print(eve_num)

import numpy as np
matrix=np.random.randint(1,101,size=(2,3))
print("Original Shape(3X3):")
print(matrix)
print("\nShape: ")
print(matrix.shape)
print("\nTranspose of Matrix: ")
print(matrix.T)
print("\nMean of matrix: ")
print(matrix.mean())


class Animal:
    def speaks(self):
        print("Animal speaks")
class Dog(Animal):
    def speaks(self):
        print("Braks")
class Cat(Animal):
    def speaks(self):
        print("Meow")
d=Dog()
c=Cat()
d.speaks()
c.speaks()'''


class Shape:
    def area(self):
        print("Area of the shape")
class Rectangle:
    def __init__(self):
        self.l=int(input("Enter the length"))
        self.b=int(input("Enter the breath"))
    def arae(self):
        print("Area of rectangle: ",{self.l}*{self.b})
class Cirlce(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return {self.r}*{self.r}
        '''

class Employee: 
    def input(self): 
        self.id = int(input("ID:")) 
        self.name = input("Name:") 
    def display(self): 
        print(f"{self.id}-{self.name}") 
e = Employee() 
e.input() 
e.display() '''
