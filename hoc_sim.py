import random
# You will need to install matplotlib with pip to view coronation histograms!
import matplotlib.pyplot as plt

## Sample bot that implements a basic "Big Money" style strategy. In the future
## this should be its own script to be imported, as well as optimizing the number
## of arguments to pass.
def botTurn(budget, handPoint, deckPoint, princessBacked):
    scoreChange = 0
    deckChange = 0
    log = ""
    if princessBacked != True:
        if budget >= 6:
            princessBacked = True
            deckChange += 6
            scoreChange += 6
            log += "Backed Lulu\nDomain: "
            for domain in range(3):
                card = hand.pop()
                log += str(card)
                if card == 1:
                    scoreChange -= 2
            log += "\n"
        elif budget >= 3:
            log += "Bought: City\n"
            discard.append(2)
    else:
        if handPoint < 0:
            log += "Scored: "
            for card in hand:
                if card < 0:
                    match card:
                        case -2:
                            scoreChange += 2
                            log += "Royal Maid "
                        case -3:
                            scoreChange += 3
                            log += "Senator "
                        case -6:
                            scoreChange += 6
                            log += "Duke "
                    hand.remove(card)
            log += "\n"
        else:
            if budget >= 8:
                deckChange += 6
                discard.append(-6)
                log += "Bought: Duke\n"
            elif budget >= 6:
                discard.append(3)
                log += "Bought: Large City\n"
            elif budget >= 5:
                deckChange += 3
                discard.append(-3)
                log += "Bought: Senator\n"
            elif budget >= 3:
                deckChange += 2
                discard.append(-2)
                log += "Bought: Royal Maid\n"
    return [princessBacked, scoreChange, deckChange, log]

## This is a highly simplified version of Heart of Crown, where a card can only
## generate gold, be worth points, or neither. The convention used here is positive
## numbers represent that much gold, while negative numbers represent point cards.

## We will run 1000 solitaire games, store the number of turns to coronation for
## each, and then create a histogram.
turnCounts = []

for iterations in range(1000):
    ## The standard starting deck has seven Farming Villages and three Apprentice
    ## Maids (represented as 0 since they are worth no gold and we have do not
    ## intend to use their -2 VP value.)
    deck = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    random.shuffle(deck)
    hand = []
    discard = []
    princessBacked = False
    points = 0
    turns = 0
    deckPoints = 0
    log = ""
    while points < 20:
        turns += 1
        log += "Turn {}:\n".format(turns)
        for draw in range(5):
            if len(deck) == 0:
                deck = discard
                discard = []
                random.shuffle(deck)
            hand.append(deck.pop())
        hand.sort()
        log += "Draw: {}\n".format(hand)
        handMoney = 0
        handPoint = 0
        for card in hand:
            if card > 0: handMoney += card
            elif card < 0: handPoint += card
        result = botTurn(handMoney, handPoint, deckPoints, princessBacked)
        princessBacked = result[0]
        points += result[1]
        deckPoints += result[2]
        log += result[3]
        while len(hand) > 0:
            discard.append(hand.pop())
    # View an arbitrary game log for debugging purposes.
    if iterations == 15:
        print(log)
    turnCounts.append(turns)

plt.hist(turnCounts, 10)
plt.show()
