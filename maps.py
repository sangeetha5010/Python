num=[1,2,3,4,5]
def double(x):
    return x**2
res=map(double,num)
print(list(res))

num=[1,2,3,4,5]
res=map(lambda x: x**2,num)
print(list(res))


num=[8,9,3,8,4,0]
def is_odd(x):
    return x%2!=0
res=filter(is_odd,num)
print(list(res))

num=[8,9,3,10,4,0]
res=filter(lambda x: x%2==0,num)
print(list(res))


from functools import reduce
list=[1,2,3,4,5]
def add(s,k):
    return s+k
res=reduce(add,list)

num=[8,9,3,10,4,0]
res=reduce(lambda a,b:a if a>b else b,num)
print(res)



scores=[25,36,85,74,55]
updated=list(map(lambda x:x+5,scores))
passed=list(filter(lambda x:x>=50,updated))
total=reduce(lambda x,y:x+y,passed)

print("Updated scores is:",updated)
print("passed students are: ",passed)
print("Total Marks is: ",total)