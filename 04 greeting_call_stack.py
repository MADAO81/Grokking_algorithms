# Printing greetings.
# Here we create two functions, that are called by the third function.
# Here we can see how a call stack works.
# Create the function "how_are_you" that prints the message "How are you, username ?" to the screen
# using the function "print()".
# This function accepts one parameter: the name "username" of the person being greeted.
def how_are_you(username):
    print("How are you,", username, "?")
    
# Create the function "bye" that prints the message "Ok, bye!" to the screen using the function "print()".
# This function doesn't have any parameters.
def bye():
    print("Ok, bye!")
    
# Create the function "greet" that prints the message "Hello, username !" to the screen using the function "print()"
# and calls the functions "how_are_you" and "bye".
# This function accepts one parameter: the name "username" of the person being greeted.
def greet(username):

    # The call stack contains the function "greet".
    # The function "greet" does its work: it prints
    # the message "Hello, username !" to the screen using the function "print()".
    print("Hello,", username, "!")

    # The function "greet" calls the function "how_are_you".
    # The function "greet" is suspended in the call stack.
    # The function "how_are_you" is added to the call stack.
    # The function "how_are_you" does its work: it prints the message "How are you, username ?" to the screen.
    how_are_you(username)

    # The function "how_are_you" stops its work, transfers control to the function "greet"
    # and is removed from the call stack.
    # The function "greet" resumes its work and prints
    # the message "Ok, bye in 3 .. 2 .. 1" to the screen using the function "print()".
    print("Ok, bye in 3 .. 2 .. 1")

    # The function "greet" calls the function "bye".
    # The function "greet" is suspended again in the call stack.
    # The function "bye" is added to the call stack.
    # The function "bye" does its work: it prints the message "Ok, bye!" to the screen.
    bye()

    # The function "bye" stops its work, transfers control to the function "greet" and is removed from the call stack.
    # The function "greet" resumes its work.
    # The function "greet" stops its work and is removed from the call stack.


# Пытаемся поприветствовать пользователя John Shepard.
# ----------
# Try to greet user Taizou Hasegawa.
greet("Taizou Hasegawa")