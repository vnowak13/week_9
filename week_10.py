# Problem 1: Student Grade Categorization
# Ask the user to enter a list of student scores (one by one)+
# Initialize counters
excellent_count = 0
good_count = 0
pass_count = 0
fail_count = 0

while True:
    score = float(input("Enter a student score (negative number to stop): "))
    
    if score < 0:
        break  # Stop if negative number is entered
    
    # Categorize the score
    if score >= 90:
        print("Excellent")
        excellent_count += 1
    elif score >= 70:
        print("Good")
        good_count += 1
    elif score >= 50:
        print("Pass")
        pass_count += 1
    else:
        print("Fail")
        fail_count += 1 

# Stop the loop and print the final count of each category when the user enters a negative number.
print(f"Excellent: {excellent_count}, Good: {good_count}, Pass: {pass_count}, Fail: {fail_count}")


##################################################################################################################################


# Problem 2: Even and Odd Counter with Conditions
# Ask the user for a starting and ending number.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Use a for loop to iterate from the starting to the ending number.
special_even_count = 0
special_odd_count = 0
# Inside the loop:

# Use nested if to check if the number is both even and greater than 10. If true, count it as a “special even” number.
# If it’s odd and less than 20, count it as a “special odd” number.
# Iterate from start to end
for number in range(start, end):
    if number > 10 and number % 2 == 0:
         special_even_count += 1  # Count as special even
    elif number < 20 and number % 2 != 0:
        special_odd_count += 1   # Count as special odd


# Print the counts
print(f"Special even numbers: {special_even_count}, Special odd numbers: {special_odd_count}")















