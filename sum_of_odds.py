# Program to calculate and display the sum of all odd numbers up to a given number n.

# Prompt the user to enter a number
user_number = int(input("Please enter a number: "))

# Initialize the sum variable to store the total of odd numbers
sum = 0

# Loop through numbers up to the user's number
for i in range(user_number):
    if i % 2 != 0:  # Check if the number is odd
        sum += i
        print(f"Odd number: {i}")  # Display each odd number

# Display the final sum of all odd numbers up to the given number
print(f"The sum of all odd numbers up to {user_number} is: {sum}")
