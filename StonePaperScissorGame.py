# This is a two-player game where each player chooses one object.  As we know, there are three objects, stone, paper,
# and scissor. So, the result will be

# Stone vs. Paper: Paper will wrap the stone hence paper wins.
# Paper vs. Scissor: Scissor will cut the paper, hence Scissor is winner
# Scissor vs. Stone: Stone will crush  scissor , hence stone is winner
# In situations where both players choose the same object, the result will be a draw.

# You have to use a random choice function to select between, stone, paper, scissor
# You do not have to use a print statement in case of the above function.
# Then you have to give input from your side.
# After getting ten consecutive inputs, the computer will show the result based on each iteration.
# You have to use loops(while loop is preferred).

import random
li = ['st', 'pa', 'sc']
# print(random.choice(li))

total_chance = 10
no_of_chances = 0
no_of_computer_chance = 0
no_of_human_chance = 0

print("st for Stone\npa for Paper\nsc for Scissor\n")

while no_of_chances<total_chance:
    inp = input("Stone, Paper,Scissor")
    ran = random.choice(li)

    if inp == ran:
        print("Game tie, both selected same\n")

        # if user input stone
    elif inp == 'st' and ran == 'pa':
        no_of_computer_chance = no_of_computer_chance+1
        print(f"your guess {inp} and computer guess {ran} \n")
        print("Computer win 1 point\n")
        print(f"your point is {no_of_human_chance} and computer point is {no_of_computer_chance}\n")

    elif inp == 'st' and ran == 'sc':
        no_of_human_chance = no_of_human_chance+1
        print(f"your guess {inp} and computer guess {ran} \n")
        print("You win 1 point")
        print(f"your point is {no_of_human_chance} and computer point is {no_of_computer_chance}")

        # if user input paper
    elif inp == 'pa' and ran == 'sc':
        no_of_computer_chance = no_of_computer_chance + 1
        print(f"your guess {inp} and computer guess {ran} \n")
        print("Computer win 1 point\n")
        print(f"your point is {no_of_human_chance} and computer point is {no_of_computer_chance}\n")

    elif inp == 'pa' and ran == 'st':
        no_of_human_chance = no_of_human_chance + 1
        print(f"your guess {inp} and computer guess {ran} \n")
        print("You win 1 point")
        print(f"your point is {no_of_human_chance} and computer point is {no_of_computer_chance}")

        # if user input scissor
    elif inp == 'sc' and ran == 'st':
        no_of_computer_chance = no_of_computer_chance + 1
        print(f"your guess {inp} and computer guess {ran} \n")
        print("Computer win 1 point")
        print(f"your point is {no_of_human_chance} and computer point is {no_of_computer_chance}")

    elif inp == 'sc' and ran == 'pa':
        no_of_human_chance = no_of_human_chance + 1
        print(f"your guess {inp} and computer guess {ran} \n")
        print("You win 1 point")
        print(f"your point is {no_of_human_chance} and computer point is {no_of_computer_chance}")

    else:
        print("next round\n")

    no_of_chances = no_of_chances+1
    print(f"{total_chance - no_of_chances} is left out of {total_chance} \n")

print("Game Over")

if no_of_human_chance == no_of_computer_chance:
    print("Game tie")

elif no_of_human_chance>no_of_computer_chance:
    print("You won")

else:
    print("Computer won")

print(f"{no_of_human_chance} and {no_of_computer_chance}")









