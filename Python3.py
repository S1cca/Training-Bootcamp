"""
Project Brief
Inspired by Summer Son’s Mad Libs project with Python. The program will first prompt the
user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc. Then,
once all the information has been inputted, the program will take that data and place them into a
premade story template. You’ll need prompts for user input, and to then print out the full story at
the end with the input included.
Concepts to keep in mind:
● Strings
● Variables
● Concatenation
● Print
Deliverables
A pretty fun beginning project that gets you thinking about how to manipulate user inputted data.
Compared to the prior projects, this project focuses far more on strings and concatenating.
Have some fun coming up with some wacky stories for this!
"""

#Mad Libs Generator

print("Input your words: ")
occupation = input("Occupation(a job): ")
noun1 = input("Noun:")
adjective1 = input("Adjective: ")
noun2 = input("Noun: ")
verb1 = input("Verb: ")
adjective2 = input("Adjective: ")
noun3 = input("Noun: ")
verb2 = input("Verb: ")
noun4 = input("Noun: ")
verb3 = input("Verb: ")

print(f"Today a {occupation} named {noun4} came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to {verb2} around a {adjective1} {noun3}. She said it was easy for her to learn her job because she loved to {verb1} when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near a {adjective2} {noun1}. That's very important! If you get too distracted in that situation you won't be able to {verb3} next to a {noun2}!")

