#if else conditional statments
gender=input("Enter the gender= ")
age=int(input("enter the age= "))
if gender=="female":
    print("Ticket is free.")
else:
    if age<=5:
        print("Ticket is free.")
    elif age<=12:
        print("Half ticket has to be paid.")
    elif age>=60:
        print("They get a senior citizen discount.")
    else:
        print("Citizen has to pay full ticket")
 

time=int(input("Enter the time"))
if time==8:
    print("It's time for breakfast")
elif time==13:
    print("It is lunch time")
elif time==20:
    print("It's dinner time")
else:
    print("It's not meal time")
    


age=int(input("Enter the age: "))
if age<=18:
    print("You get a student membership")
elif age>=60:
    print("You get a senior citizen membership")
else:
    print("You get a regular membership.")