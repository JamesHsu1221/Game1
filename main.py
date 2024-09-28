from player_choose import player_choose
from computer_random import computer_random


if __name__ == "__main__":
    player_choice = player_choose()
    computer_choice = computer_random()

    if computer_choice == 1:
        print ("Computer select paper")
    elif computer_choice == 2:
        print ("Computer select scissors")
    else:
        print ("Computer select stone")

    if player_choice == computer_choice:
        print ("It's a tie!")
    elif (player_choice == 1 and computer_choice == 2) or\
         (player_choice == 2 and computer_choice == 3) or\
         (player_choice == 3 and computer_choice == 1):
        print ("You lose!")
    else:
        print("You win!")

    
    
                   
