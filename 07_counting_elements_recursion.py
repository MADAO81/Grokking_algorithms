# Counting elements using recursion. [O(n)]

# Create the function "count" that accepts one parameter:
# the list "list_of_elem" containing elements to count.
def count(list_of_elem):
    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "count" takes a list containing 0 elements
    # as a parameter, then we exit this recursively called copy of the function "count"
    # and it returns the number "0" to the previous copy of the function "count" in a call stack,
    # since the number of elements in a list with 0 elements is always 0.
    # If the function "count" is initially called with a list containing 0 elements as a parameter,
    # then the function "count" immediately returns the number "0", since the number of elements
    # in a list with 0 elements is always 0.
    # The function "len()" returns the number of elements in a list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_of_elem) == 0:
        return 0
    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # Recursively call a copy of the function "count" with the list "list_of_elem" as a parameter,
    # except for the first element of this list, while the result of
    # this recursively called copy of the function "count" is is increased by 1.
    # When a copy of the function "count" is recursively called with the list containing 0 elements
    # as a parameter, then the base case is triggered.
    # The copies of the function "count" in the call stack terminate one by one and return their calculated values
    # to the previous recursively called copies of the function "count"
    # until the very first called function "count" stops its work.
    else:
        return 1 + count(list_of_elem[1:])

# Create the list of numbers "my_list".
my_list = [2, 0, 6, 9, 7, 7, 5, 4, 5, 2, 4, 5]


# Try to count elements in the list "my_list".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(count(my_list))