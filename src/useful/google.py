import discord
from discord.ext import commands
from googlesearch import search

class Google(commands.Cog):
     """[Google class]

     Args:
         commands ([cog]): [command extension]
     """
     def __init__(self, bot):
          self.bot = bot
          
     @commands.command()
     async def google(self,ctx, *, query):
          for i in search(query=query, stop=1):
               await ctx.send(i)
def setup(bot):
     bot.add_cog(Google(bot))