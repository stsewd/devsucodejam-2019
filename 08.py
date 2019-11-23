# Rock Paper Scissors Lizard Spock

paper = 'paper'
rock = 'rock'
scissors = 'scissors'
lizard = 'lizard'
spock = 'spock'

allowed = {paper, rock, scissors, lizard, spock}

rules = {
    paper: {rock, spock},
    rock: {scissors, lizard},
    scissors: {paper, lizard},
    lizard: {paper, spock},
    spock: {scissors, rock},
}

result_tied = 'players tied'
result_won_1 = 'player {} won by 1 point'
result_won_x = 'player {} won by {} points'

def rochambeau(player1, player2):
    if not player1 or not player2:
        return result_tied
    points1 = 0
    points2 = 0
    for p1, p2 in zip(player1, player2):
        if p1 == p2:
            continue

        if p1 not in allowed and p2 not in allowed:
            continue

        if p1 not in allowed:
            points2 += 1
            continue
        if p2 not in allowed:
            points1 += 1
            continue

        p1_won = False
        p2_won = False
        if p2 in rules[p1]:
            p1_won = True
        if p1 in rules[p2]:
            p2_won = True

        if p2_won and p1_won:
            continue
        if p2_won:
            points2 += 1
        if p1_won:
            points1 += 1

    if points2 > points1:
        if points2 > 1:
            return result_won_x.format('2', points2)
        else:
            return result_won_1.format('2')
    elif points1 > points2:
        if points1 > 1:
            return result_won_x.format('1', points1)
        else:
            return result_won_1.format('1')
    else:
        return result_tied


def test():
    result = rochambeau(
        ["rock", "lizard", "scissors", "scissors"],
        ["paper", "rock", "spock", "paper"],
    )
    assert result == 'player 2 won by 3 points'

