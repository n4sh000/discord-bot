import discord
from discord.ext import commands

class Helloworld(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
     
     @commands.command()
     async def helloworld(self, ctx):
          await ctx.send('print("Hello world!")')
     
def setup(bot):
     bot.add_cog(Helloworld(bot))