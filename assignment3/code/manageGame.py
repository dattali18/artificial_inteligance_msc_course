# -*- coding: utf-8 -*-
import Mancala


class GameManager:
    def __init__(self):
        # Initialize the current player to the human.
        self.current_player = "human"
        self.Mancala = Mancala.Mancala()

    def switch_turn(self):
        # Switch the current player from the human to the computer or vice versa.
        if self.current_player == "human":
            self.current_player = "computer"
        else:
            self.current_player = "human"

    def turn_input(self):
        if self.current_player == "human":
            while not (self.Mancala.read_input_and_update_board('O')):
                print("Try again")
        else:
            move = self.Mancala.inputComputer()
            # print("next move is: ", move)

    def game_over(self):
        return self.Mancala.check_game_over()

    def print_board(self):
        self.Mancala.print_board()

    def check_winner(self):
        return self.Mancala.check_winner()


if __name__ == "__main__":
    # Create a new game with 8 rows and 8 columns
    game = GameManager()
    game.print_board()

    # Place a piece on the board at row 0, column 0

    # Flip any pieces that need to be flipped
    x = 0
    while not (game.game_over()) and x != 99:
        print("Turn of ", game.current_player)
        game.turn_input()
        game.switch_turn()
        print("Current Board:")
        game.print_board()
        # x=int(input("Enter a number (99 to exit)"))

    print("GAME OVER")
    print("The winner is: ", game.check_winner()[0])
