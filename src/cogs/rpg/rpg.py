# from sqlite3.dbapi2 import connect
import discord
# from discord import colour
from discord.ext import commands
import sqlite3
import asyncio

from discord.ext.commands.core import command
import colorama as c

from .rpg_manage import User

r = c.Style.RESET_ALL
g = c.Fore.LIGHTGREEN_EX
m = c.Fore.LIGHTMAGENTA_EX
re = c.Fore.LIGHTRED_EX
b = c.Fore.CYAN


class Rpg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list_data = []

    def shop_connection(self):
        print(
            f'[{g}*{r}] Iniciada conexión con la base de datos de la {g}tienda{r} {m}RPG{r}')
        connection = sqlite3.connect(
            '/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM ARMOR')

        # ~ Lista de productos de armaduras ~ #
        self.the_armors = cursor.fetchall()
        connection.commit()
        connection.close()

        # ~ Lista de productos de armas ~ #
        connection_weapons = sqlite3.connect(
            '/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor_weapons = connection_weapons.cursor()

        cursor_weapons.execute('SELECT * FROM WEAPON')
        self.the_weapons = cursor_weapons.fetchall()
        connection_weapons.commit()
        connection_weapons.close()

        # ~ Lista de productos de items ~ #

        connection_items = sqlite3.connect(
            '/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor_items = connection_items.cursor()

        cursor_items.execute('SELECT * FROM ITEM')
        self.the_items = cursor_items.fetchall()
        connection_items.commit()
        connection_items.close()

    def is_in_database(self, user):
        print(
            f'[{g}*{r}] Validando si {user} está en la {re}base de datos{r} {m}RPG{r}')
        connect = sqlite3.connect(
            '/home/lvoidi/Desktop/discord/src/database/users_data.db')
        cursor = connect.cursor()
        cursor.execute(r'SELECT * FROM USERS')
        users = cursor.fetchall()
        for usr in users:
            if usr[0] == user:
                return True
            else:
                continue
        connect.commit()
        connect.close()

    def add_user_in_database(self, id: int, user: str):
        print(
            f'[{m}*{r}] Añadiendo {g}{user}{r} a la base de datos con la id {re}{id}{r}')
        connect = sqlite3.connect(
            '/home/lvoidi/Desktop/discord/src/database/users_data.db')
        cursor = connect.cursor()
        registro = [
            (int(id), f'{user}', 50, 1, 1, 0)
        ]
        try:
            cursor.executemany(
                'INSERT INTO USERS VALUES(?,?,?,?,?,?)', registro)
            cursor.execute(f"""CREATE TABLE {user}_INV(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            PRODUCT VARCHAR(50),
                            USAGE CHAR,
                            PRICE INTEGER,
                            REP INTEGER)
                            """)
            ALL = [
                # Armaduras
                ('Armadura no tan dura', "T", 0, 1),
                ('Armadura de bronce', 'F', 85, 0),
                ('Armadura sombria', "F", 105, 0),
                ('Armadura de plomo', 'F', 135, 0),
                ('Armadura de platino', 'F', 146, 0),
                ('Armadura de elixir', 'F', 186, 0),
                ('Armadura del dragón', 'F', 200, 0),

                # Armas
                ('Palo', 'T', 0, 1),
                ('Espada de madera', 'F', 20, 0),
                ('Espada de piedra', 'F', 30, 0),
                ('Espada de bronce', 'F', 40, 0),
                ('Espada de hierro', 'F', 70, 0),
                ('Espada de acero inoxidable', 'F', 85, 0),
                ('Espada encantada', 'F', 100, 0),
                ('Espada del exilio', 'F', 120, 0),
                ('Espada del oblivion', 'F', 70, 0),


                # Items


                ('Poción de curación', 'F', 20, 0),
                ('Poción de fuerza', 'F', 40, 0),
                ('Poción de resistencia', 'F', 40, 0)


            ]
            cursor.executemany(
                f"INSERT INTO {user}_INV VALUES(NULL, ?, ?, ?, ?)", ALL)
        except Exception as e:
            print("Excepcion found:", type(e), e)
            return False
        connect.commit()
        connect.close()

    @commands.command()
    async def shop(self, ctx):
        print(f'[{g}*{r}] Iniciando {re}conexión{r} con {re}tienda{r} {m}RPG{r}')
        self.shop_connection()
        the_armors = self.the_armors
        the_weapons = self.the_weapons
        the_items = self.the_items
        page = 0
        embed_color = discord.Color.gold()

        # ~ Embed de la pagina de armaduras ~ #
        embed_armor = discord.Embed(
            title="Tienda de armaduras para RPG!",
            description="""Puedes ejecutar el comando `py!buy (ID)` para **comprar una armadura!**
            reacciona con ⬅/➡ para navegar entre las diferentes páginas, y ❌ **para salir**.
            """,
            colour=embed_color
        )
        embed_armor.set_footer(text='Página 1', icon_url=ctx.author.avatar_url)
        embed_armor.set_thumbnail(
            url='https://i.gifer.com/origin/4c/4cf9c4b3173ec5a3ba877daed7c3309f_w200.gif')
        print(f'[{g}*{r}] Creado {re}embed{r} de las {g}armaduras{r} {m}RPG{r}')

        # ~ Embed de la página de armas ~ #
        embed_weapons = discord.Embed(
            title="Tienda de armas para RPG!",
            description="""Puedes ejecutar el comando `py!buy (ID)` para **comprar un arma!**
            reacciona con ⬅/➡ para navegar entre las diferentes páginas, y ❌ **para salir**""",
            colour=embed_color
        )

        embed_weapons.set_footer(
            text='Página 2', icon_url=ctx.author.avatar_url)
        embed_weapons.set_thumbnail(
            url='http://1.bp.blogspot.com/-Dz1WMgUXPSM/VUpYrBNDcNI/AAAAAAAACdY/R9JLNYs8fHo/s1600/flame_lancer_entity_000_hit.gif')

        print(f'[{g}*{r}] Creado el {re}embed{r} de las {re}armas{r} {m}RPG{r}')

        # ~ Embed de la página de items ~ #
        embed_items = discord.Embed(
            title="Tienda de items para RPG!",
            description="""Puedes ejecutar el comando `py!buy (ID)` para **comprar un item!**
            reacciona con ⬅/➡ para navegar entre las diferentes páginas, y ❌ **para salir**""",
            colour=embed_color
        )
        embed_items.set_footer(text='Página 3', icon_url=ctx.author.avatar_url)
        embed_items.set_thumbnail(
            url='https://i.pinimg.com/originals/4e/b7/bd/4eb7bda23bf456a53fd6ba84c1048ba6.gif')

        print(f'[{g}*{r}] Creado {re}embed{r} de los {b}items{r} {m}RPG{r}')

        list_emojis = [
            '❌',
            '⬅',
            '➡',
        ]

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in list_emojis

        # ~ embed de las armaduras ~ #

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
        print(
            f'[{g}*{r}] Añadiendo los {re}campos del embed{r} de {re}armors{r} {m}RPG{r}')
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
        print(
            f'[{g}*{r}] Añadiendo los {re}campos del embed{r} de {g}weapons{r} {m}RPG{r}')
        embed_items.add_field(
            name='`Sección de items`',
            value='·',
            inline=False
        )

        for item in the_items:
            embed_items.add_field(
                name=item[1],
                value=f"""
                ```{item[2]}```
                **ID**: `{item[0]}`
                **precio**: `{item[3]}`
                **nivel necesario**:`{item[4]}`
                **stage necesario**:`{item[5]}`
                """,
                inline=True
            )

        print(
            f'[{g}*{r}] Añadiendo los {re}campos del embed{r} de {b}items{r} {m}RPG{r}')
        message = await ctx.send(embed=embed_armor)
        for emoji in list_emojis:
            await message.add_reaction(emoji)

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=15.0, check=check)
                print(f'[{m}*{r}] Se ha reaccionado con {b}{reaction.emoji}{r}')
                if reaction.emoji == '❌':
                    await ctx.send("Ya no se aceptarán mas reacciones")
                    await message.remove_reaction(reaction.emoji)
                    return
                elif reaction.emoji == '⬅':
                    if page == 0:
                        continue
                    elif page == 1:
                        await message.edit(embed=embed_armor)
                        page -= 1
                    elif page == 2:
                        await message.edit(embed=embed_weapons)
                        page -= 1

                elif reaction.emoji == '➡':
                    if page == 1:
                        page += 1
                        await message.edit(embed=embed_items)

                    else:
                        page += 1
                        await message.edit(embed=embed_weapons)

            except asyncio.TimeoutError:
                await ctx.send("Se ha pasado el tiempo para reaccionar")
                return

    @commands.command()
    async def register(self, ctx, username):

        if self.is_in_database(ctx.message.author.id):
            await ctx.send("Ese nombre de usuario ya está registrado")
            return
        else:
            useradd = self.add_user_in_database(
                id=ctx.message.author.id, user=username)
            if useradd == False:
                await ctx.send("Ya estás registrado!")
                return
            embed = discord.Embed(
                title="Registro completado",
                description=f"Te has registrado en nuestra base de datos como {username} con la id de {ctx.message.author.id}",
                colour=discord.Color.dark_gold(),
            )
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            print(
                f'[{g}*{r}] {b}{ctx.message.author}{r} se ha registrado como {re}{username}{r}')
            await ctx.send(embed=embed)

    @commands.command()
    async def profile(self, ctx):
        usr = User()
        profile = usr.get_by(id=ctx.message.author.id)

        if self.is_in_database(ctx.message.author.id) == False:

            embed = discord.Embed(
                title=f'No se ha encontrado tu perfil, {ctx.message.author}, prueba py!register (nombre de usuario) para registrarte',
                colour=discord.Color.red()
            )
            await ctx.send(embed=embed)

        the_profile = discord.Embed(
            title=f'Perfil de {ctx.message.author}',
            description=f'{ctx.message.author.mention}',
            colour=discord.Color.gold()
        )
        the_profile.set_thumbnail(url='https://i.gifer.com/LWEI.gif')
        the_profile.set_footer(text=ctx.message.author,
                               icon_url=ctx.message.author.avatar_url)
        the_profile.add_field(
            name=f'Id de {profile.get("username")}',
            value=f">>>  **{profile.get('id')}**",
            inline=True)

        the_profile.add_field(
            name=f'Nombre de usuario',
            value=f'>>> **{profile.get("username")}**',
            inline=True
            )

        the_profile.add_field(
            name=f'Dinero en **doblones**',
            value=f'>>> **{profile.get("balance")}Ðþ**',
            inline=True
            )

        the_profile.add_field(
            name=f'Nivel de {profile.get("username")}',
            value=f'>>> **{profile.get("nivel")}**',
            inline=True
            )


        the_profile.add_field(
            name=f'Fase en la que está **{profile.get("username")}**',
            value=f'>>> **{profile.get("fase")}**',
            inline=True
            )

        the_profile.add_field(
            name=f'**XP actual de {profile.get("username")}**',
            value=f'>>> **{profile.get("xp")}**',
            inline=True
            )

        the_profile.set_image(url='http://38.media.tumblr.com/b22ce060141beace4075fe1f0e3c7396/tumblr_ne9l9iyNNI1u2uscho1_250.gif')
        print(f'[{g}*{r}] {b}{ctx.message.author}{r} está viendo su perfil')
        await ctx.send(embed=the_profile)


def setup(bot):
    bot.add_cog(Rpg(bot))
