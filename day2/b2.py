import sys

file = sys.argv[1]
# file = 'tempA.in'

with open(file, 'r') as f:
    lines = f.readlines()


def calc_winner(opp_guess, my_guess):
    if opp_guess == 'A':
        if my_guess == 'X':
            return 0
        elif my_guess == 'Y':
            return 1
        else:
            return -1

    if opp_guess == 'B':
        if my_guess == 'Y':
            return 0
        elif my_guess == 'Z':
            return 1
        else:
            return -1

    if opp_guess == 'C':
        if my_guess == 'Z':
            return 0
        elif my_guess == 'X':
            return 1
        else:
            return -1


def calc_score(opp_guess, my_guess):
    score = 0

    winner = calc_winner(opp_guess, my_guess)
    if winner == 1:
        score += 6
    elif winner == 0:
        score += 3

    if my_guess == 'X':
        score += 1
    elif my_guess == 'Y':
        score += 2
    else:
        score += 3

    return score


def calc_my_guess(opp_guess, outcome):
    """X means you lose, Y means you draw, Z means you win"""
    if opp_guess == 'A':
        if outcome == 'X':
            return 'Z'
        elif outcome == 'Y':
            return 'X'
        else:
            return 'Y'

    if opp_guess == 'B':
        if outcome == 'X':
            return 'X'
        elif outcome == 'Y':
            return 'Y'
        else:
            return 'Z'

    if opp_guess == 'C':
        if outcome == 'X':
            return 'Y'
        elif outcome == 'Y':
            return 'Z'
        else:
            return 'X'


total_score = 0
for l in lines:
    opp_guess, outcome = l.strip().split()
    my_guess = calc_my_guess(opp_guess, outcome)
    total_score += calc_score(opp_guess, my_guess)

print(total_score)

