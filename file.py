file=open("students.txt","w")
names=[]
for i in range(4):
    n=input(f"Enter the name {i+1} : ")
    names.append(n)
    file.write(f"{names}\n")
print(names)

file.close()



file=open("marks.txt","w")

student_marks=[]
for i in range(3):
    for j in range(3):
        n=input(f"Enter the name {i+1} : ")
        m=int(input("enter the marks : "))
        student_marks[n[i]]=m[j]
        student_marks.append(n)
        file.write(f"{student_marks}\n")
print(student_marks)

file.close()