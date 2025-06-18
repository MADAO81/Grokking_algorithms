# Selection sort. [O(n*n)]
# Here we create two functions:
# the first function finds the smallest element in a list,
# and the second function sorts the list by comparing each element in the list with the smallest element.

# Create the function "find_smallest" that accepts one parameter:
# the list "arr" that contains numbers.
# This function returns the index of the smallest number in the list.
def find_smallest(arr):
    smallest = arr[0]  # To store the smallest value
    smallest_index = 0 # To store the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
    return smallest_index
    
# Create the function "selection_sort" that accepts one parameter:
# the list "arr" that contains numbers.
# This function returns this list sorted in ascending order.
    
def selectionsort(arr): # Сортирует массив
    newarr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr) # Finds the smallest element in the array and adds ero to the new array
        newarr.append(arr.pop(smallest))
    return newarr

print (selectionsort([5, 3, 6, 8, 2, 19]))