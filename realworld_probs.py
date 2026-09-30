'''units=int(input("Enter the units in the electricity bill : "))
if(units<=100):
    bill=units*2
elif(units<=200):
    bill=(100*2)+(units-100)*3
else:
    bill=(100*2)+(200*3)+(units-200)*5

print("Electricity Bill = ",bill)'''



correct_pin=1234
trials=3
while trials>=1:
    pin=int(input("enter the pin"))
    if pin!=correct_pin:
        trials-=1
        print("Incorrect Pin!")
        print("Try Again")
    else:
        print("Correct Pin")
        break
    

    



total_sum=0
num=int(input("enter the number(0 to stop) : "))
while num!=0:
    total_sum+=num
    num=int(input("Enter the number"))

print("Sum of numbers =", total_sum)



num=int(input("Enter the number : "))
count=0
while num!=0:
    num=num//10
    count+=1
print("No. of digits are : ",count)

num=int(input("Enter the number : "))
reverse=0
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print("the reverse number is : ",reverse)