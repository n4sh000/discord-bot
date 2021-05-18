import discord
from discord.ext import commands
import colorama as c
r = c.Style.RESET_ALL
g = c.Fore.LIGHTGREEN_EX
m = c.Fore.LIGHTMAGENTA_EX
re = c.Fore.LIGHTRED_EX
b = c.Fore.CYAN

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Comando de ayuda de VoiT",
                              description="En el siguiente embed, se mostraran las diferentes funcionalidades del bot",
                              color=discord.Colour.random())
        embed.add_field(
                    name='`comandos de diversión`',
                    value='`lista de comandos de la seccion de diversión `',
                    inline=False
                )
        embed.add_field(name="py!meme", value="saca memes de reddit sintax: py!meme", inline=False)
        embed.add_field(name="py!say", value=" repite lo que le digas, sintax: py!say [mensaje a repetir]",
                        inline=False)
        embed.add_field(name="py!dumb",
                        value="repitira lo que le digas pero de manera tonta, sintax:py!dumb [mensaje a repetir]",
                        inline=False)
        embed.add_field(name="py!cap", value="va a decir una mentira sintax: py!cap")
        embed.add_field(
            name='`comandos útiles`',
            value='`lista de comandos de la seccion de utilidad `',
            inline=False
        )
        embed.add_field(name="py!google", value="va a buscar en google lo que digas,  sintax: py!google [busqueda]",
                        inline=False)
        embed.add_field(name="py!contact",
                        value="manda un embed con los medios para contactar al creador del bot, sintax: py!contact",
                        inline=False)
        embed.add_field(name="py!avatar", value="manda en un embed el avatar de un usuario, sintax: py!avatar @usuario",
                        inline=False)
        embed.add_field(
            name="`comandos RPG en desarrollo`",
            value="`coming soon...`"
        )
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
