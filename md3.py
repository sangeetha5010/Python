class Student:
    def __init__(self,roll_no,name):
        self.name=name
        self.roll_no=roll_no
        self.__marks={}

    def get_marks(self):
        return self.__marks

    def add_marks(self,subject,marks):
        self.__marks[subject]=marks

    def calculate_avg(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
        avg=total/len(self.__marks)
        return avg

    def is_passed(self):
        is_passed=all(mark<35 for mark in self.__marks.values())
        if is_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calculate_grade(self):
        print("Grade: ",end="")
        percentage=self.calculate_avg()*100
        if percentage>=90:
            print("A")
        elif percentage>=75 and percentage<90:
            print("B")
        else:
            print("C")

class ReportCard:
    @staticmethod
    def generate(student:Student):
        student_marks=student.get_marks()
        print(f"Name : {student.name}\t Roll No. {student.roll_no}")
        print("---Marks------")
        for subject,marks in student_marks.items():
            print(f"{subject} : {marks}")
        print("-----")
        print(f"Average: {student.calculate_avg()}")
        student.is_passed
        student.calculate_grade()


class ClassRoom:
    def __init__(self,grade,section):
        self.grade=grade
        self.section=section
        self.__students=[]

    def add_student(self,student):
        self.__students.append(student)

    def calculate_class_average(self):
        pass
    def get_students_list(self):
        for students in self.__students:
            print(f"{students.roll_no}. {students.name}")

a=Student(1,"Sangeetha")
a.add_marks("math",95)
a.add_marks("science",95)

c=ClassRoom("10","B")
c.add_student(a)
b=Student(2,"Bharath")
c.add_student(b)




from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []


class Transaction:
    def __init__(self, user, book):
        self.user = user
        self.book = book
        self.borrow_date = datetime.now()
        self.due_date = self.borrow_date + timedelta(days=7)
        self.return_date = None

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.transactions = []


    def add_book(self, book):
        self.books[book.book_id] = book

    
    def add_user(self, user):
        self.users[user.user_id] = user

   
    def view_available_books(self):
        for book in self.books.values():
            if book.is_available:
                print(book.book_id, book.title, "-", book.author)

    
    def borrow_book(self, user_id, book_id):
        user = self.users.get(user_id)
        book = self.books.get(book_id)

        if book and book.is_available:
            book.is_available = False
            user.borrowed_books.append(book)
            transaction = Transaction(user, book)
            self.transactions.append(transaction)
            print(f"{user.name} borrowed '{book.title}'")
            print(f"Due date: {transaction.due_date.date()}")
        else:
            print("Book not available")

    
    def return_book(self, user_id, book_id):
        user = self.users.get(user_id)
        book = self.books.get(book_id)

        for transaction in self.transactions:
            if transaction.book == book and transaction.user == user and transaction.return_date is None:
                transaction.return_date = datetime.now()
                book.is_available = True
                user.borrowed_books.remove(book)

                if transaction.return_date > transaction.due_date:
                    late_days = (transaction.return_date - transaction.due_date).days
                    penalty = late_days * 10  # ₹10 per day
                    print(f"Late return! Penalty: ₹{penalty}")
                else:
                    print("Returned on time!")

                return

        print("Transaction not found")