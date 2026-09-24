#logical operator
num1=int(input("Enter the first value: "))
num2=int(input("Enter the second value: "))
print(num1>10 and num2>10)
print(num1<5 or num2<5)
print(not(num1>num2))
    
#relational operator
age=int(input("Enter your age: "))
if(age>=18):
    print("You are adult")
else:
    print("You are minor")


#membership operator
a=input("Enter a string: ")
print("a" in a)
print("Python" not in a)