# Question 1
while True:
    q1 = input("Which number would you like to investigate (0 to exit):\n")
    # if statement that targets invalid user input that is not an integer
    if q1.isnumeric() and int(q1) <= 10:
        q1 = int(q1)
        # if statement giving user ability to exit application by clicking 0
        if q1 == 0:
            print("Exiting the application")
            break
        print(f"You entered: {q1}")
    # else statement shooting error message letting user know that only integers are accepted as input
    else:
        print("Invalid input for number, please enter an integer between 1 and 10")
        continue
    # Question 2 
    while True:
        q2 = input("Minimum Calculated Range:\n")
        if q2.isnumeric():
            q2 = int(q2)
            print(f"You entered: {q2}")
            break
        else:
            print("Invalid input for minimum range, please enter an integer")
    # Question 3 
    while True:
        q3 = input("Maximum Calculated Range:\n")
        if q3.isnumeric():
            q3 = int(q3)
            print(f"You entered {q3}")
            break
        else:
            print("Invalid input for maximum range, please enter an integer")
    # Final equation for the time table using "i" as the loop variable
    for i in range(q2, q3+1):
        print(q1, "*", i, "=", q1*i)
