# Countdown using recursion. [O(n)]
# Create the function "countdown" that accepts one parameter:
# the number "i" representing the number of seconds to count down.
def countdown(i):
    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If there is no seconds to count down, then we exit the function. This is our base case.
    # The keyword "return" is to exit a function and return a value.
    if i < 0:
        return
    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # Print the number to the screen using the function "print()" and recursively call the function "countdown"
    # with the parameter decreased by 1. This is our recursive case.
    # When the parameter of the function "countdown" is less than 0,
    # then the base case is triggered and the function stops its work.
    else:
        print(i)
        return countdown(i-1)

# Try to display the countdown from 15 to 0.
countdown(15)
