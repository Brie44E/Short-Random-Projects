# A short game based on this (no source code exe)
# Source https://inventwithpython.com/invent4thed/chapter3.html

import random

anwser = "Start"
number = random.randint(0,20)

# print(number)

# Get user name
name = input("Hello! What is your name?")

# Question
guess = input(f"Well, {name}, I am thinking of a number between 1 and 20. \n Take a guess.")
numberOfGuess = 1

while int(guess) != number:
    numberOfGuess += 1
    if int(guess) > number:
        guess = input("Your guess is too high. \n Take a guess.")
    elif int(guess) < number:
        guess = input("Your guess is too low. \n Take a guess.")

if int(guess) == number:
    print(f'Good job, {name}! You guessed my number in {numberOfGuess} guesses!')





