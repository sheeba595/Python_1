
# 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

students = [
    Student("Alice", 85),
    Student("Bob", 78),
    Student("Charlie", 92)
]

for s in students:
    s.display()
    
# 2
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)

print(car1.__dict__)
print(car2.__dict__)   

# 3
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self):
        self.price *= 0.9

book = Book("Python 101", "John Doe", 500)
book.apply_discount()
print(book.title, book.price)

4.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print(c.area(), c.circumference())

5.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.balance)

6.
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

movies = [
    Movie("Inception", "Nolan", 9),
    Movie("Avengers", "Russo", 8),
    Movie("MovieX", "DirectorX", 7)
]

for m in movies:
    if m.rating > 8:
        print(m.title, m.rating)
        
7.
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram

l = Laptop("Dell", 8, 70000)
l.upgrade_ram(8)
print(l.ram)

8.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(5, 10)
print(r.area(), r.perimeter())

9.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def status(self):
        print("Adult" if self.age >= 18 else "Minor")

p = Person("Alice", 20)
p.status()

10.
class Temperature:
    def __init__(self, celsius=None, fahrenheit=None):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

    def to_celsius(self):
        return (self.fahrenheit - 32) * 5/9

t = Temperature(celsius=25)
print(t.to_fahrenheit())

11.
class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):
    def move(self):
        print("Car driving")

class Bike(Vehicle):
    def move(self):
        print("Bike riding")

Car().move()
Bike().move()

12.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

m = Manager("Alice", 50000, 10000)
print(m.name, m.salary, m.bonus)

13.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
    14.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

s = Student("Bob", 18, 90)
print(s.name, s.age, s.marks)

15.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

s = Student("Bob", 18, 90)
print(s.name, s.age, s.marks)

16.
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

Dog().make_sound()
Cat().make_sound()
17.
class Appliance:
    def switch_on(self):
        print("Appliance is on")

class WashingMachine(Appliance):
    def wash(self):
        print("Washing clothes")

class Refrigerator(Appliance):
    def cool(self):
        print("Cooling food")

w = WashingMachine()
w.wash()
r = Refrigerator()
r.cool()

18.
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary + 2000  # extra allowance

class Tester(Employee):
    def calculate_salary(self):
        return self.base_salary + 1000

dev = Developer("Alice", 50000)
test = Tester("Bob", 40000)
print(dev.calculate_salary(), test.calculate_salary())

19.
class Transport:
    def __init__(self, max_speed):
        self.max_speed = max_speed

class Bus(Transport):
    pass

class Train(Transport):
    pass

b = Bus(80)
t = Train(150)
print(b.max_speed, t.max_speed)

20.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

t = Teacher("Alice", 35, "Math")
print(t.name, t.subject)

