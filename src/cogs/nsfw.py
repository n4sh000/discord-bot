from discord.ext import commands
import discord
import re
from urllib import request
import asyncio
class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  
    
#    def request_post(self, post):
#        req = request.Request('https://nhentai.net{}'.format(post),
#                                        headers={'User-Agent': 'Mozilla/5.0'})
#        html_h_post = request.urlopen(url=req)
#        get_images = re.findall()
        
    @commands.command()
    async def nhentai(self, ctx, *, query):
        if ctx.channel.is_nsfw():
            req = request.Request('https://nhentai.net/search/?q={}'.format(query),
                                        headers={'User-Agent': 'Mozilla/5.0'})
            html_h = request.urlopen(url=req)
            print("busqueda hecha")
            mangas = re.findall(r'(/g/[\d]+)', html_h.read().decode())
            print("Contenido: ", mangas)
            embed = discord.Embed(colour=discord.Colour.random())
            embed.title = 'Resultado de las busquedas de {0} en nhentai.net'.format(query)
            fir = embed.add_field(name=f"{counter}th result",
                            value=f"https://nhentai.net{mangas[0]}",
                            inline=False)

            message = await ctx.send(embed = embed)
#            state_in = True
#            state_t = ''
#            state_n = ''
#            state_b = ''
#            state_e = ''
            
#            def check_this(m):
#                state_t = 't'
#                return m.content == 't' and m.channel == ctx.channel
            
            
#            while state_t == 't':
#                msg = await client.wait_for('message', check=check_this)
#                embed.remove_field(0)
                            
        elif ctx.channel.is_nsfw() == False:
            await ctx.send("Parece que el canal no es nsfw")

def setup(bot):
    bot.add_cog(Nsfw(bot))
