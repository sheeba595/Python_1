s = input("Enter string: ")

length = len(s)
vowels = 0
upper = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    if ch.isupper():
        upper += 1

print("Length:", length)
print("Vowels:", vowels)
print("Uppercase letters:", upper)
    