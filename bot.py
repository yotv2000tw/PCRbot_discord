import discord
import client
import json
import os
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
async def load(ctx,extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F"Loaded {extension} done.")

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F"Un-loaded {extension} done.")

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F"Re-loaded {extension} done.")

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f"cmds.{Filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])