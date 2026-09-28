num=int(input("Enter the number: "))
match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _:
        print("Other number")


time=14
is_hungry=False
match time:
    case 9:
        print("breakfast")
    case 13 |14:
        print("lunch")
    case 17 if is_hungry:
        print("Snacks")
    case 20:
        print("Dinner")
    case _:
        print("Do Work")

letter=input("Enter a single letter: ")
match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Vowel")
    case _:
        print("Consonant")




# Input point
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

point = (x, y)

match point:
    case (0, 0):
        print("Point is at Origin")
    case (0, y) :
        print("Point lies on Y-axis")
    case (x, 0):
        print("Point lies on X-axis")
    case (x, y) if x>0 and y<0:
        print("Point lies 4th quadranty")
    case (x, y) if x>0 and y>0:
        print("Point lies 1th quadranty")
    case (x, y) if x<0 and y>0:
        print("Point lies 2th quadranty")
    case (x, y) if x<0 and y<0:
        print("Point lies 3th quadranty")
    case _:
        print("Invalid inpuut")


command = input("Enter command (start/stop/pause): ").lower()

match command:
    case "start":
        print("System is starting...")
    case "stop":
        print("System is stopping...")
    case "pause":
        print("System is paused...")
    case _:
        print("Invalid command")


