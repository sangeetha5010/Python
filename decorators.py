def welcome(func):
    def wrapper():
        print("Namaskara!")
        func()
        print("Take care!")
    return wrapper

@welcome
def intro():
    print("I am Chandan from Karnataka.")
intro()

@welcome
def bye():
    print("Byeeee")
bye()


def greeting(func):
    def wrapper(name):
        func(name)
        print(f"{name} is a good girl and har working")
        func(name)
    return wrapper


@greeting
def greet(name):
    print(name)
greet("Sangeetha")


def log_function_call(func):
    def wrapper(name,time):
        print(f"{name}-Called at {time}")
        func(name,time)
    return wrapper


@log_function_call
def add(name,time):
    print(name,time)
add("Keer",6)
    
   

import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper

@timer
def long_task():
    time.sleep(4) 

long_task()


def add_lines(func):
    def wrapper():
        print("===")
        func()
        print("===")
    return wrapper

def add_arrow(func):
    def wrapper():
        print(">>> ", end="")
        func()
    return wrapper

@add_lines
@add_arrow
def show_name():
    print("Sangeetha")
show_name()


def allow_only(func):
    def wrapper(name):
        if name != "admin":
            print("Access Denied")
        else:
            func(name)
    return wrapper

@allow_only
def view_data(name):
    print(f"Welcome {name}, you can view the data.")


view_data("admin")  
view_data("user")   