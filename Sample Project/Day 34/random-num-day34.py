import random 
secret_number = random.randint(1, 20) 
attempts = 5 
while attempts > 0: 
    guess = int(input("Guess a number between 1 and 20: ")) 
    if guess == secret_number: 
        print("🎉 Congratulations! You guessed the correct number!") 
        break  # Exit the loop when guessed correctly 
    elif guess > secret_number: 
        print("📉 Too high! Try again.") 
    else: 
        print("📈 Too low! Try again.") 
    attempts -= 1 
    if attempts == 0: 
        print(f"❌ Out of attempts! The correct number was {secret_number}.") 
    else: 
        pass  # Placeholder for future enhancements