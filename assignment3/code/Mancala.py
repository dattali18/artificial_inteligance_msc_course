import copy

VICTORY = 10000
LOSS = -10000


class Mancala:
    def __init__(self, board=None):
        # 0-5: Player O, 6: Store O
        # 7-12: Player X, 13: Store X
        if board:
            self.board = list(board)
        else:
            self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def check_game_over(self):
        side_o = all(x == 0 for x in self.board[0:6])
        side_x = all(x == 0 for x in self.board[7:13])
        return side_o or side_x

    def check_winner(self):
        score_o = self.board[6] + sum(self.board[0:6])
        score_x = self.board[13] + sum(self.board[7:13])
        if score_x > score_o:
            return ["Computer (X)", score_x]
        elif score_o > score_x:
            return ["Human (O)", score_o]
        else:
            return ["Tie", score_x]

    def value(self):
        if self.check_game_over():
            winner, score = self.check_winner()
            if winner == "Computer (X)":
                return VICTORY
            elif winner == "Human (O)":
                return LOSS
            else:
                return 0
        # Heuristic: Difference in stones in stores
        return self.board[13] - self.board[6]

    def find_valid_moves(self, player):
        valid_states = []
        start, end = (0, 6) if player == 'O' else (7, 13)
        for i in range(start, end):
            if self.board[i] > 0:
                new_game = Mancala(copy.deepcopy(self.board))
                new_game.make_move(i, player)
                valid_states.append(new_game)
        return valid_states

    def make_move(self, pit_index, player):
        stones = self.board[pit_index]
        self.board[pit_index] = 0
        current = pit_index
        while stones > 0:
            current = (current + 1) % 14
            if player == 'O' and current == 13: continue
            if player == 'X' and current == 6: continue
            self.board[current] += 1
            stones -= 1

        # Rule 1: Repeat turn
        if (player == 'O' and current == 6) or (player == 'X' and current == 13):
            return True

        # Rule 2: Capture
        if self.board[current] == 1:
            is_own = (0 <= current <= 5) if player == 'O' else (7 <= current <= 12)
            if is_own and self.board[12 - current] > 0:
                captured = self.board[12 - current] + 1
                self.board[12 - current] = 0
                self.board[current] = 0
                self.board[6 if player == 'O' else 13] += captured
        return False

    def inputComputer(self):
        import alphaBetaPruning
        print("Computer is thinking...")
        next_state = alphaBetaPruning.go(self)
        if next_state:
            self.board = next_state.board
        return next_state

    def read_input_and_update_board(self, player):
        try:
            val = int(input(f"Enter pit (0-5): "))
            if 0 <= val <= 5 and self.board[val] > 0:
                repeat = self.make_move(val, player)
                if repeat:
                    print("Play again!")
                    return False
                return True
            print("Invalid move.")
            return False
        except ValueError:
            return False

    def print_board(self):
        print("\n   " + "  ".join(f"{x:2}" for x in reversed(self.board[7:13])))
        print(f"{self.board[13]:2}" + " " * 22 + f"{self.board[6]:2}")
        print("   " + "  ".join(f"{x:2}" for x in self.board[0:6]) + "\n")