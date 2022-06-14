# Code support for translating card names to money/VP values.

def getGoldValue(card):
    match card:
        case "Farming Village":
            return 1
        case "City":
            return 2
        case "Large City":
            return 3
        case "Magic Lamp":
            return 3
        case _:
            return 0

def getVPValue(card):
    match card:
        case "Apprentice Maid":
            return -2
        case "Royal Maid":
            return 2
        case "Senator":
            return 3
        case "Duke":
            return 6
        case _:
            return 0
            
