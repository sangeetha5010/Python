#tuple
names=["sangeetha","keerthana","yashu","sanvi"]
names.append("bhavana")
print(names)
names.insert(1,"anjana")
print(names)
names.remove("yashu")
print(names)

nums=[5,3,8,4,0,2]
a=sorted(nums)
print(a)
a.reverse()
print(a)

t=(1,2,3,4,5,6,7)
b=(23,4,5,26,98)
print(t[1:4])
print(type(t))
a=t+b #adding two tuple 
print(a)


s={"mango","strawberry","watermelon","grapes"}
k={"banana","orange","grapes"}
a=s|k
print(a)
a=s&k
print(a)
a=s-k
print(a)

s.remove("grapes")
print(s)
k.discard("orange")
print(k)