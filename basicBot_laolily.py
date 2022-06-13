## Variation of Basic Bot that backs Laolily instead of Lulu.

import cardLookup as cl

def botTurn(field):
    log = ""
    handGold = 0
    handPoint = 0
    for card in field["hand"]:
        handGold += cl.getGoldValue(card)
        vpValue = cl.getVPValue(card)
        if vpValue > 0: handPoint += vpValue
    if len(field["domain"]) == 0:
        if handGold >= 6:
            log += "Backed Laolily\nDomain: "
            field["hand"].sort(key=cl.getGoldValue)
            for domain in range(3):
                card = field["hand"].pop()
                field["domain"].append(card)
                log += str(card) + " "
                if card == "Farming Village":
                    field["points"] -= 2
            field["discard"].append("Royal Maid")
            field["discard"].append("Royal Maid")
            field["discard"].append("Royal Maid")
            field["discard"].append("Royal Maid")
            field["discard"].append("Royal Maid")
            log += "\n"
        elif handGold >= 3:
            log += "Bought: City\n"
            field["discard"].append("City")
    else:
        if handPoint > 0:
            log += "Scored: "
            i = 0
            while i < len(field["hand"]):
                card = field["hand"][i]
                vpValue = cl.getVPValue(card)
                if cl.getVPValue(card) > 0:
                    field["points"] += vpValue
                    log += card + " "
                    field["hand"].pop(i)
                else:
                    i += 1
            log += "\n"
        else:
            if handGold >= 8:
                log += "Bought: Duke\n"
                field["discard"].append("Duke")
                field["deckPoints"] += 6
            elif handGold >= 5:
                log += "Bought: Senator\n"
                field["discard"].append("Senator")
                field["deckPoints"] += 3
            elif handGold >= 3:
                log += "Bought: Royal Maid\n"
                field["discard"].append("Royal Maid")
                field["deckPoints"] += 2
    log += "Points: " + str(field["points"]) + "\n"
    return [field, log]
