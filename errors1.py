age=int(input("enter your age : "))

try:
    a=100-age
    print(f"In {a} years you will be 100 years old.")
except ValueError:
    print("Error ")
else:
    print("Progarm ran successfully")
finally:
    print("Program Ended")




try:
    a=int(input("Enter a : "))
    b=2
    div=a/b
    print(div)
except ZeroDivisionError as e:
    print(f"Error : {e}")
except ValueError:
    print("Error:Please enter a valid number.")
else:
    print("There is no error")
finally:
    print("Program ended!")


try:
    file=input("enter the file you want to open : ")
    a=open(file)
    contents=a.read()
    print(contents)
    a.close
except:
    print("Error")


file=open("students.txt","w")
names=[]
for i in range(4):
    n=input(f"Enter the name {i+1} : ")
    names.append(n)
    file.write(f"{names}\n")
print(names)

file.close()


from collections import namedtuple
Data=namedtuple('Data','IDs,MARKS,CLASS,NAME')
n=int(input("Enter the total number of students: "))
x=Data(IDs=1,MARKS=98, CLASS=12,NAME="Sangeetha")
x=Data(IDs=2,MARKS=95, CLASS=1,NAME="keer")
x=Data(IDs=3,MARKS=94, CLASS=2,NAME="yashu")
x=Data(IDs=4,MARKS=99, CLASS=11,NAME="Sange")
print(x)


