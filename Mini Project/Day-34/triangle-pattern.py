# Objective: 
# Create a Triangle Pattern Generator that takes a number input from the user and 
# prints a triangle pattern. 
user=int(input("Enter a number: "))
print("Triangle Pattern")
for i in range(1,user+1):
    if(i%2!=0):
        print(i*"*")
print("Triangle generation completed!")