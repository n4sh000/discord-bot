import discord
from discord.ext import commands

class Dumb(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
          self.all = ''
          self.count = 0
          
     @commands.command()
     async def dumb(self, ctx, *, message: str):
          for letter in message:
               try:
                    if self.count % 2 is 1:
                         self.all += letter.upper()
                    else:
                         self.all += letter.lower()
                    
                    self.count += 1
               except Exception as e:
                    await ctx.send("Algo ha ido mal compa, aprende a usar el bot")
                    print(e)
                    break
          await ctx.send(self.all)
          self.all = ''
     
    
          
def setup(bot):
     bot.add_cog(Dumb(bot))