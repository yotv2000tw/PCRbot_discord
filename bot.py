import discord
import client
import json
from discord.ext import commands

with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print("bot is online.")

@bot.event
async def on_member_join(member):
    print(F"{member} join")

@bot.event
async def on_member_remove(member):
    print(F"{member} leave")

@bot.command()
async def ping(ctx):
    await ctx.send(F"{round(bot.latency*1000)}ms")

@bot.command()
async def Pic(ctx):
    pic = discord.File(jdata['Pic'])
    await ctx.send(file= pic)

bot.run(jdata['TOKEN'])