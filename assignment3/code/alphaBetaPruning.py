import Mancala

DEPTH = 2


def go(gm):
    # print("In go of game ", gm.board)
    # print("Turn of agent")
    obj = abmax(gm, DEPTH, Mancala.LOSS - 1, Mancala.VICTORY + 1)[1]
    # print("object board: ",obj)
    return obj


# s = the state (max's turn)
# d = max. depth of search
# a,b = alpha and beta
# returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmax(gm, d, a, b):
    # print("now calculate abmax")
    # print("d=",d)
    # print("alpha=",a)
    # print("beta=",b)
    if d == 0 or gm.check_game_over():
        # print("returns ", [gm.value()])
        return [gm.value(), 0]
    v = float("-inf")
    ns = gm.find_valid_moves('X')
    # print("next moves:", len(ns), " possible moves ")
    # print("valid moves: ", ns)
    bestMove = 0
    for st in ns:
        tmp = abmin(st, d - 1, a, b)
        if tmp[0] > v:
            v = tmp[0]
            bestMove = st
        if v >= b:
            return [v, st]
        if v > a:
            a = v
    return [v, bestMove]


# s = the state (min's turn)
# d = max. depth of search
# a,b = alpha and beta
# returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmin(gm, d, a, b):
    # print("now calculate abmin")
    # print("d=",d)
    # print("a=",a)
    # print("b=",b)

    if d == 0 or gm.check_game_over():
        # print("returns ", [gm.value()])
        return [gm.value(), 0]
    v = float("inf")

    ns = gm.find_valid_moves('O')
    # print("next moves:", len(ns), " possible moves ")
    bestMove = 0
    for st in ns:
        tmp = abmax(st, d - 1, a, b)
        if tmp[0] < v:
            v = tmp[0]
            bestMove = st
        if v <= a:
            return [v, st]
        if v < b:
            b = v
    return [v, bestMove]
