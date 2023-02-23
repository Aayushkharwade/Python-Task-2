#random libeary
import random

#variables
options = ("rock" , "paper", "scissor")
player = None
computer = random.choice(options)

while True :
    player = None
    computer = random.choice(options)
#if invalid choice
    while player not in options:
        player = input("enter the choice (rock, paper, scissor):")

#choice display
    print(f"player : {player}")
    print(f"computer : {computer}")
  
#logic
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
        

       


