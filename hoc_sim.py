import random
# You will need to install matplotlib with pip to view coronation histograms!
import matplotlib.pyplot as plt
import supportLaolily as bot

## This is a highly simplified version of Heart of Crown, where a card can only
## generate gold, be worth points, or neither. The convention used here is positive
## numbers represent that much gold, while negative numbers represent point cards.

## We will run 1000 solitaire games, store the number of turns to coronation for
## each, and then create a histogram.
turnCounts = []

for iteration in range(1000):
    ## The standard starting deck has seven Farming Villages and three Apprentice
    ## Maids (represented as 0 since they are worth no gold and we have do not
    ## intend to use their -2 VP value.)
    deck = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    random.shuffle(deck)
    hand = []
    discard = []
    domain = []
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
        field = {
            "hand": hand,
            "deck": deck,
            "discard": discard,
            "domain": domain,
            "points": points,
            "deckPoints": deckPoints
        }
        result = bot.botTurn(field)
        hand = result[0]["hand"]
        deck = result[0]["deck"]
        discard = result[0]["discard"]
        domain = result[0]["domain"]
        points = result[0]["points"]
        deckPoints = result[0]["deckPoints"]
        log += result[1]
        while len(hand) > 0:
            discard.append(hand.pop())
    if iteration == 15:
        print(log)
    turnCounts.append(turns)

plt.gca().set_ylim([0, 300])
plt.hist(turnCounts, [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
plt.show()
