# Lab 1
# Group 5
# Authors: Marvin Lew, Noa Tomas Mandorf, Chance Manning
# Date: 09/25/26

from rock_paper_scissors import rock_paper_scissors
from guessing_game import guessing_game

#Noa Mandorf
if __name__ == '__main__':

    while True:

        game_to_play = input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. ")

        if game_to_play == "1":
            print(guessing_game())
        elif game_to_play == "2":
            print(rock_paper_scissors())

        if input("Do you want to play again? (Y/N): ").upper() != "Y":
            break

    print("Thank you for playing!")

    def cube(number):
        """returns the cube of the number passed as an argument"""
        return number * number * number
