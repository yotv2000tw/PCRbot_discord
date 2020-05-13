import discord
import json
import os
import keep_alive
from discord.ext import commands

with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='[')
client = discord.Client()

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 280037932298010624

@bot.event
async def on_ready():
    act = discord.Game('with 雪楓')
    await bot.change_presence(status=discord.Status.dnd, activity=act)
    print("bot is online.")

@bot.command()
@commands.check(check_if_it_is_me)
async def only_for_me(ctx):
    await ctx.send('I know you!')

@bot.event
async def on_member_join(member):
    print(F"{member} join")

@bot.event
async def on_member_remove(member):
    print(F"{member} leave")

@bot.command()
@commands.check(check_if_it_is_me)
async def load(ctx,extension):
      bot.load_extension(F'cmds.{extension}')
      await ctx.send(F"Loaded {extension} done.")

@bot.command()
@commands.check(check_if_it_is_me)
async def unload(ctx,extension):
      bot.unload_extension(F'cmds.{extension}')
      await ctx.send(F"Un-loaded {extension} done.")

@bot.command()
@commands.check(check_if_it_is_me)
async def reload(ctx,extension):
      bot.reload_extension(F'cmds.{extension}')
      await ctx.send(F"Re-loaded {extension} done.")

@bot.command()
async def id(ctx):
  await ctx.send(F'{ctx.message.author.id} is your id.')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f"cmds.{Filename[:-3]}")

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])