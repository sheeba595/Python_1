# ----------------------------------
# Mini Project 4: Shopping Cart System using Tuples
# ----------------------------------

# Create a tuple containing different product names in a shopping cart
cart = ("Laptop", "Mouse", "Keyboard", "Mouse")

while True:
    print("\n1. View All Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Count Product")
    print("5. Show First Three Products")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Allow the user to view all products in the cart
    if choice == "1":
        print("Shopping Cart:", cart)

    # Allow the user to add a new product
    # (Convert tuple to list, add item, convert back to tuple)
    elif choice == "2":
        product = input("Enter product name to add: ")
        cart_list = list(cart)
        cart_list.append(product)
        cart = tuple(cart_list)
        print("Product added successfully!")

    # Allow the user to remove a product
    # (Convert tuple to list, remove item, convert back to tuple)
    elif choice == "3":
        product = input("Enter product name to remove: ")
        cart_list = list(cart)
        if product in cart_list:
            cart_list.remove(product)
            cart = tuple(cart_list)
            print("Product removed successfully!")
        else:
            print("Product not found!")

    # Find how many times a specific product appears using .count()
    elif choice == "4":
        product = input("Enter product name to count: ")
        print(f"{product} appears {cart.count(product)} time(s) in the cart")

    # Display only the first three items using tuple slicing
    elif choice == "5":
        print("First three products:", cart[:3])

    # Exit the program
    elif choice == "6":
        print("Exiting Shopping Cart System.")
        break

    else:
        print("Invalid choice! Please try again.")
