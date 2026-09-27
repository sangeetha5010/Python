for i in range(1,31):
    print(f"3X{i}={3*i}")

n=int(input("Enter the numeber"))
total=0
for i in range(1,n+1):
    total+=i
print(total)

a="Sangeetha"
vowels="aeiouAEIOU"
count=0
for char in a:
    if char in vowels:
        count+=1

print("Number of vowels are: ",count)

name="Sangeetha"
for letter in name:
    print(letter,end=" ")