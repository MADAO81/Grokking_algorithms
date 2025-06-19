# binary search

def binary_search(list, item):
    # the variables "low" and "high" store the boundaries of the part of the search in which the search is performed.
    low = 0
    high = len(list) - 1
    
    while low <= high: # Until this part is reduced to one element...
        mid = (low + high)//2 # ...checking the average subscription
        guess = list[mid]
        if guess == item: # Value found
            return mid
        if guess > item: # too much 
            high = mid - 1 
        else: # too low
            low = mid + 1 
    return None # The value does not exist
        
        

         
my_list = [ 1, 3, 5,  7,  9] # let's test the function


print (binary_search(my_list, 3))
print (binary_search(my_list, -1))
