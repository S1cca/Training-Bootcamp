"""
This project uses the random module in Python. The program will first randomly generate a
number unknown to the user. The user needs to guess what that number is. (In other words, the
user needs to be able to input information.) If the user’s guess is wrong, the program should
return some sort of indication as to how wrong (e.g. The number is too high or too low). If the
user guesses correctly, a positive indication should appear. You’ll need functions to check if the
user input is an actual number, to see the difference between the inputted number and the
randomly generated numbers, and to then compare the numbers.

"""

import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    guess_str = input("Guess a number between 1 and 100: ")
    try:
        guess = int(guess_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_guess()
    return guess

def check_guess(guess, target):
    if guess < target:
        print("The number is too low.")
    elif guess > target:
        print("The number is too high.")
    else:
        print("Congratulations, you guessed the number!")
    return False

def play_game():
    target = generate_random_number()
    while True:
        guess = get_user_guess()
        if check_guess(guess, target):
            break

play_game()
