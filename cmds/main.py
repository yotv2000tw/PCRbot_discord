import discord
from discord.ext import commands
from core.classes import Cog_extension

class Main(Cog_extension):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F"{round(self.bot.latency*1000)}ms")
def setup(bot):
    bot.add_cog(Main(bot))