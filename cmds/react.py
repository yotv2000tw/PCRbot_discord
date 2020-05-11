import discord
from discord.ext import commands
from core.classes import Cog_extension
import json
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

class react(Cog_extension):
    @commands.command()
    async def 圖片(self,ctx):
        pic = discord.File(jdata['Pic'])
        await ctx.send(file= pic)
def setup(bot):
    bot.add_cog(react(bot))