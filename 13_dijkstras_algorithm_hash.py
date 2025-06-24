# Dijkstra's algorithm using hash tables (dictionaries).
# [O(E*log V)); V - the number of vertices in a graph, E - the number of edges in a graph]
# Here we need to find all the shortest paths from a start node to all other nodes
# in a directed acyclic weighted graph.

# Create the dictionary "graph" which is a directed acyclic weighted graph.
# This dictionary is special in that each of its value is a dictionary.
# These values are the sets of neighboring nodes of each node of this graph and their costs.
graph = {"start": {"a": 6,
                   "b": 2},
         "a": {"fin": 1},
         "b": {"a": 3,
               "fin": 5},
         "fin": {}}

# Create the variable "infinity" that stores "infinity".
# We use this variable when a path to a node is unknown.
infinity = float("inf")

# Create the dictionary "costs" which is a table of costs of the paths from the node "start"
# to the other nodes of the graph "graph".
# We specify those costs that are known at the beginning of the algorithm.
# The comments below show the changes of the values after each cycle of the while loop,
# which is located at the bottom of this program.
costs = {"a": 6,            # 5 - 5 - 5
         "b": 2,            # 2 - 2 - 2
         "fin": infinity}   # 7 - 6 - 6


# Create the dictionary "parents" which is a table of the parents of each node in the graph "graph".
# We specify those parents that are known at the beginning of the algorithm.
# The comments below show the changes of the values after each cycle of the while loop,
# which is located at the bottom of this program.
parents = {"a": "start",    # "b"     - "b"     - "b"
           "b": "start",    # "start" - "start" - "start"
           "fin": None}     # "b"     - "a"     - "a"


# Create the list "processed" to which we add already processed nodes
# to avoid reprocessing such nodes.
# Initially this list is empty.
processed = []


# Create the function "find_lowest_cost_node" that accepts one parameter:
# the dictionary "table_of_costs" which is a table of costs of paths from a start node
# to other nodes of a directed acyclic weighted graph.
# This function returns a name of the lowest cost node.
def find_lowest_cost_node(table_of_costs):

    # Create the variable "lowest_cost" that stores the cost of the lowest cost node.
    # Initially this variable stores the value "infinity".
    lowest_cost = float("inf")

    # Create the variable "lowest_cost_node" that stores the name of the lowest cost node.
    # Initially this variable stores "None".
    lowest_cost_node = None

    # Create the for loop in which we iterate over all the keys (graph nodes) of the dictionary "table_of_costs".
    for key_node in table_of_costs:
        # Create the variable "value_cost" that stores the value (cost of a graph node)
        # corresponding to the current key.
        value_cost = table_of_costs[key_node]
        # If the cost of the current node is less than the cost of the lowest cost node,
        # and if we have not yet processed this current node, then
        if value_cost < lowest_cost and key_node not in processed:
            # we consider that the cost of the current node is the lowest,
            lowest_cost = value_cost
            # and we also consider that this node is the new lowest cost node.
            lowest_cost_node = key_node
    # As a result of this for loop, the function "find_lowest_cost_node" returns the name of the lowest cost node.
    # The keyword "return" is to exit a function and return a value.
    return lowest_cost_node
# Find the name of the lowest cost node in the dictionary "costs" (initially it is the node "b").
# The comments below show the changes of the value of this variable after each cycle of the while loop,
# which is located at the bottom of this program.
node = find_lowest_cost_node(costs)  # "a" - "fin" - None

# Calculate all the shortest paths from the node "start" to the nodes "a", "b", "fin"
# by updating the dictionaries "costs" and "parents".
# Create the while loop that works as long as the variable "node" is not empty, that is,
# as long as we have the lowest cost nodes to process.
while node is not None:
    # Create the variable "cost" that stores the cost of the current lowest cost node "node".
    cost = costs[node]
    # Create the variable "neighbors", the stores a dictionary which is a list of the neighboring nodes
    # of the current lowest cost node "node" and their costs.
    neighbors = graph[node]
    # Create the for loop in which we iterate over the keys (the names of all neighboring nodes
    # of the current lowest cost node "node") in the dictionary "neighbors".
    for neighbor_name in neighbors.keys():
        # Calculate the new cost of the path from the node "start" to the current neighboring node
        # of the lowest cost node "node".
        new_cost = cost + neighbors[neighbor_name]
        # If the current cost of the path from the node "start" to the current neighboring node
        # of the lowest cost node "node" is greater than the new cost of this path, then
        if costs[neighbor_name] > new_cost:
            # we update the current cost of this path in the dictionary "costs",
            costs[neighbor_name] = new_cost
            # and also we update the parent of the current neighboring node
            # of the current lowest cost node "node" in the dictionary "parents".
            parents[neighbor_name] = node
    # If we have iterated over all the neighboring nodes of the current lowest cost node "node",
    # then we add this node to the list "processed",
    processed.append(node)
    # find the next lowest cost node
    # and this while loop continues from the beginning using this new node.
    node = find_lowest_cost_node(costs)

# Display the updated dictionaries "costs" and "parents".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(costs)
print(parents)