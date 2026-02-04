# Taking user input 
item_name = input("Enter the item name: ") 
price = float(input("Enter the price per item: ")) 
quantity = int(input("Enter the quantity: ")) 
# Calculating total bill (including 10% tax) 

subtotal = price * quantity 
tax = subtotal * 0.10 
total = subtotal + tax 
# Checking data types 
print(f"Type of item_name: {type(item_name)}")  # str 
print(f"Type of price: {type(price)}")  # float 
print(f"Type of quantity: {type(quantity)}")  # int 
print(f"Type of total: {type(total)}")  # float 
# Printing formatted bill 
print("\n===== Bill Summary =====") 
print(f"Item: {item_name}") 
print(f"Price per item: ${price:.2f}") 
print(f"Quantity: {quantity}") 
print(f"Subtotal: ${subtotal:.2f}") 
print(f"Tax (10%): ${tax:.2f}") 
print(f"Total Amount: ${total:.2f}")