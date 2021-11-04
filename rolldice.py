
    #if the first letter is an a, remove the a and call the multiDiceMod function
def rollDice(dice):
    import re
    if dice[0].upper() == 'A':
        return multiDiceAdv(dice[1:], True)
    if dice[0].upper() == 'D' and re.match('^D[0-9]*D[0-9]+$',dice):
        return multiDiceAdv(dice[1:], False)
    if re.match('^[1-9][0-9]*\*[0-9]*D[0-9]+$',dice):
        dice  = dice.split('*')
        returning  = ""
        for i in range(int(dice[0])):
            returning += str(multiDiceMod(dice[1])) + " "
        return returning    
    return multiDiceMod(dice)

#accepts an integer and returns a result between 1 and that input
def singleDice(sides):
    import random
    return random.randint(1,sides)

#accepts a string of xDy where x is the number of dice and y is the number of sides
#then uses the singleDice function to return a result integer
def multiDice(dice):
    import re
    if dice[0] == 'D':
        dice = "1" + dice
    dice = re.split('D',dice)
    dice = [int(x) for x in dice]
    result = 0
    for i in range(dice[0]):
        result += singleDice(dice[1])
    return result

def multiDiceAdv(dice, adv):
    first = multiDiceMod(dice)
    second = multiDiceMod(dice)
    if adv:
        return max(first, second)
    else:
        return min(first, second)

#a function accepting xDy+z where x is the number of dice, y is the number of sides, and z is the modifier
#then uses the multiDice function to return a result
def multiDiceMod(dice):
    dice = dice.upper()
    if not isValidInput(dice):
        return "Invalid Format"
    import re
    dice = re.split('\+',dice)
    #call the multiDice function
    result = multiDice(dice[0])
    #check if there is a modifier
    if len(dice) > 1:
        result += int(dice[1])
    return result

#ensures the input is of the form Dy, xDy, Dy+z, or xDy+z
def isValidInput(input):
    import re
    if re.match('^[0-9]*D[0-9]+$',input):
        return True
    if re.match('^[0-9]*D[0-9]+\+[0-9]+$',input):
        return True
    return False