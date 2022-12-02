import sys

file = sys.argv[1]

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


total_score = 0
for l in lines:
    opp_guess, my_guess = l.strip().split()
    total_score += calc_score(opp_guess, my_guess)

print(total_score)






