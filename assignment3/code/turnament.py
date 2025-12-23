import time
import copy
import sys

# --- 1. Game Constants & Logic ---
VICTORY = 10000
LOSS = -10000


class Mancala:
    def __init__(self, board=None):
        if board:
            self.board = list(board)
        else:
            self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def check_game_over(self):
        side_o_empty = all(x == 0 for x in self.board[0:6])
        side_x_empty = all(x == 0 for x in self.board[7:13])
        return side_o_empty or side_x_empty

    def check_winner(self):
        # Calculate final scores including remaining stones
        score_o = self.board[6]
        score_x = self.board[13]
        remaining_o = sum(self.board[0:6])
        remaining_x = sum(self.board[7:13])

        final_o = score_o + remaining_o
        final_x = score_x + remaining_x

        if final_x > final_o:
            return ["Computer (X)", final_x, final_o]
        elif final_o > final_x:
            return ["Computer (O)", final_o, final_x]
        else:
            return ["Tie", final_x, final_o]

    def value(self):
        if self.check_game_over():
            winner, s1, s2 = self.check_winner()
            if winner == "Computer (X)":
                return VICTORY
            elif winner == "Computer (O)":
                return LOSS
            else:
                return 0
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
        current_index = pit_index

        while stones > 0:
            current_index = (current_index + 1) % 14
            if player == 'O' and current_index == 13: continue
            if player == 'X' and current_index == 6: continue
            self.board[current_index] += 1
            stones -= 1

        # Rule 1: Repeat Turn
        if (player == 'O' and current_index == 6) or (player == 'X' and current_index == 13):
            return True

        # Rule 2: Capture
        if self.board[current_index] == 1:
            is_own_side = (0 <= current_index <= 5) if player == 'O' else (7 <= current_index <= 12)
            if is_own_side:
                opposite_index = 12 - current_index
                if self.board[opposite_index] > 0:
                    captured = self.board[opposite_index] + 1
                    self.board[opposite_index] = 0
                    self.board[current_index] = 0
                    store = 6 if player == 'O' else 13
                    self.board[store] += captured
        return False


# --- 2. Alpha Beta Logic (Adapted for Dynamic Depth) ---
def abmax(gm, d, a, b):
    if d == 0 or gm.check_game_over(): return [gm.value(), 0]
    v = float("-inf")
    ns = gm.find_valid_moves('X')
    bestMove = 0
    if not ns: return [gm.value(), 0]  # Handle no moves
    for st in ns:
        tmp = abmin(st, d - 1, a, b)
        if tmp[0] > v:
            v = tmp[0]
            bestMove = st
        if v >= b: return [v, st]
        if v > a: a = v
    return [v, bestMove]


def abmin(gm, d, a, b):
    if d == 0 or gm.check_game_over(): return [gm.value(), 0]
    v = float("inf")
    ns = gm.find_valid_moves('O')
    bestMove = 0
    if not ns: return [gm.value(), 0]  # Handle no moves
    for st in ns:
        tmp = abmax(st, d - 1, a, b)
        if tmp[0] < v:
            v = tmp[0]
            bestMove = st
        if v <= a: return [v, st]
        if v < b: b = v
    return [v, bestMove]


def get_best_move(gm, player, depth):
    if player == 'X':
        val, move = abmax(gm, depth, LOSS - 1, VICTORY + 1)
    else:
        val, move = abmin(gm, depth, LOSS - 1, VICTORY + 1)
    return move


# --- 3. Tournament Runner ---
def run_match(depth_o, depth_x):
    gm = Mancala()
    turn = 'O'
    moves_o = 0;
    time_o = 0
    moves_x = 0;
    time_x = 0

    while not gm.check_game_over():
        start = time.time()
        d = depth_o if turn == 'O' else depth_x

        # AI Selection
        next_state = get_best_move(gm, turn, d)

        if next_state == 0: break  # No valid moves

        duration = time.time() - start
        if turn == 'O':
            moves_o += 1;
            time_o += duration
        else:
            moves_x += 1;
            time_x += duration

        # Detect if it was a repeat turn (heuristic: check if store increased by < stones in hand...
        # actually easier to just re-simulate to check the flag)
        repeat = False
        # Find which move was made to check repeat rule
        possible = gm.find_valid_moves(turn)
        for i in range(len(possible)):
            if possible[i].board == next_state.board:
                # We need to re-run make_move to see if it returns True
                # Re-create temp board
                temp = Mancala(list(gm.board))
                # We don't know the index easily, but we know the resulting board.
                # Let's just update the board and switch turn if store didn't cause repeat.
                # Actually, correct way:
                # Iterate indices, simulate, match board, check flag.
                start_idx, end_idx = (0, 6) if turn == 'O' else (7, 13)
                for pit in range(start_idx, end_idx):
                    if gm.board[pit] > 0:
                        t = Mancala(list(gm.board))
                        r = t.make_move(pit, turn)
                        if t.board == next_state.board:
                            repeat = r
                            break
                break

        gm = next_state
        if not repeat:
            turn = 'X' if turn == 'O' else 'O'

    winner, s1, s2 = gm.check_winner()
    # Normalize scores: s1 is winner's score, s2 is loser's.
    if "X" in winner:
        final_x, final_o = s1, s2
    elif "O" in winner:
        final_o, final_x = s1, s2
    else:
        final_x, final_o = s1, s2

    return {
        "depth_o": depth_o, "depth_x": depth_x,
        "winner": winner, "score_o": final_o, "score_x": final_x,
        "time_o": time_o / max(1, moves_o), "time_x": time_x / max(1, moves_x)
    }


# --- 4. Main Execution ---
if __name__ == "__main__":
    depths = [1, 2, 5]
    print(f"{'Agent O':<8} | {'Agent X':<8} | {'Winner':<15} | {'Score':<8} | {'Time O':<8} | {'Time X':<8}")
    print("-" * 75)

    import itertools

    for d1, d2 in itertools.product(depths, depths):
        res = run_match(d1, d2)
        print(
            f"{d1:<8} | {d2:<8} | {res['winner']:<15} | {res['score_o']}-{res['score_x']:<6} | {res['time_o']:.4f}   | {res['time_x']:.4f}")