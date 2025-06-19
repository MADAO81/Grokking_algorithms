# Sum of elements using recursion. [O(n)]

# Create the function "sum_of_elem" that accepts one parameter:
# the list "list_of_elem" containing the elements to add.
def sum_of_elem(list_of_elem):

    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "sum_of_elem" takes a list containing 0 elements
    # as a parameter, then we exit this recursively called copy of the function "sum_of_elem"
    # and it returns the number "0" to the previous copy of the function "sum_of_elem" in a call stack,
    # since the sum of 0 elements is always 0.
    # If the function "sum_of_elem" is initially called with a list containing 0 elements as a parameter,
    # then the function "sum_of_elem" immediately returns the number "0", since the sum of 0 elements is always 0.
    # The function "len()" returns the number of elements in a list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_of_elem) == 0:
        return 0

    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # Recursively call a copy of the function "sum_of_elem" with the list "list_of_elem" as a parameter,
    # except for the first element of this list, while the result of
    # this recursively called copy of the function "sum_of_elem" is summed up with the first element of the parameter
    # of the current copy of the function "sum_of_elem".
    # When a copy of the function "sum_of_elem" is recursively called with a list containing 0 elements
    # as a parameter, then the base case is triggered.
    # The copies of the function "sum_of_elem" in the call stack terminate one by one and return their calculated values
    # to the previous recursively called copies of the function "sum_of_elem"
    # until the very first called function "sum_of_elem" stops its work.
    else:
        return list_of_elem[0] + sum_of_elem(list_of_elem[1:])



# Try to find the sum of 15, 9, 45, 3, 2.
# The function "print()" prints the specified message to the screen, or other standard output device.
print(sum_of_elem([15, 9, 45, 3, 2]))