from discord.ext import commands

class Rpg(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
          #self.enemies
          
def setup(bot):
     bot.add_cog(Rpg(bot))