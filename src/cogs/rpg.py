import discord
from discord.ext import commands
import sqlite3
import asyncio

from discord.ext.commands.core import command
class Rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list_data = []
    
    def shop_connection(self):
        connection = sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ARMOR')
        

        # ~ Lista de productos de armaduras ~ #
        self.the_armors = cursor.fetchall()
        connection.commit()
        connection.close()
        
        # ~ Lista de productos de armas ~ #
        connection_weapons = sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor_weapons = connection_weapons.cursor()
        
        cursor_weapons.execute('SELECT * FROM WEAPON')
        self.the_weapons = cursor_weapons.fetchall()
        connection_weapons.commit()
        connection_weapons.close()


        # ~ Lista de productos de items ~ #
        """
        connection_items = sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor_items = connection_items.cursor()
        
        cursor_items.execute('SELECT * FROM SHOP_ITEMS')
        self.the_items = cursor_items.fetchall()
        connection_items.commit()
        connection_items.close()
        """
    @commands.command()
    async def rhunt(self, ctx):
        pass
    @commands.command()
    async def rfight(self, ctx, user):
        pass



    @commands.command()
    async def rshop(self, ctx):
        self.shop_connection()
        the_armors = self.the_armors
        the_weapons = self.the_weapons
        # the_items = self.the_items
        
        embed_color = discord.Color.gold()
        
        # ~ Embed de la pagina de armaduras ~ #
        embed_armor = discord.Embed(
            title="Tienda de armaduras para RPG!",
            description="""Puedes ejecutar el comando `py!buy (ID)` para **comprar una armadura!**
            reacciona con ⬅/➡ para navegar entre las diferentes páginas, y ❌ **para salir**.
            """,
            colour=embed_color
        )
        embed_armor.set_footer(text='Página Armaduras', icon_url=ctx.author.avatar_url)
        embed_armor.set_thumbnail(url='https://i.gifer.com/origin/4c/4cf9c4b3173ec5a3ba877daed7c3309f_w200.gif')
        
        # ~ Embed de la página de armas ~ #
        embed_weapons = discord.Embed(
            title="Tienda de armas para RPG!",
            description="""Puedes ejecutar el comando `py!buy (ID)` para **comprar un arma!**
            reacciona con ⬅/➡ para navegar entre las diferentes páginas, y ❌ **para salir**""",
            colour=embed_color
        )
        embed_weapons.set_footer(text='Página 2', icon_url=ctx.author.avatar_url)
        embed_weapons.set_thumbnail(url='http://1.bp.blogspot.com/-Dz1WMgUXPSM/VUpYrBNDcNI/AAAAAAAACdY/R9JLNYs8fHo/s1600/flame_lancer_entity_000_hit.gif')
        
        list_emojis = [
            '❌',
            '⬅',
            '➡',
        ]
        
        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in list_emojis
        
        # ~ embed de las armaduras ~ #
        count = 0
        embed_armor.add_field(
            name='`Sección de armaduras`',
            value='·',
            inline=False
        )
        
        for armor in the_armors:
            embed_armor.add_field(
                name=armor[1],
                value=f"""
                ```{armor[2]}```
                **ID**: `{armor[0]}`
                **precio**: `{armor[3]}`
                **nivel necesario**:`{armor[4]}`
                **stage necesario**:`{armor[5]}`
                **puntos de defensa**:`{armor[6]}`
                """,
                inline=True
            )
        
        embed_weapons.add_field(
            name='`Sección de armas`',
            value='·',
            inline=False
        )
        
        for weapon in the_weapons:
            embed_weapons.add_field(
                name=weapon[1],
                value=f"""
                ```{weapon[2]}```
                **ID**: `{weapon[0]}`
                **precio**: `{weapon[3]}`
                **nivel necesario**:`{weapon[4]}`
                **stage necesario**:`{weapon[5]}`
                **puntos de ataque**:`{weapon[6]}`
                """,
                inline=True
            )
        
        message = await ctx.send(embed = embed_armor)
        for emoji in list_emojis:
            await message.add_reaction(emoji)
            
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=15.0, check=check)
                if reaction.emoji == '❌':
                    await ctx.send("Ya no se aceptarán mas reacciones")
                    await message.remove_reaction(reaction.emoji)
                    return
                elif reaction.emoji == '⬅':
                    if page == 0:
                        continue
                    elif page == 1:
                        await message.edit(embed = embed_armor)
                        page -= 1
                elif reaction.emoji == '➡':
                    page = 1
                    await message.edit(embed = embed_weapons)
                    
            except asyncio.TimeoutError:
                await ctx.send("Se ha pasado el tiempo para reaccionar")
                return
                
            
        
        
        
        
        
    @commands.command()
    async def revent(self, ctx):
        pass
    
    @commands.command()
    async def rstage(self, ctx):
        pass



def setup(bot):
    bot.add_cog(Rpg(bot))