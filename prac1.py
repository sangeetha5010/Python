'''word="Sangeetha"
vowels="aeiouAEIOU"
count=0
for char in word:
    if char in vowels:
        count+=1
print(count)

word="level"
a=input("Enter the word: ")
if word==a[::-1]:
    print("same")
else:
    print("not same")

list=[1,2,3,4,5]
count=0
for i in list:
    count+=1
print(f"The lenght of the list is {count}")
    


sen="My name is Sangeetha"
a=sen.split()
print(a)
count=0
for i in a:
    count+=1
print(f"the number of words in the sentance is {count}")


name="Sangeetha"
a=name[::-1]
print(a)'''


sen=input("Enter the sentance: ")
s=sen.split()
print(s)
count={}
for char in s:
    cahr=char.lower()
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print("Word counts:")
for char in count:
    print(char, ":", count[char])  


'''n=10
while n != 1: 
    print(n, end=", ") 
    if n % 2 == 0: 
        n = n // 2 
    else:                 
        n = n * 3 + 1
    print(n, end=".\n")



list=[10,20,30,50,28]
print("Original list : ",list)
list.insert(2,25)
print(list)

list.append(40)
print(list)

list.remove(25)
print(list)

print(len(list))

list.pop()
print(list)

list.clear()
print(list)



A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
result=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        
        result[i][j]+=A[i][j]+B[i][j]

print(result)'''


dict={"name":"Sangeetha",
      "branch":"CSE"}
dict["section"]="F"
print(dict)
del dict["branch"]
print(dict)

d1 = {"a": 1, "b": 2}
d2 = d1   # aliasing 
d2["a"] = 100 
print(d1) 
print(d2)

for key,value in dict.items():
    print(f"{key}:{value}")


a="level"
name=input("enter the name")
n=name[::-1]
if n==a:
    print("Same")
else:
    print("Different")