#accepts an integer and returns a result between 1 and that input
def singleDice(sides):
    import random
    return random.randint(1,sides)

#accepts a string of xDy where x is the number of dice and y is the number of sides
#then uses the singleDice function to return a result
def multiDice(dice):
    import re
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

#so we have the dice functionality
#now we need to communicate with discord and get the user input
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
#get the token from the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    

# a bot command that takes in a string of xDy+z where x is the number of dice, y is the number of sides, and z is the modifier
# then uses the multiDiceMod function to return a result
@bot.command(name='roll', help='rolls a dice')
async def roll(ctx, *args):
    #get the input
    input = ''.join(args)
    #call the multiDiceMod function
    result = multiDiceMod(input)
    #send the result
    await ctx.send(result)

bot.run(TOKEN)