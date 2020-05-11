import discord
import client
from discord.ext import commands

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

bot.run(client.key)