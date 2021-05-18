import discord
from discord.ext import commands
import colorama as c
r = c.Style.RESET_ALL
g = c.Fore.LIGHTGREEN_EX
m = c.Fore.LIGHTMAGENTA_EX
re = c.Fore.LIGHTRED_EX
b = c.Fore.CYAN
class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        r = c.Style.RESET_ALL
        g = c.Fore.RED
        if isinstance(error, commands.CheckFailure):
            print(f'[{g}*{r}]{type(error)}')
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"no tienes permiso para ejecutar este comando: {ctx.message.content}"))
        
        if isinstance(error, commands.CommandNotFound):
            print(f'[{g}*{r}]{type(error)}')
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"El comando introducido no existe, , escribe py!help para leer la sintaxis: {ctx.message.content}"))
        
        if isinstance(error, commands.MissingRequiredArgument):
            print(f'[{g}*{r}]{type(error)}')
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Al comando le faltan parametros, escribe py!help para leer la sintaxis: {ctx.message.content}"))
        
        if isinstance(error, commands.BadArgument):
            print(f'[{g}*{r}]{type(error)}')
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"El comando está mal escrito, escribe py!help para leer la sintaxis: {ctx.message.content}"))


def setup(bot):
    bot.add_cog(Error(bot))