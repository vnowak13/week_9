# while loops = execute some code WHILE some condition remains true

# name = input("Enter your name: ")
# # iteration = loops
# while name == '':
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("Bye")

# num = int(input("Enter a number between 1 - 10: "))

# while num <1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1- 10: "))
# print(f"your number is {num}")

################################################################################################################################
 
# for loops = execute a block of code a fixed number of times. 
#             You can iterate over a range, string, sequence, etc.

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue #skips over
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break #stops it
#     else:
#         print(x)

###############################################################################################################################
        
#challenge
list_of_name = ['John', 'Paul', 'George', 'Ringo']
# if the name is 'John', 'Paul', 'George', 'Ringo' was found!
#otherwise, print 'George was not found!' and print out the other names using a loop
#print out the other names using a loop
for name in list_of_name:
    if name == 'George':
        print("George was found!")
    else: 
        print('George was not found!')
        print(name)

list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']
#loop through the list_of_names2
#if the name is 'Ironman', skip over it and
#print out the other names
for name in list_of_names2:
    if name == "Ironman":
        continue
    print(name)

#loop through the list_of_names2 and
# and rename 'Thanos' to 'Black Widow'
for name in list_of_names2:
    if name == 'Thanos':
        name = 'Black Widow'
        print(name)
#another way of naming 'Thanos to 'Black Widow'
list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']
for i in range(len(list_of_names2)):
    if list_of_names2[i] == 'Thanos':
        list_of_names2[i] = 'Black Widow'
    print(list_of_names2[i])