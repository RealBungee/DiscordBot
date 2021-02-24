#bot.py
import os
import random
import threading
import requests
import json
import discord

from dotenv import load_dotenv
from discord.ext import commands

#variables
fundingHead = "Binance\tBybit\tBitmex\tFTX\t\tOkex\tHuobi"
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
        await ctx.send(embed=printFunding(funding, arg))
    print("Getting " + arg.upper() + " funding")


#idea for the bot - add the ability to show 1min - 15 min - 1H, 4H, D, W charts of coins
def printFunding(funding, arg):
    string = "```" + fundingHead + "\n"
    embedVar = discord.Embed(title="Funding for: " + arg.upper(), color=0x00ff00)
    for e in exchanges:
        try:
            string += str("{0:.4f}".format(funding[e]['predictedRate'])) + "\t"
            embedVar.add_field(name = e, value = "{0:.4f}".format(funding[e]['predictedRate']))
        except KeyError:
            try:
                string += str("{0:.4f}".format(funding[e]['rate'])) + "\t"
                embedVar.add_field(name = e, value = "{0:.4f}".format(funding[e]['rate']))
            except KeyError:
                string += "No Data\t"
    string += "\n```"
    return embedVar


bot.run(TOKEN)
