# 1. Rotate a list to the right by K positions
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

# 2. Find the longest substring without repeating characters
def longest_unique_substring(s):
    seen = {}
    start = max_len = 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# 3. Compress a string using character counts
def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

# 4. Find all duplicate words in a paragraph
from collections import Counter
def duplicate_words(paragraph):
    words = paragraph.lower().split()
    counts = Counter(words)
    return [word for word, count in counts.items() if count > 1]

# 5. Check whether two lists are circular rotations of each other
def are_circular_rotations(lst1, lst2):
    return len(lst1) == len(lst2) and ''.join(map(str, lst1*2)).find(''.join(map(str, lst2))) != -1

# 6. Return elements that appear more than once in a list
def duplicates_in_list(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]

# 7. Find the index of first repeating element in a list
def first_repeating_index(lst):
    seen = {}
    for i, val in enumerate(lst):
        if val in seen:
            return seen[val]
        seen[val] = i
    return -1

# 8. Group words that are anagrams from a list of strings
from collections import defaultdict
def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[tuple(sorted(word))].append(word)
    return list(anagrams.values())

# 9. Remove consecutive duplicate characters from a string
def remove_consecutive_duplicates(s):
    if not s:
        return ""
    result = [s[0]]
    for c in s[1:]:
        if c != result[-1]:
            result.append(c)
    return ''.join(result)

# 10. Split a list into equal-sized chunks of size N
def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# 11. Invert a dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}

# 12. Merge multiple dictionaries into one
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# 13. Sort a dictionary by its values in descending order
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

# 14. Count frequency of elements in a list using dictionary
def count_frequency(lst):
    return dict(Counter(lst))

# 15. Find key with maximum value in dictionary
def key_with_max_value(d):
    return max(d, key=d.get)

# 16. Convert two lists into a dictionary (one as keys, one as values)
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# 17. Filter dictionary items where value is greater than 50
def filter_dict_gt50(d):
    return {k: v for k, v in d.items() if v > 50}

# 18. Create a nested dictionary for student records (name → subjects → marks)
def student_records():
    return {
        "Alice": {"Math": 90, "Science": 85},
        "Bob": {"Math": 78, "Science": 82}
    }

# 19. Flatten a nested dictionary
def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# 20. Count occurrence of each character in a file
def char_count_in_file(filename):
    counts = Counter()
    with open(filename, 'r') as f:
        for line in f:
            counts.update(line)
    return dict(counts)

# 21. Create a recursive function to calculate power (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

# 22. Implement factorial using recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# 23. Generate Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 24. Create a function decorator that logs function execution time
import time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end-start:.6f}s")
        return result
    return wrapper

# 25. Build a function that accepts variable number of arguments and returns their product
def product(*args):
    result = 1
    for a in args:
        result *= a
    return result

# 26. Write a recursive function to reverse a string
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

# 27. Create a lambda function to filter even numbers from list
filter_even = lambda lst: [x for x in lst if x % 2 == 0]

# 28. Write a higher-order function that accepts another function as argument
def apply_func(func, data):
    return func(data)

# 29. Implement memoization manually for Fibonacci
fib_memo = {}
def fibonacci_memo(n):
    if n in fib_memo:
        return fib_memo[n]
    if n <= 1:
        fib_memo[n] = n
    else:
        fib_memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return fib_memo[n]

# 30. Build a function that validates password strength
import re
def validate_password(pwd):
    return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$', pwd))

# 31. Read a file and count how many times a specific word appears
def word_count_in_file(filename, word):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += line.lower().split().count(word.lower())
    return count

# 32. Copy content from one file to another without overwriting existing content
def append_file(src, dest):
    with open(src, 'r') as s, open(dest, 'a') as d:
        d.write(s.read())

# 33. Handle exception when dividing numbers (ZeroDivisionError)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# 34. Create a custom exception for invalid age input
class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age entered")

# 35. Read CSV file and display rows where salary > 50000
import csv
def high_salary_rows(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader if float(row['salary']) > 50000]

# 36. Safely open file and handle file-not-found error
def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

# 37. Create a log file for errors using try-except
def log_error():
    try:
        1/0
    except Exception as e:
        with open("error.log", "a") as f:
            f.write(str(e)+"\n")

# 38. Parse JSON file and display specific field values
import json
def read_json_field(filename, field):
    with open(filename) as f:
        data = json.load(f)
    return [item[field] for item in data if field in item]

# 39. Create a program that retries file reading 3 times if error occurs
def retry_read(filename, attempts=3):
    for _ in range(attempts):
        try:
            with open(filename) as f:
                return f.read()
        except FileNotFoundError:
            time.sleep(1)
    return None

# 40. Write program to append user input to a file
def append_input_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text + "\n")

# 41. Find all unique pairs in list whose difference equals given number
def pairs_with_difference(lst, diff):
    s = set(lst)
    return [(x, x+diff) for x in lst if x+diff in s]

# 42. Determine whether a number is a happy number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

# 43. Find the majority element in a list (> n/2 occurrences)
def majority_element(lst):
    counts = Counter(lst)
    for k, v in counts.items():
        if v > len(lst)//2:
            return k
    return None

# 44. Find intersection of three lists
def intersection_three(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

# 45. Check if a string contains only unique characters
def unique_chars(s):
    return len(set(s)) == len(s)

# 46. Implement stack using class and simulate push/pop operations
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def peek(self):
        return self.items[-1] if self.items else None
    def is_empty(self):
        return not self.items

# 47. Implement queue using collections.deque
from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self, item):
        self.q.append(item)
    def dequeue(self):
        return self.q.popleft() if self.q else None
    def is_empty(self):
        return not self.q

# 48. Detect cycle in a list using Floyd’s algorithm logic
def has_cycle(lst):
    slow = fast = 0
    while fast < len(lst) and fast+1 < len(lst):
        slow += 1
        fast += 2
        if lst[slow] == lst[fast]:
            return True
    return False

# 49. Validate whether a string is valid IPv4 address
def valid_ipv4(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255:
            return False
    return True

# 50. Simulate a basic command-line task manager (add, delete, view tasks)
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
    def view_tasks(self):
        return self.tasks