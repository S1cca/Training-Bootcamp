"""
Dice Rolling Simulator
Project Brief
The Goal of this project, like the title suggests, involves writing a program that simulates rolling a
dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever
other integer you prefer — the number of sides on the die is up to you.) The program will print
what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need
to set the min and max number that your dice can produce. For the average die, that means a
minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number
within that range and prints it.
Concepts to keep in mind:
● Random
● Integer
● Print
● While Loops
Deliverables
This project will help establish a solid foundation for basic concepts.
"""

import random

min_val = 1
max_val = 6

roll_again = True

while roll_again:
    print("Rolling the dice...")
    print("The value is", random.randint(min_val, max_val))
    roll_again = input("Roll the dice again? (y/n) ") == "y"


    

