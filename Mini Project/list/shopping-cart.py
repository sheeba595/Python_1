# ----------------------------------
# Mini Project 2: Shopping Cart System
# ----------------------------------

# Cart list to store products as [product_name, price]
cart = []

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")

    choice = input("Enter your choice: ")

    # 1. Add product to cart
    if choice == "1":
        product_name = input("Enter Product Name: ")
        price = int(input("Enter Price: "))
        cart.append([product_name, price])
        print("Product added successfully!")

    # 2. Remove product by name
    elif choice == "2":
        product_name = input("Enter Product Name to remove: ")
        found = False

        for item in cart:
            if item[0] == product_name:
                cart.remove(item)
                found = True
                print("Product removed successfully!")
                break

        if not found:
            print("Product not found!")

    # 3. View cart items and total price
    elif choice == "3":
        if not cart:
            print("Shopping Cart is empty!")
        else:
            total_price = 0
            print("Shopping Cart:", cart)

            for item in cart:
                total_price += item[1]

            print("Total Items:", len(cart))
            print("Total Price:", total_price)

    # 4. Checkout and exit
    elif choice == "4":
        total_price = 0
        for item in cart:
            total_price += item[1]

        print("Final Cart:", cart)
        print("Total Amount to Pay:", total_price)
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Please try again.")
