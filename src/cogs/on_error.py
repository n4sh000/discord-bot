import discord
from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"no tienes permiso para ejecutar este comando: {ctx.message.content}"))
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"El comando introducido no existe, , escribe py!help para leer la sintaxis: {ctx.message.content}"))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Al comando le faltan parametros, escribe py!help para leer la sintaxis: {ctx.message.content}"))
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"El comando está mal escrito, escribe py!help para leer la sintaxis: {ctx.message.content}"))


def setup(bot):
    bot.add_cog(Error(bot))