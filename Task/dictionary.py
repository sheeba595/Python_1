# ==================================================
# SETS
# ==================================================

# Task 1: Create and Access a Set
colors = {"Red", "Blue", "Green", "Yellow", "Purple"}
for color in colors:
    print(color)


# Task 2: Add Items to a Set
movies = set()
movies.add("Inception")
movies.add("Avatar")
movies.add("Titanic")
movies.add("Interstellar")
movies.add("Jumanji")
print(movies)


# Task 3: Remove Items from a Set
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"}
fruits.remove("Mango")
fruits.discard("Papaya")   # No error
print(fruits)


# Task 4: Check if an Item Exists in a Set
languages = {"Python", "Java", "C", "C++", "JavaScript"}
lang = input("Enter a language: ")
if lang in languages:
    print("Language exists in the set")
else:
    print("Language not found")


# Task 5: Join Two Sets
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
print(even.union(odd))


# Task 6: Find the Common Elements in Two Sets
set1 = {2, 4, 6, 8, 10}
set2 = {4, 8, 12, 16}
print(set1.intersection(set2))


# Task 7: Find the Difference Between Two Sets
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
print(A.difference(B))


# Task 8: Symmetric Difference Between Two Sets
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.symmetric_difference(setB))


# Task 9: Loop Through a Set
cars = {"BMW", "Audi", "Toyota", "Tesla"}
for car in cars:
    print(car)


# Task 10: Convert a List to a Set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)


# Task 11: Frozen Set Example
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# vowels.add('y')  # Error: frozenset is immutable
print(vowels)


# Task 12: Perform Set Operations on a Frozen Set
primes = frozenset({2, 3, 5, 7})
evens = {2, 4, 6, 8, 10}
print(primes.intersection(evens))
print(primes.union(evens))


# Task 13: Find the Length of a Set
words = {"apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"}
print(len(words))


# ==================================================
# DICTIONARIES
# ==================================================

# Task 14: Create a Dictionary and Access Elements
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])
print(person.get("age"))


# Task 15: Handle Missing Keys While Accessing Dictionary Items
print(person.get("salary", "Key not found"))


# Task 16: Add New Key-Value Pairs to a Dictionary
data = {}
data["name"] = "Sheeba"
print(data)
data["age"] = 20
print(data)
data["course"] = "Python"
print(data)


# Task 17: Update an Existing Dictionary Entry
product = {"name": "Laptop", "price": 50000, "stock": 10}
print("Before:", product)
product["price"] = 48000
product["stock"] = 8
print("After:", product)


# Task 18: Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)


# Task 19: Remove a Specific Key from a Dictionary
sample = {"x": 10, "y": 20, "z": 30, "a": 40, "b": 50}
del sample["z"]
try:
    del sample["p"]
except KeyError:
    print("Key does not exist")
print(sample)


# Task 20: Remove an Item Using pop() Method
info = {"name": "John", "age": 30, "city": "London"}
removed_value = info.pop("age")
print("Removed:", removed_value)
print(info)


# Task 21: Remove and Return the Last Item from a Dictionary
details = {"id": 101, "name": "Alice", "role": "Student"}
item = details.popitem()
print("Removed Item:", item)
print(details)


# Task 22: Iterate Through a Dictionary (Keys & Values)
for key, value in person.items():
    print(key, ":", value)


# Task 23: Iterate Through a Dictionary and Extract Keys Only
for key in person.keys():
    print(key)


# Task 24: Iterate Through a Dictionary and Extract Values Only
for value in person.values():
    print(value)


# Task 25: Iterate Through a Nested Dictionary
students = {
    "student1": {"name": "Sheeba", "age": 20, "subjects": ["Math", "CS"]},
    "student2": {"name": "Arun", "age": 21, "subjects": ["Physics", "Math"]}
}

for student, details in students.items():
    print(student)
    for key, value in details.items():
        print(key, ":", value)


# Task 26: Access a Specific Value from a Nested Dictionary
print(students["student2"]["subjects"])
print(students.get("student2").get("subjects"))
