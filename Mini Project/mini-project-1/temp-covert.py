print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
choice = int(input("Enter choice: "))

temp = float(input("Enter temperature: "))

if choice == 1:
    print("Fahrenheit:", (temp * 9/5) + 32)
elif choice == 2:
    print("Celsius:", (temp - 32) * 5/9)
