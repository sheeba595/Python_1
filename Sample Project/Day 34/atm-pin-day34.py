correct_pin = "1234"  # Set a correct PIN 
attempts = 3   
while attempts > 0: 
    pin = input("Enter your 4-digit PIN: ") 
    if pin == correct_pin: 
        print("✅ Access Granted!") 
        break  # Exit the loop if PIN is correct 
    else: 
        attempts -= 1 
        print(f"❌ Incorrect PIN! {attempts} attempts left.") 
        if attempts == 0: 
            print("🚫 Access Denied. Your account is locked.") 
        else: 
            continue  # Skip to the next attempt 