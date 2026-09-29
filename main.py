# Lab 1
# Group 5
# Authors: Marvin Lew, Noa Tomas Mandorf, Chance Manning
# Date: 09/25/26

'''
   Allows the user to select what game you want to play and if you want to
   play again or switch the game up.
   Author: Chance Manning
   Author: Noa Mandorf
   '''


# Imports the 2 functions
from rock_paper_scissors import rock_paper_scissors
from guessing import guessing_game

if __name__ == '__main__':

    game_to_play = ''

# Main Loop - loops as long as the user wants to keep playing games
    while True:

        # Checks what game user wants to play
        if game_to_play not in( '1', '2' ):
            game_to_play = input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. ")

        # Selects the game
        if game_to_play == '1':
            guessing_game()
        elif game_to_play == '2':
            rock_paper_scissors()
        else:
            print("Please enter either 1 or 2.")
            continue

        # Asks user if they want to swap game
        switch_game = input("Do you want to switch game? (Y/N): ").upper()

        # Handles game swap or closes the game
        if switch_game == "Y":
            game_to_play = '2' if game_to_play == '1' else '1'
        else:
            break
    # Thanks the user for playing
    print("Thank you for playing!")
