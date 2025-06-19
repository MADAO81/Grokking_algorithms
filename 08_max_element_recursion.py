# Finding the greatest element using recursion. [O(n)]

# Create the function "find_max_one" that accepts one parameter:
# the list "list_one" containing elements to find the greatest one.
def find_max_one(list_one):

    # If the list "list_one" contains 0 elements, then the function "find_max_one" returns "None".
    # "None" means nil (nothing) in Python. We use it to define that the number to find is not in the list.
    # The function "len()" returns the number of elements in a list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_one) == 0:
        return None
        
    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "find_max_one" takes a list containing 1 element
    # as a parameter, then we exit this recursively called copy of the function "find_max_one"
    # and it returns the first element of this list to the previous copy of the function "find_max_one"
    # in a call stack, since if a list contains only 1 element, then this element is the greatest one.
    # If the function "find_max_one" is initially called with a list containing 1 element as a parameter,
    # then the function "find_max_one" immediately returns the first element of this list,
    # since if a list contains only 1 element, then this element is the greatest one.
    if len(list_one) == 1:
        return list_one[0]

    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # If the first element is greater than the second element in the list "list_one",
    # then this second element is deleted using the keyword "del" and a new copy of the function "find_max_one"
    # is recursively called with this reduced list "list_one" as a parameter.
    # When a copy of the function "find_max_one" is recursively called with a list containing 1 element
    # as a parameter, then the base case is triggered.
    # The copies of the function "find_max_one" in the call stack terminate one by one and return
    # their calculated values to the previous recursively called copies of the function "find_max_one"
    # until the very first called function "find_max_one" stops its work.
    if list_one[0] > list_one[1]:
        del list_one[1]
        return find_max_one(list_one)

    # Otherwise, if the first element is less than the second element in the list "list_one",
    # then a new copy of the function "find_max_one" is recursively called with the list "list_one",
    # except for the first element, as a parameter.
    else:
        return find_max_one(list_one[1:])


# Create 2 lists and try to find the greatest elements in these lists.
# The list "my_list1" contains several numbers, but the list "my_list2" is empty.
# The function "print()" prints the specified message to the screen, or other standard output device.
my_list1 = [2, 0, 6, 9, 7, 7]
my_list2 = []
print(find_max_one(my_list1))
print(find_max_one(my_list2))


# Let's create another variation of the function to find the greatest element.
# Here we create another recursive case.
# Create the function "find_max_two" that accepts one parameter:
# the list "list_two" containing the elements to find the greatest one.
def find_max_two(list_two):

    # If the list "list_two" contains 0 elements, then the function "find_max_two" returns "None".
    # "None" means nil (nothing) in Python. We use it to define that the number to find is not in the list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_two) == 0:
        return None

    # Create the base case.
    # If one of the recursively called copies of the function "find_max_two" takes a list containing 1 element
    # as a parameter, then we exit this recursively called copy of the function "find_max_two"
    # and it returns the first element of this list to the previous copy of the function "find_max_two"
    # in a call stack, since if a list contains only 1 element, then this element is the greatest one.
    # If the function "find_max_two" is initially called with a list containing 1 element as a parameter,
    # then the function "find_max_two" immediately returns the first element of this list,
    # since if a list contains only 1 element, then this element is the greatest one.
    if len(list_two) == 1:
        return list_two[0]

    # Create the recursive case.
    # A new copy of the function "find_max_two" is recursively called with the list "list_two",
    # except for the first element, as a parameter,
    # and the result of this recursively called copy of the function "find_max_two" is stored
    # in the variable "sub_max".
    # Any copy of the function "find_max_two" returns a result based on the following condition:
    # it returns the first element of the list "list_two" if this first element is greater than the value of
    # the variable "sub_max", otherwise this local variable "sub_max" is returned.
    # When a copy of the function "find_max_two" is recursively called with a list containing 1 element
    # as a parameter, then the base case is triggered.
    # The copies of the function "find_max_two" in the call stack terminate one by one and return
    # their calculated values to the previous recursively called copies of the function "find_max_two"
    # until the very first called function "find_max_two" stops its work.
    else:
        sub_max = find_max_two(list_two[1:])
        return list_two[0] if list_two[0] > sub_max else sub_max


# Try to find the greatest elements in the lists "my_list1" and "my_list2" using the function "find_max_two".
print(find_max_two(my_list1))
print(find_max_two(my_list2))