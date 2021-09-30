import rolldice
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
    result = rolldice.multiDiceMod(input)
    #send the result
    await ctx.send(result)

bot.run(TOKEN)

#need a persistent storage system for the bot

