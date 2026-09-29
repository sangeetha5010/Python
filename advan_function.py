mul=lambda a,b : a*b
print(mul(2,3))


def sum():
    total=0
    num=int(input("Enter the number : "))
    for i in range(1,num+1):
        total+=num
        
    print("total=",total)

sum()


def sum_natural(n):
    if n == 0:          
        return 0
    else:
        return n + sum_natural(n-1)

n = int(input("Enter a number: "))
result = sum_natural(n)

print("Sum of first", n, "natural numbers =", result)


def find_average(*numbers):#argunments
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

result = find_average(10, 20, 30, 40)
print("Average =", result)
    

#keyword argunmnets
def students_info(**detials):
    for name,marks in detials.items():
        print(f"{name}:{marks}")
students_info(name="Sangeetha",marks=97)
