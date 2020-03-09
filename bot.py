import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

bot.run(TOKEN)

@bot.command(name="RPSLS", help="rock paper sciccors more advanced")
async def rspls(ctx):
    await  ctx.send(random.choices(["Rock", "Paper", "Scissors", "Lizard", "Spock"]))
    