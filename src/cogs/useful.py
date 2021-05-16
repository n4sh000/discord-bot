import discord
from discord.ext import commands
from googlesearch import search

from config import FORBIDDEN


class Google(commands.Cog):
    """[Google class]

    Args:
        commands ([cog]): [command extension]
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def google(self, ctx, *, query: str, results = 5):
        forbidden_word = False
        for word in query.split():
            for fword in FORBIDDEN:
                if word == fword:
                    await ctx.send("Esta palabra esta prohibida :/")
                    forbidden_word = True
                    return
                else:
                    forbidden_word = False

        id_usr = f'<@{ctx.author.id}>'
        count = 0
        embed = discord.Embed(title="Search results", colour=discord.Colour.random())

        if forbidden_word == False:
            for i in search(query=query, stop=results):
                count += 1
                embed.add_field(name=f"{count}th result", value=i, inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.description = f"{id_usr} aqui están los resultados de tu búsqueda"
            await ctx.send(embed=embed)

    @commands.command()
    async def contact(self, ctx):
        color = discord.Colour.random()
        embed = discord.Embed(title="Formas de contratar al creador del bot", colour=color)
        embed.set_author(name="MrJakeSir")
        embed.insert_field_at(index=1, name="Reddit", value="https://www.reddit.com/user/Mrjakeprro")
        embed.insert_field_at(index=2, name="Twitter", value="https://twitter.com/SitAmetDolorem")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, user: discord.User):
        try:
            
            embed = discord.Embed(title=f"foto de perfil de {user}", colour=discord.Colour.random())
        except Exception:
            user = ctx.message.author
            embed = discord.Embed(title=f"foto de perfil de {user}", colour=discord.Colour.random())
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='clear')
    async def clear(self, ctx, limit='5'):
        if str(limit) == '-a':
            limit = int(1000)
        if ctx.message.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=int(limit))
        else:
            await ctx.send("No puedes usar este comando porque no eres administrador")

def setup(bot):
    bot.add_cog(Google(bot))
