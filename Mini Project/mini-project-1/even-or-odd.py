while True:
    n = int(input("Enter number (0 to exit): "))
    if n == 0:
        break
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
