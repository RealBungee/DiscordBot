#bot.py
import os
import random
import threading

from dotenv import load_dotenv
from discord.ext import commands
from FundingScraper import getBTCFunding
from FundingScraper import getETHFunding
from FundingScraper import refreshPage
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

bot = commands.Bot(command_prefix='!')

print("---------------Sexy bot is starting---------------------")
@bot.command()
async def btc(ctx):
    await ctx.send(getBTCFunding())
    print("Scraping BTC funding")

@bot.command()
async def eth(ctx):
    await ctx.send(getETHFunding())
    print("Scraping ETH funding")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

#idea for the bot - add the ability to show 1min - 15 min - 1H, 4H, D, W charts of coins
def autoCall():
    threading.Timer(60.0, autoCall).start()
    refreshPage()


bot.run(TOKEN)
