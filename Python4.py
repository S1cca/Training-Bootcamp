"""
Remember Adventure? Well, we’re going to build a more basic version of that. A complete text
game, the program will let users move through rooms based on user input and get descriptions
of each room. To create this, you’ll need to establish the direction in which the user can move, a
way to track how far the user has moved (and therefore which room he/she is in), and to print
out a description. You’ll also need to set limits for how far the user can move. In other words,
create “walls” around the rooms that tell the user, “You can’t move further in this direction.”
Concepts to keep in mind:
"""

House=("Kitchen","Living Room","bedroom","Dining Room")
position = 0

print (f"Welcome to our adventure game. We are in a house with 4 rooms. You are now in the {House[position]}")
move = input(" Do you wanna move (yes/no): ")
if move == "yes":
    print(f"You are currently in the {House[position]}")
    direction = input("which way would you wanna go? (forward/backward): ")
    ##steps = int(input("How many steps would you wanna move?(a number): "))
    ## Rooms are all in horizontal lines, Room 1 -> Room 2 -> Room 3 -> Room 4
    if direction == "forward":
        steps = int(input("How many steps would you wanna move?(a number): "))
        if steps > 0 and steps < (5 - position):
            position += steps
            print(f"You took {steps} steps, you are now in {House[position]}")
        elif steps == 0:
            print(f"You have not moved, You are still in the {House[position]}")
        else:
            print(f"You can’t move further in this direction, you can not move {steps} steps")
    elif direction == "backward":
        steps = int(input("How many steps would you wanna move?(a number): "))
        if steps > 0 and steps < (5 - position):
            if (position - steps) < 0:
                print(f"You cant move that many steps, you would go over the wall")
            else:
                position -= steps
                print(f"You took {steps} steps, you are now in {House[position]}")
        elif steps == 0:
            print(f"You have not moved, You are still in the {House[position]}")
        else:
            print(f"You can’t move further in this direction, you can not move {steps} steps")
    
    else:
        print ("please input only forward or backward")
else:
    print(f"You have not moved, You are still in the {House[position]}")






