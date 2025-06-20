# Voting using hash tables (dictionaries).
# Using a dictionary, here we track the voters who voted and do not allow them to vote,
# and we also enter into the dictionary those voters who have not yet voted and allow them to vote.

# Hash table is a type of data structure that is an array whose elements contain pairs "key : value".
# Using a hash function, you can access a value by referring to its key.
# Create the dictionary (a dictionary is a hash table in Python) "voted", that stores a list of voters who voted.
# Initially this dictionary is empty.

voted = {}

# Create the function "check_voter" that accepts one parameter:
# the variable "voter_name" that contains a key representing the name of a voter.
def check_voter(name):
    
    # Using the function "get", we try to get the value by referring to the specified key "voter_name".
    # If the specified key "voter_name" is in the dictionary "voted",
    # then it means that the voter has already voted and we need to not allow him to vote.
    # The function "print()" prints the specified message to the screen, or other standard output device.
    if voted.get(name):
        print ("kick them out!")
        
    # If the specified key "voter_name" is not in the dictionary "voted", then the function "get" returns "None".
    # This means that the voter votes the first time, so we need to allow the voter to vote
    # and enter the name of this voter into the dictionary "voted"
    # by adding the value "True" by referring to the key "voter_name".
    else:
        voted[name] = True 
        print ("let them vote!")
        
        

# User Hasegawa tries to vote the first time.
print("User Taizo Hasegawa tries to vote the first time:")
check_voter("Hasegawa")


# User Gintoki tries to vote the first time.
print("User Sakata Gintoki tries to vote the first time:")
check_voter("Gintoki")


# User Gintoki tries to vote again.
print("User Gintoki tries to vote again:")
check_voter("Gintoki")


# User  Isao Kondo tries to vote the first time.
print("User Kondo tries to vote the first time:")
check_voter("Kondo")

# User Hasegawa tries to vote again.
print("User Hasegawa tries to vote again:")
check_voter("Hasegawa")