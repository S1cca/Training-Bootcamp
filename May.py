num = int(input("Enter a number: "))  # Ask user for a number

print("Odd numbers up to", num, ":")  # Print a message indicating the odd numbers will be listed

for i in range(num + 1):  # Loop through numbers up to user's input
    if i % 2 != 0:  # Check if number is odd
        print(i)  # If odd, print the number