21.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(self.__balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()

22.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = None
        self.set_marks(marks)

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

s = Student("Alice", 90)
print(s.get_marks())
s.set_marks(120)  # Invalid marks

23.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price

    def increase_price(self):
        self.__price *= 1.1

    def show_price(self):
        print(self.__price)

c = Car("Toyota", "Corolla", 20000)
c.increase_price()
c.show_price()

24.
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

r = Rectangle(5, 10)
print(r.area())

25.
class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary

    def show_salary(self):
        if self.role.lower() == "manager":
            print(self.__salary)
        else:
            print("Salary hidden")

e1 = Employee("Alice", "Manager", 80000)
e2 = Employee("Bob", "Developer", 50000)
e1.show_salary()
e2.show_salary()

26.
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram  # in GB

    def get_ram(self):
        return f"{self.__ram} GB"

l = Laptop("Dell", 16)
print(l.get_ram())

27.
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram  # in GB

    def get_ram(self):
        return f"{self.__ram} GB"

l = Laptop("Dell", 16)
print(l.get_ram())

28.
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.__rating = None
        self.set_rating(rating)

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print("Invalid rating")

    def get_rating(self):
        return self.__rating

m = Movie("Inception", 9)
print(m.get_rating())
m.set_rating(12)  # Invalid rating

29.
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock

    def sell(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            print("Not enough stock")

    def show_stock(self):
        print(self.__stock)

p = Product("Laptop", 10)
p.sell(3)
p.show_stock()

30.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.set_age(age)

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age cannot be negative")

    def get_age(self):
        return self.__age

p = Person("Alice", 25)
print(p.get_age())

31.
class Account:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
        else:
            print("Incorrect old PIN")

    def get_pin(self):
        return self.__pin  # For testing only

a = Account(1234)
a.change_pin(1234, 5678)
print(a.get_pin())

32.
class Account:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
        else:
            print("Incorrect old PIN")

    def get_pin(self):
        return self.__pin  # For testing only

a = Account(1234)
a.change_pin(1234, 5678)
print(a.get_pin())

33.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return math.pi * self.r**2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h
    
34.
class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

    def calculate_salary(self):
        return self.base

class Manager(Employee):
    def calculate_salary(self):
        return self.base + 10000

class Developer(Employee):
    def calculate_salary(self):
        return self.base + 5000

m = Manager("Alice", 50000)
d = Developer("Bob", 40000)
print(m.calculate_salary(), d.calculate_salary())

35.
class Notification:
    def send(self):
        print("Sending notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

EmailNotification().send()
SMSNotification().send()

36.
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

Sparrow().fly()
Penguin().fly()

37.
class Appliance:
    def switch_on(self):
        print("Appliance on")

class WashingMachine(Appliance):
    def switch_on(self):
        print("Washing machine on")

class Oven(Appliance):
    def switch_on(self):
        print("Oven on")

WashingMachine().switch_on()
Oven().switch_on()

38.
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hello, I am a student")

class Teacher(Person):
    def greet(self):
        print("Hello, I am a teacher")

Student().greet()
Teacher().greet()

39.
class Payment:
    def process(self):
        print("Processing payment")

class CreditCardPayment(Payment):
    def process(self):
        print("Processing credit card payment")

class UPIPayment(Payment):
    def process(self):
        print("Processing UPI payment")

CreditCardPayment().process()
UPIPayment().process()

40.
class Device:
    def turn_on(self):
        print("Device on")

class Phone(Device):
    def turn_on(self):
        print("Phone starting")

class Laptop(Device):
    def turn_on(self):
        print("Laptop starting")

Phone().turn_on()
Laptop().turn_on()

41.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_books(self):
        print(self.books)

lib = Library()
lib.add_book("Python 101")
lib.add_book("Java Basics")
lib.display_books()
lib.remove_book("Python 101")
lib.display_books()

42.
class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = False

    def mark_complete(self, task):
        if task in self.tasks:
            self.tasks[task] = True

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]

t = TodoList()
t.add_task("Study")
t.mark_complete("Study")
t.delete_task("Study")
print(t.tasks)

43.
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity, price):
        self.products.append({"name": name, "quantity": quantity, "price": price})

    def display(self):
        for p in self.products:
            print(p)

inv = Inventory()
inv.add_product("Laptop", 5, 50000)
inv.add_product("Mouse", 20, 500)
inv.display()

44.
class TicketBooking:
    def __init__(self, seats):
        self.available_seats = seats

    def reserve_seat(self, num):
        if num <= self.available_seats:
            self.available_seats -= num
        else:
            print("Not enough seats")

    def cancel_seat(self, num):
        self.available_seats += num

    def display_seats(self):
        print(self.available_seats)

tb = TicketBooking(50)
tb.reserve_seat(5)
tb.cancel_seat(2)
tb.display_seats()

45.
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def display_students(self):
        print(self.students)

c = Course("Python")
c.add_student("Alice")
c.add_student("Bob")
c.display_students()

46.
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    def remove_product(self, name):
        self.products = [p for p in self.products if p["name"] != name]

    def total_price(self):
        return sum(p["price"] for p in self.products)

cart = ShoppingCart()
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 500)
print(cart.total_price())

47.
class StudentResult:
    def __init__(self, marks):
        self.marks = marks  # list of marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        elif avg >= 75: return "B"
        elif avg >= 50: return "C"
        else: return "F"

sr = StudentResult([80, 90, 70])
print(sr.total(), sr.average(), sr.grade())

48.
class Restaurant:
    def __init__(self):
        self.orders = []

    def take_order(self, item, price):
        self.orders.append({"item": item, "price": price})

    def calculate_bill(self):
        return sum(o["price"] for o in self.orders)

    def display_orders(self):
        print(self.orders)

r = Restaurant()
r.take_order("Pizza", 500)
r.take_order("Coke", 100)
print(r.calculate_bill())
r.display_orders()

49.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.name] = acc

    def transfer(self, from_name, to_name, amount):
        if self.accounts[from_name].balance >= amount:
            self.accounts[from_name].balance -= amount
            self.accounts[to_name].balance += amount
        else:
            print("Insufficient funds")

b = Bank()
a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 500)
b.add_account(a1)
b.add_account(a2)
b.transfer("Alice", "Bob", 200)
print(a1.balance, a2.balance)

50.
class Game:
    def __init__(self):
        self.players = {}

    def add_player(self, name, score):
        self.players[name] = score

    def display_winner(self):
        winner = max(self.players, key=self.players.get)
        print(f"Winner: {winner} with {self.players[winner]} points")

g = Game()
g.add_player("Alice", 50)
g.add_player("Bob", 70)
g.display_winner()


    