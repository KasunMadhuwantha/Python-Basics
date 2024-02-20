#value = input("please enter value= \n ")

#print(value)

import sys
import random


player_choice = input("Enter...\n 1 for rock \n 2 for paper \n 3 for siccor \n\n" )

player = int(player_choice)

if player <1 or player >3:
  sys.exit("You must enter 1,2 or 3")

pc_choice = random.choice("123")
computer = int(pc_choice)
print("")
print("you chose" + player_choice)
print("Python chose" + pc_choice)
print("")

if player == 1 and computer == 3:
  print("you win!")
elif player == 2 and computer == 1:
  print("You win!")
elif player == 3 and computer == 2:
  print("You win!")
elif player == computer:
  print("Draw!")

else:
  print("python win!")
        