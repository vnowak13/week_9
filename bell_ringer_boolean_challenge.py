# Exerise 1: Simple Conditional
fav_program = input("Enter yourZ favorite programming language: ")

if fav_program == 'python' : 
    print('You love Python!')
else: 
    print("Different Choice")

# Exerise 2: Grading System
grade = input("Enter your grade number value: ")
l = int(grade)

if 90<=l<=100: 
    print("Your grade is an A!")
elif 80<=l<=89:
    print("Your grade is a B!")
elif 70<=l<=79:
    print("Your grade is a C!")
elif 60<=l<=69:
    print("Your grade is a D!")
else:
    print("Your grade is a F!")

# Exercise 3: Admin Login
username = input("Enter your username: ")
logged_in = "False"

if username == 'admin' and "logged_in" == 'True':
    print("Welcome Admin!")
else:
    print("Please log in!") 

# Exercise 4: Object identity Check
list_1 = [4, 5, 6]
list_2 = ['x' , 'y' , 'z' ]

print(list_1 == list_2) # compares the two listen and indicates if it's true or not