'''
numbers = [1, 2, 3] 
print(id(numbers))  

print("Arthematic Opertaions")
print("1.Add\t2.Subtract\t")
print("2.Subtract\t")
print("3.Multiply\t")
print("4.Division\t")
choice=int(input("Enter the choice from the above(1,2,3,4): "))
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("Invalid Input")

name=input("Enter your name: ")
year=int(input("enter the year of birth: "))
current_year=int(input("enter the current year: "))
age=current_year-year
if age>=60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")

n=int(input("Enter the value of n: "))
a,b=0,1
for i in range(n):
    print(a,end="")
    a,b=b,a+b

list=[1,2,3,4,5,8,9]
print(list)

list.insert(6,5)
print(list)

list.remove(4)
print(list)

list.append(10)
print(list)

print(len(list))

list.pop()
print(list)

list.clear()
print(list)


import math as m 
n=int(input("Enter the total number of value: "))
number=[]
for i in range(n):
    value=int(input("Enter the numbers: "))
    number.append(value)
print(number)
mean=sum(number)/n
std_dev=sum((x-mean)**2 for x in number)/n
var=m.sqrt(std_dev)
print("Mean = ",mean)
print("Standard Deviation = ",std_dev)
print("Variance = ",var)   

num=input("Enter the numbers: ")
print("The entered number is: ",num)
uniqnum=set(num)
for ele in uniqnum:
    print(ele,"occurs",num.count(ele),"times")

with open("input.txt","r") as infile:
    lines=infile.readlines()
data=[line.strip() for line in lines]
data.sort()
with open("output.txt","w") as outfile:
    for item in data:
        outfile.write(item+"\n")
print("File has been sorted successfully\n")
print("Sorted content is written to output.txt")

import sys
def DivExp(a,b):
    assert a>0,"a should be greater than 0"
    try:
        c=a/b
    except ZeroDivisionError:
        print("value of b cannot be zero")
        sys.exit(0)
    else:
        return c
val1=int(input("Enter the value for a: "))
val2=int(input("Enter the value of b: "))
val3=DivExp(val1,val2)
print(val1,"/",val2,"=",val3)

f = open("demofile.txt")
print(f.read())


with open ("demofile.txt") as f:
    print(f.readlines())

import os
current_directory=os.getcwd()
print(f"Current working directory: {current_directory}")

print("Directary is created successfully")

import os
dict=r"C:\Users\Smile"
conents=os.listdir(dict)
print(f"Conents of {dict} is: ")
for i in conents:
    print(i)'''


class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,grade):
        super.__init__(name)
        self.grade=grade
    def display_info(self):
        return f"Name-{self.name},Grade-{self.grade}"
s=Student("Riya",19)
print(s.display_info())
