# Greedy algorithm using sets and hash tables (dictionaries).
# Here we need to find a set of radio stations to cover a certain number of states using a greedy algorithm.

# Set is a list-like type of data structure that cannot have duplicates.
# Create the set "states_needed" that stores a list of states to cover.
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "са", "az"}

# Create the dictionary "stations" in which its keys are the names of radio stations
# and its values are the states for coverage by these radio stations.
# The values are sets in this dictionary.
stations = {"kone": {"id", "nv", "ut"},
            "ktwo": {"wa", "id", "mt"},
            "kthree": {"or", "nv", "са"},
            "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}

# Create the set "final_stations" that stores a final set of radio stations to cover the states.
# Initially this set is empty.
final_stations = set()

# Create the while loop that generates the final set of radio stations to cover the states "final_stations".
# This while loop works as long as the set "states_needed" is not empty, that is,
# as long as we have uncovered states.
while states_needed:
    # Create the variable "best_station" that stores a name of the radio station
    # that covers the most states that are not yet covered.
    # Initially this variable stores "None".
    best_station = None
    # Create the variable "states_covered" that stores a set of states that are not yet covered
    # and can be covered by the radio station "best_station".
    # Initially this variable stores an empty set.
    states_covered = set()
    # Create the for loop in which we iterate over all the keys ("station") and values ("states_for_station")
    # in the dictionary "stations" and find the radio station "best_station".
    for station, states_for_station in stations.items():
        # Create the variable "covered" that stores a set of states
        # that are not yet covered and can be covered by the current radio station "station".
        # We find this set by intersecting the following sets:
        # 1. "states_needed" - the set of the states that are not yet covered.
        # 2. "states_for_station" - the set of the states that can be covered by the current radio station "station".
        covered = states_needed & states_for_station
        # If the set "covered" is greater than the set "states_covered", then
        if len(covered) > len(states_covered):
            # the current radio station "station" becomes the new best radio station "best_station",
            best_station = station
            # and also we update the set "states_covered".
            states_covered = covered
    # After each cycle of the for loop, we reduce the list of the states to be covered
    # by subtracting the list of the states that are covered by the current best radio station "best_station".
    # We do this by subtracting the set "states_covered" from the set "states_needed".
    states_needed -= states_covered
    # And also after each cycle of the for loop, we add the current best radio station "best_station"
    # to the final set of radio stations "final_stations".
    final_stations.add(best_station)
# Display the final set of the radio stations to cover the states "final_stations".
# The function "print()" prints the specified message to the screen, or other standard output device.
print(final_stations)