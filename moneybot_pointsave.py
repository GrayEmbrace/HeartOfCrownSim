## This is a WIP bot to implement a strategy where you do not play Succession
## cards until there are 20 VP in your deck. Importing this file does not work
## due to variable scope, but I would like it to work.

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
        if handPoint < 0 and deckPoint >= 20:
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
            elif budget >= 3 and deckPoint <= 20:
                deckChange += 2
                discard.append(-2)
                log += "Bought: Royal Maid\n"
    return [princessBacked, scoreChange, deckChange, log]
