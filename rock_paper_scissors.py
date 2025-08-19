#!/usr/bin/env python3

import random


rock = '''
    _______
___'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
___'   ____)____
          ______)
          ______)
        _______)
---._________)
'''

scissors = '''
    _______
___'   ____)____
          ______)
        _________)
        (____)
---.____(____)
'''

asciiart = [rock, paper, scissors]




player_choice = int(input("0 = rock\n1 = paper\n2 = scissors\nur choice: "))


if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("invalid input.")
    exit()
    #make a loop here that will keep asking user untill input is valid



computer_choice = random.choice(asciiart)

print("computer's choice:")
print(computer_choice)


if computer_choice == rock:
    computer_choice = 0

elif computer_choice == paper:
    computer_choice = 1

else:
    computer_choice = 2



#rules of da game   

if player_choice == computer_choice:
    print("it's a tie")

elif player_choice == 0 and computer_choice == 1:
    print("you LOSE")

elif player_choice == 0 and computer_choice == 2:
    print("you WIN!")

elif player_choice == 1 and computer_choice == 0:
    print("you WIN!")

elif player_choice == 1 and computer_choice == 2:
    print("you LOSE")

elif player_choice == 2 and computer_choice == 0:
    print("you LOSE")

elif player_choice == 2 and computer_choice == 1:
    print("you WIN!")

