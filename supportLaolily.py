# Bot that backs Laolily with Kurona. Does not consider Apprentice Maids.

def botTurn(field):
    log = ""
    handGold = 0
    handPoint = 0
    for card in field["hand"]:
        if card > 0:
            handGold += card
        elif card < 0:
            handPoint += abs(card)
    if len(field["domain"]) == 0:
        if handGold >= 8:
            log += "Backed Laolily+Kurona\nDomain: "
            field["hand"].sort()
            for domain in range(3):
                card = field["hand"].pop()
                field["domain"].append(card)
                log += str(card)
                if card == 1:
                    field["points"] -= 2
            field["discard"].append(-2)
            field["discard"].append(-2)
            field["discard"].append(-2)
            field["discard"].append(-2)
            field["discard"].append(-2)
            log += "\n"
        elif handGold >= 6:
            log += "Bought: Large City\n"
            field["discard"].append(3)
        elif handGold >= 3:
            log += "Bought: City\n"
            field["discard"].append(2)
    else:
        if handPoint > 0:
            log += "Scored: "
            i = 0
            maidCount = 0
            while i < len(field["hand"]):
                card = field["hand"][i]
                if card < 0:
                    match card:
                        case -2:
                            field["points"] += 2
                            maidCount += 1
                            log += "Royal Maid "
                        case -3:
                            field["points"] += 3
                            log += "Senator "
                        case -6:
                            field["points"] += 6
                            log += "Duke "
                    field["hand"].pop(i)
                else:
                    i+=1
            log += "\n"
            if maidCount >= 2:
                field["points"] += 2
                log += "Kurona activated\n"
        else:
            if handGold >= 8:
                log += "Bought: Duke\n"
                field["discard"].append(-6)
                field["deckPoints"] += 6
            elif handGold >= 5:
                log += "Bought: Senator\n"
                field["discard"].append(-3)
                field["deckPoints"] += 3
            elif handGold >= 3:
                log += "Bought: Royal Maid\n"
                field["discard"].append(-2)
                field["deckPoints"] += 2
    return [field, log]
