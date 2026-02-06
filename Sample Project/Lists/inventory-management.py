# Mini Project 4: Inventory Management System using Tuples 
# Inventory Tuple (Item Name, Price) 
inventory = (("Laptop", 70000), ("Mouse", 1500), ("Keyboard", 2500), ("Monitor", 
12000)) 
# Display all inventory items 
print("Inventory Items:") 
for item in inventory: 
    print(f"{item[0]} - Rs.{item[1]}") 
# Searching for an item 
search_item = "Mouse" 
found = next((item for item in inventory if item[0] == search_item), None) 
if found: 
    print(f"\n{search_item} is available at Rs.{found[1]}") 
else: 
    print(f"\n{search_item} is not available in the inventory.") 
# Removing an item from inventory 
remove_item = "Keyboard" 
inventory = tuple(item for item in inventory if item[0] != remove_item) 
print("\nUpdated Inventory (After Removing Keyboard):") 
print(inventory)