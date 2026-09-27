
for i in range(1,11):
        print(i)

for i in range(0,11,2):
    print(i,end=" ")
    
    
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")

names=["sangeetha","keerthana","yashu","sanvi","bhavana"]
for index,name in enumerate(names):
    if name=="sanvi":
        continue
    print(f"{index+1}:{name}")

laddus=5
names=["sangeetha","keerthana","yashu","sanvi","bhavana"]
for name in names:
    if laddus>0:
        print(f"{name} get a laddu!")
        laddus-=1
    else:
        print("NO laddus!")


total_sum=0
for num in range(1,11):
    total_sum+=num
print(f"The sum of numbers:{total_sum}")



text="Hello World!"
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count+=1

print("Number of vowels in a string:",count)


n=int(input("Enter the numer: "))
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
    else:
        print("It is a prime")


for num in range(10,51):
    is_prime=True
    if num<2:
        is_prime=False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
    if is_prime:
        print(num,end=" ")


n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial:",fact)
