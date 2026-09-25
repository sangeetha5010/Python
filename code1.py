with open("sample.txt","r") as file:
    text=file.read().lower()
words=text.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
sorted_word=sorted(freq.items(),key=lambda x:x[1],reverse=True)
print("10 most frequently Appearing words:\n")
for word,count in sorted_word[:10]:
    print(word,":",count)


import os
path=input("enter the path name: ")
for root,files,folders in os.walk(path):
    print("Directory-",root)
for folder in folders:
    print("Folders-",folders)
for file in files:
    print("Files-",files)

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,other):
        new_real=self.real+other.real
        new_imag=self.imag+other.imag
        return Complex(new_real,new_imag)
    def display(self):
        print(f"{self.real}+{self.imag}i")
n=int(input("Enter the number of complex number: "))
r=int(input("Enter the real value: "))
i=int(input("Enter the imaginary value: "))
total=Complex(r,i)
for k in range(n-1):
    r=int(input("Enter the real value: "))
    i=int(input("Enter the imaginary value: "))
    c=Complex(r,i)
    total=total.add(c)
print("Addition of complex number: ")
total.display()


student={}
n=int(input("Enter the total no. of students: "))
for i in range(n):
    name=input("Enter the name")
    marks=int(input("enter the marks: "))
    student[name]=marks
print("Students Detals\n")
for name,marks in student.items():
    print(name,":",marks)
avg=sum(student.values())/n
topper=max(student,key=student.get)
lower=min(student,key=student.get)
print("Summary Report\n")
print("Average Marks: ",avg)
print("Maximum: ",topper,"-",student[topper])
print("Minimum: ",lower,"-",student[lower])


class LibraryItem:
    def __init__(self,title):
        self.title=title
    def display(self):
        print("Library Item: ",self.title) 
class Book(LibraryItem):
    def display(self):
        print("Book Title: ",self.title)
class Magazine(LibraryItem):
    def display(self):
        print("Magazine title: ",self.title)
class ItemCount:
    def __init__(self,count):
        self.count=count
    def __add__(self,other):
        return ItemCount(self.count + other.count)
    def show(self):
        print("Total Items: ",self.count)
b1=Book("Python Programming")
m1=Magazine("Science Today")
b1.display()
m1.display()
count1=ItemCount(2)
count2=ItemCount(1)
total=count1+count2
total.show()

    