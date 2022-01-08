# Discord Bot Nitro Generator

# Python 3.x needed
# Libraries: asyncio, discord, typing, random, time
COOLDOWN = 1 # w sekundach
DLUGOSC = 16
TOKEN = 'ODEzNzg5OTUyNjY0MDEwNzUz.YDUa9A.IpykB85ARssRzlIDJrSv49VyWa8'
PREFIX = 'g!'

import asyncio
import discord
import typing
from discord.ext import commands
from random import randint
from time import sleep

bot = commands.Bot(command_prefix=PREFIX)
st = 'ABCDEFGHIJKLMNOPRSTUWYZXabcdefghijklmnoprstuwyzx1234567890'

def genkod():
    out = ''
    for i in range(DLUGOSC):
        out += st[randint(0, len(st)-1)]
    return out

@bot.command(name='nitro')
async def generate(ctx, count: int = 0):
    if(count == 0):
        await ctx.send(f"Poprawne uzycie: {PREFIX}gen [ilosc kodow]")
    else:
        for i in range(count):
            await ctx.message.author.send(f'discord.gift/{genkod()}')
            sleep(COOLDOWN)

bot.run(TOKEN)

# Discord Bot Nitro Generator
