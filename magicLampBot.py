# Basic Bot + Magic Lamp

import cardLookup as cl

def botTurn(field):
    log = ""
    handGold = 0
    handPoint = 0
    for card in field["hand"]:
        handGold += cl.getGoldValue(card)
        vpValue = cl.getVPValue(card)
        if card == "Magic Lamp":
            field["discard"].append("Misfortune")
            field["discard"].append("Misfortune")
        if vpValue > 0: handPoint += vpValue
    if len(field["domain"]) == 0:
        if handGold >= 6:
            log += "Backed Lulu\nDomain: "
            field["points"] += 6
            field["hand"].sort(key=cl.getGoldValue)
            i = len(field["hand"]) - 1
            backedGold = 0
            while len(field["domain"]) < 3 and backedGold < 6:
                card = field["hand"][i]
                backedGold += cl.getGoldValue(card)
                if card != "Magic Lamp":
                    field["domain"].append(card)
                    field["hand"].pop(i)
                    log += str(card) + " "
                    if card == "Farming Village":
                        field["points"] -= 2
                i -= 1
            log += "\n"
        elif handGold >= 4 and not "Magic Lamp" in field["hand"] and not "Magic Lamp" in field["discard"] and not "Magic Lamp" in field["deck"]:
            log += "Bought: Magic Lamp\n"
            field["discard"].append("Magic Lamp")
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
    i = 0
    while i < len(field["hand"]):
        if field["hand"][i] == "Misfortune":
            field["hand"].pop(i)
        else:
            i += 1
    log += "Points: " + str(field["points"]) + "\n"
    return [field, log]
