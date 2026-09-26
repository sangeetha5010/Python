num=int(input("Enter the number"))
if(num>0):
    print("Positive number")
elif(num<0):
    print("Odd number")
else:
    print("Number is zero")

a=23
if(a%2==0):
    print("Even")
else:
    print("Odd")

n=int(input("Enter the number"))
for i in range(1,n+1):
    print(i)




n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")


n=int(input("Enter the number"))
if(n%3==0 and n%5==0):
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")


n=int(input("Enter the number"))
sum=0
for num in range(1,n+1):
    sum+=num

print(f"Total sum={sum}")

num=int(input("Enter the number:"))
count=0
while num!=0:
    num=num//10
    count+=1
print("Number of digits: ",count)



