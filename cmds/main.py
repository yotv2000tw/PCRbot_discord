import discord
from discord.ext import commands
from core.classes import Cog_extension

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 280037932298010624

class Main(Cog_extension):    
    @commands.command()
    @commands.check(check_if_it_is_me)
    async def ping(self,ctx):
        await ctx.send(F"{round(self.bot.latency*1000)}ms")
        
def setup(bot):
    bot.add_cog(Main(bot))