#-----------------------------------------------------------------------------
# Name:        Guess the Number
# Purpose:     Write a program that generates a random number between `1` and `10` and keeps asking the user to guess it using a `while` loop **until they guess correctly**.
#
# Author:      Aleeza Siddiqui
# Created:     5-Mar-2025
#-----------------------------------------------------------------------------
import random
secret_number = random.randint(1, 10)
#guessing
while True:
    guess = int(input("Guess the number:" ))
    if guess == secret_number:
        print("Correct! Congrats!")
        break
    else:
        print("Wrong! try again!")
