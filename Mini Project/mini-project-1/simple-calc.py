print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Enter choice: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    print("Invalid choice")
