import discord
from discord.ext import commands

class Repeat(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
          
     @commands.command()
     async def repeat(self, ctx, *, message):
          
          """[repeat]

          Args:
          ctx ([discord]): [contexto]
          message ([str]): [mensaje a repetir]
          """ 
          self.message = message

          if "im stupid" in self.message or self.message is "im stupid":
               self.stupid = "yeah, i also think you are stupid"
               await ctx.send(self.stupid)
               
          elif "im gay" in self.message or self.message is "im gay":
               self.gay = "yeah, i also think you are gay"
               await ctx.send(self.gay)
          else:
               await ctx.send(self.message)

def setup(bot):
     bot.add_cog(Repeat(bot))