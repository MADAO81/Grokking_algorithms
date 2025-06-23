# Breadth-first search using hash tables (dictionaries) and deques.
# [O(V+E); V - the number of vertices in a graph, E - the number of edges in a graph]
# Here we need to find a mango seller among the friends and the friends of friends of a character.
# Here we can see how deque works.

# Deque is a data structure type similar to call stack:
# we can't choose the element that we want to access.
# Deque supports two operations: enqueue and dequeue.
# Deque allows us to add or remove elements from both the beginning and the end of a queue.
# To create deques, you need to use the list-like container "deque" from the module "collections".
# The keyword "import" is used to import modules.
# The keyword "from" is used to import certain sections from a module.
from collections import deque

# Create the function "person_is_seller" that accepts one parameter:
# the variable "char_name" containing a name of a character to check if this character is a mango seller or not.
# If the name of a character ends with the letter "r", then the function "person_is_seller" returns "True",
# otherwise this function returns "False".
# The keyword "return" is to exit a function and return a value.
def person_is_seller(char_name):
    return char_name[-1] == 'o'

# Create the dictionary "char_graph", that is a graph of the characters and their closest friends.
# Each key has an associated value that is a list.
# This list is a list of the closest friends of a character whose name is represented in a key.
char_graph = {"Hasegawa": ["Gintoki", "Kagura", "Shinpachi"],
              "Gintoki": ["Katsura"],
              "Kagura": ["Katsura", "Sadaharu"],
              "Shinpachi": ["Tae", "Tsukuyo"],
              "Sadaharu": [],
              "Katsura": [],
              "Tae": [],
              "Tsukuyo": []}

# Create the function "search_seller" that accepts one parameter:
# the variable "char_name" containing a name of a character to check if this character has a mango seller
# among the friends and the friends of friends of this character.
def search_seller(char_name):

    # Create the new deque "search_queue" by using the method "deque()".
    search_queue = deque()

    # Add all the closest friends of the character "char_name" to the deque "search_queue"
    search_queue += char_graph[char_name]

    # Create the list "searched", to which we add those characters that we have already checked.
    # Initially this list is empty.
    searched = []

    # Create the while loop that works as long as the deque "search_queue" is not empty.
    while search_queue:

        # The first element is retrieved from the deque "search_queue".
        # The method "popleft()" removes the first element from the deque "search_queue"
        # and returns it to the variable "person".
        person = search_queue.popleft()

        # If the character "person" is not in the list "searched" and
        if person not in searched:

            # if this character "person" is a mango seller (here the function "person_is_seller" is called),
            # then the message stating that this "person" is a mango seller is displayed.
            # The function "print()" prints the specified message to the screen, or other standard output device.
            if person_is_seller(person):
                return print(person + " is a mango seller!")

            # Otherwise, if this character "person" is not a mango seller,
            # then all the closest friends of this character "person" are added to the end of the deque "search_queue".
            else:
                search_queue += char_graph[person]

                # And also this character "person" is added to the list "searched"
                # to avoid re-checking this character.
                searched.append(person)

    # If the deque "search_queue" happens to be empty, it means there is no mango seller among the characters.
    # The message stating that there is no mango seller among the characters is displayed.
    return print("There is no mango seller among the characters")

# Try to find a mango seller among the friends and the friends of friends of the character Hasegawa.
search_seller("Hasegawa")
