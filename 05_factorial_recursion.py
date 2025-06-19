
# Factorial using recursion. [O(n)]
# Create the function "fact" that calculates a factorial.
# This function accepts one parameter: the number "x", the factorial of which is to be found.
def fact(x):

    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "fact" calculates the factorial of the number 1,
    # then we exit this recursively called copy of the function "fact" and it returns the number "1" to
    # the previous copy of the function "fact" in a call stack.
    # If the function "fact" is initially called with the parameter of 1,
    # then the function "fact" immediately returns the number 1, since the factorial of the number 1 is 1.
    # The keyword "return" is to exit a function and return a value.
    if x == 1:
        return 1

    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # Recursively call a copy of the function "fact" with the parameter decreased by 1,
    # the result of which is multiplied by the value of the parameter of the current copy of the function "fact".
    # When a copy of the function "fact" is recursively called with the parameter of 1, then the base case is triggered.
    # The copies of the function "fact" in the call stack terminate one by one and return their calculated values
    # to the previous recursively called copies of the function "fact"
    # until the very first called function "fact" stops its work.
    else:
        return x * fact(x-1)


# Try to find the factorial of 10.
# The function "print()" prints the specified message to the screen, or other standard output device.
print(fact(10))