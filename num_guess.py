#!usr/bin/env python3
# Made by Maximiliano Fairman
# Created on oct 16th 2025

# Constant for the correct number
CORRECT_NUMBER = 7  # You can choose any number between 0 and 9

# Ask the user to guess
guess = int(input("Guess a number between 0 and 9: "))

# If the guess is correct
if guess == CORRECT_NUMBER:
    print("You guessed correctly!")

# If the guess is incorrect
if guess != CORRECT_NUMBER:
    print("You guessed wrong")
