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
    purpose if you can!"""

def number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")

def super_asker(low, high, message="Please enter an integer"):
    while True:
        try:
            input_number= int(input(f"{message} between {low} and {high}: "))
            if low <= input_number <=high:
                return input_number
        except Exception as e:
            print('do it again'.format(e)) 

def advancedGuessingGame():
    print("😊Welcome to the Advanced Guessing Game!")

    lowerbound = super_asker(-5000, 5000, "Enter the lower bound ")
    upperbound = super_asker(lowerbound + 2, 5000, "Enter the upper bound: ")

    # while upperbound <= lowerbound:
    #     if upperbound == lowerbound:
    #         print ("they cannot be equal, my friend.")
    #     else:
    #         print("please switch the positions of these two numbers or make a new one.")
    #     lowerbound = number("Enter the lower bound: ")
    #     upperbound = number("Enter the upper bound: ")
    
    actualNumber = random.randint(lowerbound, upperbound)
    guessed = False

    while not guessed:
        guessednumber = super_asker(lowerbound , upperbound, "guess a number: ")

        if guessednumber < lowerbound or guessednumber > upperbound:
            print(f"😰 why you try this number?")
        elif guessednumber < actualNumber:
            print(f"it's small, try again.")
            lowerbound=guessednumber
        elif guessednumber > actualNumber:
            print(f"it's big, try agian.")
            upperbound=guessednumber
        else:
            guessed = True

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
