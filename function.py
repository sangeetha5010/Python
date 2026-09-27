'''def greet():
    print("Hello Eveyone!, My name Sangeetha")
greet()

def greet(name):
    print(f"Good Evening {name}.")
greet("Sangeetha")


def add_numbers(a,b):
    return a+b
result=add_numbers(3,4)
print("Sum = ",result)'''

n=int(input("Enter the numer: "))
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
    else:
        print("It is a prime")

'''def isprime(n):
    for i in range(2,n):
        if(n%i)==0:
           print("Number is not prime")
           break
        else:
           print("It is a prime")

isprime(7)'''