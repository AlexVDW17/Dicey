#accepts an integer and returns a result between 1 and that input
def singleDice(sides):
    import random
    return random.randint(1,sides)

#accepts a string of xDy where x is the number of dice and y is the number of sides
#then uses the singleDice function to return a result
def multiDice(dice):
    import re
    #convert all letters to uppercase
    dice = dice.upper()
    dice = re.split('D',dice)
    dice = [int(x) for x in dice]
    result = 0
    for i in range(dice[0]):
        result += singleDice(dice[1])
    return result

#a function accepting xDy+z where x is the number of dice, y is the number of sides, and z is the modifier
#then uses the multiDice function to return a result
def multiDiceMod(dice):
    import re
    dice = re.split('\+',dice)
    #call the multiDice function
    result = multiDice(dice[0])
    #check if there is a modifier
    if len(dice) > 1:
        result += int(dice[1])
    return result
