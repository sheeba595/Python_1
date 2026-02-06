# ----------------------------------
# 1. Create a Tuple
# ----------------------------------
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits)


# ----------------------------------
# 2. Tuple Operations - Indexing & Length
# ----------------------------------
print("Third element:", fruits[2])
print("Length of tuple:", len(fruits))


# ----------------------------------
# 3. Accessing Tuple Elements
# ----------------------------------
numbers = (10, 20, 30, 40, 50)
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# ----------------------------------
# 4. Concatenation of Tuples
# ----------------------------------
num_tuple = (1, 2, 3)
name_tuple = ("Sheeba", "Arun", "Meena")
combined_tuple = num_tuple + name_tuple
print(combined_tuple)


# ----------------------------------
# 5. Tuple Slicing
# ----------------------------------
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums[2:8])


# ----------------------------------
# 6. Modifying a Tuple (Indirectly)
# ----------------------------------
tuple_data = (10, 20, 30)
temp_list = list(tuple_data)
temp_list[1] = 99
tuple_data = tuple(temp_list)
print(tuple_data)


# ----------------------------------
# 7. Deleting a Tuple
# ----------------------------------
temp_tuple = ("A", "B", "C")
del temp_tuple
# print(temp_tuple)  # NameError
print("Tuple deleted")


# ----------------------------------
# 8. Using Tuple Methods
# ----------------------------------
repeat_tuple = (1, 2, 2, 3, 2, 4)
print("Count of 2:", repeat_tuple.count(2))


# ----------------------------------
# 9. Tuple Built-In Functions
# ----------------------------------
num_data = (5, 10, 3, 8, 15)
print("Max:", max(num_data))
print("Min:", min(num_data))
print("Sum:", sum(num_data))


# ----------------------------------
# 10. Tuple vs List - Mutability Test
# ----------------------------------
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

# my_tuple[0] = 10  # TypeError
my_list[0] = 10

print("Tuple:", my_tuple)
print("List:", my_list)


# ----------------------------------
# 11. Check if an Element Exists in a Tuple
# ----------------------------------
check_tuple = (5, 10, 15, 20)
num = 10
print(num in check_tuple)


# ----------------------------------
# 12. Unpacking a Tuple
# ----------------------------------
colors = ("Red", "Green", "Blue", "Yellow")
c1, c2, c3, c4 = colors
print(c1, c2, c3, c4)


# ----------------------------------
# 13. Iterate Over a Tuple
# ----------------------------------
names_tuple = ("Alice", "Bob", "Charlie")
for name in names_tuple:
    print(name.upper())


# ----------------------------------
# 14. Create a list of 5 favorite movies and print it
# ----------------------------------
movies = ["Inception", "Avatar", "Titanic", "Interstellar", "Jumanji"]
print(movies)


# ----------------------------------
# 15. Access the 2nd and 4th elements from a list
# ----------------------------------
print(movies[1], movies[3])


# ----------------------------------
# 16. Add three new items to a list using append() and insert()
# ----------------------------------
fruit_list = ["Apple", "Banana"]
fruit_list.append("Mango")
fruit_list.append("Orange")
fruit_list.insert(1, "Grapes")
print(fruit_list)


# ----------------------------------
# 17. Update the value of an element in a list
# ----------------------------------
books = ["Python", "Java", "C++"]
books[1] = "JavaScript"
print(books)


# ----------------------------------
# 18. Remove a specific item using remove() and del
# ----------------------------------
items = ["Pen", "Pencil", "Eraser", "Scale"]
items.remove("Eraser")
del items[1]
print(items)


# ----------------------------------
# 19. Print only even numbers from a list
# ----------------------------------
num_list = [1, 2, 3, 4, 5, 6]
for n in num_list:
    if n % 2 == 0:
        print(n)


# ----------------------------------
# 20. Print list of names in uppercase
# ----------------------------------
name_list = ["sheeba", "arun", "meena"]
for name in name_list:
    print(name.upper())


# ----------------------------------
# 21. Reverse a list using slicing
# ----------------------------------
print(num_list[::-1])


# ----------------------------------
# 22. Nested list and flattening
# ----------------------------------
students = [
    ["Sheeba", [85, 90, 88]],
    ["Arun", [78, 80, 75]]
]

print("Marks of Sheeba:", students[0][1])

nested = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sub in nested:
    for item in sub:
        flat_list.append(item)
print(flat_list)


# ----------------------------------
# 23. Sort list in ascending and descending order
# ----------------------------------
sort_list = [5, 2, 9, 1, 7]
sort_list.sort()
print("Ascending:", sort_list)
sort_list.sort(reverse=True)
print("Descending:", sort_list)


# ----------------------------------
# 24. Find maximum and minimum in a list
# ----------------------------------
print("Max:", max(sort_list))
print("Min:", min(sort_list))


# ----------------------------------
# 25. Remove duplicates from a list without using set()
# ----------------------------------
dup_list = [1, 2, 2, 3, 4, 3, 5]
unique_list = []

for item in dup_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
