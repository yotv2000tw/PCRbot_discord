import discord
import random
from discord.ext import commands
from core.classes import Cog_extension
import json
with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 280037932298010624

class react(Cog_extension):
    @commands.command()
    @commands.check(check_if_it_is_me)
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata['Pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    @commands.check(check_if_it_is_me)    
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(react(bot))