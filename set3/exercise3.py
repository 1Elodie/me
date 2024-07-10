"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!

    def get_valid_integer(prompt):
    
    Prompt the user for a valid integer.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def advancedGuessingGame():
    print("Welcome to the Advanced Guessing Game!")

    # Get a valid lower bound
    lower_bound = get_valid_integer("Enter the lower bound: ")
    
    # Get a valid upper bound
    while True:
        upper_bound = get_valid_integer("Enter the upper bound: ")
        if upper_bound > lower_bound:
            break
        print("The upper bound must be greater than the lower bound.")

    # Generate a random number within the range
    secret_number = random.randint(lower_bound, upper_bound)

    print(f"Guess a number between {lower_bound} and {upper_bound}.")

    # Start the guessing game
    while True:
        guess = get_valid_integer("Your guess: ") """
    
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
