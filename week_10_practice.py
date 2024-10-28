# Question 13: Internet Speed Check

speed = float(input("Enter your internet download speed in Mbps: "))
streaming = input("Are you currently streaming? (Y or N): ")

# Determine the internet speed category
if speed < 10:
    if streaming == "Y":
        print("Upgrade required for streaming.")
    else:
        print("Basic browsing supported.")
elif 10 <= speed <= 50:
    if streaming == "Y":
        print("Good for light streaming.")
    else:
        print("Good for general use.")
else:
    print("High-speed internet.")
# Question 19: Course Enrollment Eligibility

grade = float(input("What is your grade? "))
prerequisites = input("Is your prerequisites complete or incomplete? ")

if grade > 10:
    if prerequisites == "complete":
        print("Eligible for advanced course enrollment.")
    else:
        print("Complete prerequisites to enroll>")

elif grade < 10:
    if prerequisites == "complete":
        print("Eligible for basic course enrollment")
else:
    print("Please complete prerequisites and reapply next year.")