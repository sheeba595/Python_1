# 1. Define a function greet_user() that prints "Hello, User!" when called. 
def greet():
    print("Hello , User!")
greet()

# 2. Create a function calculate_sum(a, b) that takes two numbers as arguments and returns their sum. 
def calculate_sum(a,b):
    return a+b
print(calculate_sum(10,10))

# 3. Write a function check_positive(num) that takes a number as input. If the number is positive, return "Positive", else use the pass statement. 

def check_positive(num):
    if(num>=0):
        return ("Positive number")
    else:
        pass
num=int(input("Enter number: "))
print(check_positive(num))

# 4. Create a function find_max(a, b, c) that takes three numbers and returns the maximum among them using the return statement.
def find_max(a,b,c):
    if (a>=b and a>=c):
        return (f"{a} is maximium")
    elif (b>=a and b>=c):
        return (f"{b} is maximum")
    else:
        return (f"{c} is maximum")
print(find_max(10,20,30))
        
        
# 5. Demonstrate global and local variables by defining a global variable count = 10
# and modifying it inside a function using global count.

count = 10  # global variable

def modify_count():
    global count
    count = count + 5

modify_count()
print("Updated global count:", count)


# 6. Write a function modify_variable() where a local variable message = "Local Scope"
# is declared. Print this inside and outside the function to show scope difference.

def modify_variable():
    message = "Local Scope"  # local variable
    print("Inside function:", message)

modify_variable()

# print(message)  # This will cause an error because message is local to the function


# 7. Write a recursive function factorial(n) to find the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 8. Create a recursive function fibonacci(n) that returns the nth Fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("5th Fibonacci number:", fibonacci(5))


# 9. Write a function sum_numbers(*args) that takes multiple numbers and returns their sum.

def sum_numbers(*args):
    return sum(args)

print("Sum:", sum_numbers(1, 2, 3, 4, 5))


# 10. Create a function print_student_details(**kwargs) that takes keyword arguments
# like name, age, and grade, and prints them.

def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_details(name="Sheeba", age=20, grade="A")


# 11. Create a function apply_operation(func, a, b) that takes a function and two numbers
# as arguments. Pass lambda x, y: x + y as an argument and return the sum.

def apply_operation(func, a, b):
    return func(a, b)

result = apply_operation(lambda x, y: x + y, 5, 3)
print("Result:", result)


# 12. Write a function outer_function() that defines an inner function inner()
# inside it and returns "Hello from Inner Function".

def outer_function():
    def inner():
        return "Hello from Inner Function"
    return inner()

print(outer_function())


# 13. Use map() function to double each element of a given list [1, 2, 3, 4, 5].

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled list:", doubled)
