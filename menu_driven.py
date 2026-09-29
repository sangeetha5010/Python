'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


while True:
    print("### Simple Multiplication ###")
    print("1.Add")
    print( "2.Subtraction") 
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice : "))

    if choice in {1,2,3,4}:
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))
    
    

    if choice==1:
        print("Result: ",add(a,b))
    elif choice==2:
        print("Result: ",sub(a,b))
    elif choice==3:
        print("Result: ",mul(a,b))
    elif choice==4:
        if b==0:
            print("Error:Division by zero is not allowed")
        else:
            print("Result: ",div(a,b))
    elif choice==5:
        print("Quitting..")
        break
    else:
        print("Invalid Choice")





#2
def bankingSystem():
    balance=0
    while True:
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice=int(input("Enter the choice : "))
        if choice==1:
            print(f"Your current balance is = {balance}")


        elif choice==2:
            try:
                amount=int(input("Enter the amount to deposite : "))
                if amount<=0:
                    print("Amount must be greater than zero")
                else:
                    balance+=amount
                    print(f"The total amount in the bank is : {balance}")
            except ValueError:
                print("Invalid input")


        elif choice==3:
            try:
                amount=int(input("Enter the amount to withdraw : "))
                if amount<=0:
                    print("Amount must be greater than zero")
                elif amount>balance:
                    print("Insufficient balance")
                else:
                    balance-=amount
                    print(f"Total balance is : {balance}")
            except ValueError:
                    print("Invalid input")


        elif choice==4:
            print("Exitting")
            break
        else:
            print("Invalid Choice")

bankingSystem()


#3
menu={
        "Chocolate":50,
        "Biscuit":30,
        "Soaps":40
          }
while True:
    print("### Grocery Stored Items ###")
    print("Select the following Options")
    print("1.Add")
    print("2.Remove")
    print("3.View Cart and Total price")
    print("4.Exit")
    choice=int(input("Enter the choice(1-3) : "))

    if choice==1:
        add=input("Enter the item to add : ")
        amt=int(input("Enter the amount of the item : "))
        menu[add]=amt
        print(menu)
        print("Items Added")

    elif choice==2:
        rmve=input("Enter the items to remove")
        found=False
        for i in menu:
            if i[0]==rmve:
                menu.remove(i)
                found=True
                print("Item removed")
                break
        if not found:
            print("Items not found")

    elif choice==3:
        total=0
        print("\nYour cart: ")
        for item in menu:
            print(item, "-" ,menu[item])
            total+=menu[item]
        print("total Price : ",total)
     

    elif choice==4:
        print("Thank You!")
        break


    else:
        print("Invalid Choice")'''





#4
list=[]
while True:
    print("### Educational System ###")
    print("1.Adding students detals")
    print("2,Display students details")
    print("3.Exit")
    choice=int(input("Enter the choice(1-3) : "))
    
    if choice==1:
        n=int(input("enter the number of students"))
        for i in range(n):
            name=input("Enter the student's name : ")
            mark=int(input("Enter the student's marks : "))
            list.append([name,mark])
        print("Added in to the list")


    elif choice==2:
        print("--Students Detalis--")
        for i in list:
            print(i[0] ,"-",i[1])

    elif choice==3:
        print("Exiting......")
        break

    else:
        print("Invalid Choice")
