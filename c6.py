
#list
names=["Sangeetha","Keerthana","Yashu","Sanvi","Bhavana"]
print(names[4])
print(names[0:4])
print(names[:3])
print(names[::2])
names.append("Anjana")
print(names)
names.insert(4,"Anjana")
print(names)
names.remove("Bhavana")
print(names)
names.pop()
print(names)
print(names.index("Yashu"))
print(names)




nums=[8,5,9,6,23,13,6,46,79,6,35]
print(len(nums))
a=sorted(nums)
print(a)
print(sum(nums))
print(nums.count(6))
a.reverse()
print(a)

list=[]
for i in range(3):
    n=int(input("Enter the value"))
    list.append(n)

print(list)





