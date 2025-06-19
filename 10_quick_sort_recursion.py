# Quick sort using recursion. [O(n*log n)]

# Create the function "quick_sort" that accepts one parameter:
# the list "list_to_sort" that contains numbers.
# This function returns this list sorted in ascending order.
def quick_sort(list_to_sort):
    
    # Create the base case.
    # Base case in a recursive function is a part of a function that describes
    # a condition for termination of the function in order to prevent loops.
    # If one of the recursively called copies of the function "quick_sort" takes a list containing 1 or 0 elements
    # as a parameter, then we exit this recursively called copy of the function "quick_sort"
    # and it returns this list to the previous copy of the function "quick_sort"
    # in a call stack, since if a list contains 1 or 0 elements, then this list is already sorted in ascending order.
    # If the function "quick_sort" is initially called with a list containing 1 or 0 elements as a parameter,
    # then the function "quick_sort" immediately returns this list,
    # since if a list contains 1 or 0 elements, then this list is already sorted in ascending order.
    # The function "len()" returns the number of elements in a list.
    # The keyword "return" is to exit a function and return a value.
    if len(list_to_sort) < 2:
        return list_to_sort

    # Create the recursive case.
    # Recursive case in a recursive function is a part of a function
    # in which the function calls itself in order to perform some task.
    # If the list "list_to_sort" contains 2 or more elements, then:
    else:

        # 1. The variable "pivot", that stores the pivot element of the list "list_to_sort",
        # that is equal to the element of the list "list_to_sort" at index 0, is created.
        pivot = list_to_sort[0]

        # 2. The sublist of the elements of the list "list_to_sort",
        # that are less than or equal to the pivot element of the list "list_to_sort", is formed.
        # To do this, we iterate over all the elements of the list "list_to_sort",
        # except for the first element of this list, using a for loop, and store in the sublist "less"
        # only those elements that are less than or equal to the pivot element.
        less = [i for i in list_to_sort[1:] if i <= pivot]

        # 3. The sublist of the elements of the list "list_to_sort",
        # that are greater than the pivot element of the list "list_to_sort", is formed.
        # To do this, we iterate over all the elements of the list "list_to_sort",
        # except for the first element of this list, using a for loop,
        # and store in the sublist "greater" only those elements are are greater than the pivot element.
        greater = [i for i in list_to_sort[1:] if i > pivot]

        # 4. Copies of the function "quick_sort" are recursively called for the sublists "less" and "greater",
        # and the results of these recursively called copies of the function "quick_sort"
        # are concatenated to the pivot element (["less" + "pivot" + "greater"]).
        # When a copy of the function "quick_sort" is recursively called with a list containing 1 or 0 elements
        # as a parameter, then the base case is triggered.
        # The copies of the function "quick_sort" in the call stack terminate one by one and return
        # their calculated values to the previous recursively called copies of the function "quick_sort"
        # until the very first called function "quick_sort" stops its work.
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Try to sort the list [2, 0, 6, 9, 7, 7] in ascending order.
# The function "print()" prints the specified message to the screen, or other standard output device.
print(quick_sort([1, 0, 3, 9, 11, 8]))