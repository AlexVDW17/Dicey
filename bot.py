import rolldice
import spells
import characters
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
#get the token from the .env file
#TO USE: CREATE A .env FILE IN THE SAME FOLDER AS THIS FILE with the following contents:
#DISCORD_TOKEN=your_token_here
#DISCORD_GUILD=Your_guild_name_here
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
@bot.command(name='r', help='rolls a dice given input xDy + z. use a xDy +z for advantage and d xDy + z for disadvantage')
async def roll(ctx, *args):
    input = ''.join(args)
    #call the multiDiceMod function
    result = rolldice.rollDice(input)
    #send the result
    print("[Roll] Command: " , input)
    print("[Roll] Result: " , result)
    await ctx.send(result)

@bot.command(name='s', help='Provides spell information given a spell name')
async def provideSpell(ctx, *args):
    input = ' '.join(args)
    input = input.title()
    #call the spellInfo function
    result = spells.findSpell(input)
    #send the result
    await ctx.send(result)

@bot.command(name='c', help='Provides character information give a name')
async def character(ctx, *args):
    input = ' '.join(args[1:])
    result = characters.perform(input, args[1])
    #send the result
    await ctx.send(result)


bot.run(TOKEN)

