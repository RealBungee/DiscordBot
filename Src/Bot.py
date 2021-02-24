#bot.py
import os
import random
import threading
import requests
import json

from tabulate import tabulate
from dotenv import load_dotenv
from discord.ext import commands
from FundingScraper import getBTCFunding
from FundingScraper import getETHFunding

#variables
fundingHead = "Binance \tBybit\tBitmex\tFTX\tOkex\tHuobi"
exchanges = "Binance", "Bybit", "Bitmex", "FTX", "Okex", "Huobi"
string = ""

headers = {
    'bybtSecret': 'dba42239741b482ab20cae5848c4185a'
}

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

@bot.command()
async def oi(ctx):
    params = {
        "interval": 0,
        "symbol": "BTC"
    }
    url = "https://open-api.bybt.com/api/pro/v1/futures/openInterest"
    response = requests.request("GET", url, headers=headers, data = params)
    print(response.json())

@bot.command()
async def f(ctx, arg):
    url = "https://open-api.bybt.com/api/pro/v1/futures/funding_rates?symbol=" + arg.upper()
    response = requests.request("GET", url, headers=headers)
    try:
        funding = response.json()['data'][0]
    except IndexError:
        await ctx.send("```No data for " + arg.upper() + "```")
    else:
        await ctx.send(printFunding(funding))
    print("Getting " + arg.upper() + " funding")


#idea for the bot - add the ability to show 1min - 15 min - 1H, 4H, D, W charts of coins
def printFunding(funding):
    string = "```" + fundingHead + "\n"
    for e in exchanges:
        try:
            string += str(funding[e]['predictedRate']) + "\t"
        except KeyError:
            try:
                string += str(funding[e]['rate']) + "\t"
            except KeyError:
                string += "No Data\t"
    string += "\n```"
    return string


bot.run(TOKEN)
