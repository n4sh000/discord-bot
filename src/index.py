import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import colorama as c
from config import TOKEN
r = c.Style.RESET_ALL
g = c.Fore.LIGHTGREEN_EX
m = c.Fore.LIGHTMAGENTA_EX
re = c.Fore.LIGHTRED_EX
# Commands extensions
startup_extensions = [
    "cogs.fun",
    "cogs.meme__",
    "cogs.useful",
    "cogs.help",
    "cogs.on_error",
    "cogs.rpg.rpg",
    "cogs.rpg.rpg_cogs",
    "servermanage"
]

# Bot instance
bot = commands.Bot(command_prefix='py!', description='Beta version of this bot', help_command=None)






@bot.event
async def on_ready():
    game = discord.Game("py!help")
    await bot.change_presence(activity=game)

    print(f'[{re}*{r}] {m}Exitosamente iniciado con el nombre de usuario {bot.user}{r}')
    
@bot.command()
async def ping(ctx):
    a = ''
    latency = str(round(bot.latency, 3))
    for letter in latency:
        if letter.startswith('0') or letter.startswith('.'):
            continue
        else:
            a += str(letter)
    await ctx.send('{0}ms'.format(a))
    a = ''
    latency = ''
"""
@bot.command()
async def xyz(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        color=discord.Color.gold()
    )
    
    embed.title = "Bienvenido a the door, el server para **programadores** y **amantes de la informatica**"
    
    embed.description = 
>>> Primero que todo, escribe el comando **__py!verify__** para que pueda asignarte ***__el rol de miembro__***

    ***Link permanente del server:*** https://discord.gg/4zDWYyrReW
    
    embed.add_field(
        name="¿Ayuda?",
        value='>>> Vete a la categoría de **code y preguntas**!'
    )
    
    embed.add_field(
        name="¿Creador del server?",
        value=">>> Ehhh dificil de decir su nombre, dejame pensar... se ha llamado desde troll hasta void, es difícil"
    )

    embed.add_field(
        name="¿Metodos de contacto?",
        value=">>> El dm del owner está abierto!"
    )
    
    embed.add_field(
        name="¿Propósito del servidor?",
        value=">>> Juntar a la mayor cantidad de amantes de la informática posibles!!"
    )
    embed.set_image(url='https://media.discordapp.net/attachments/844732529474535436/844736774324355083/thedoor.png?width=811&height=456')
    
    await ctx.send(embed = embed)
"""

@bot.command()
async def verify(ctx):
    try:
        role = ctx.message.guild.get_role(844729557029748736)
        await ctx.message.author.add_roles(role)
        m = await ctx.send(">>> **Se ha dado el rol a {}**".format(ctx.message.author.mention))
        await ctx.message.delete()
        await m.delete(delay=1)
    except Exception as e:
        exc = '{} : {}'.format(type(3).__name__, e)
        print(exc)

@bot.command()
async def load(extension_name: str):
    """[Extension loading]
    It loads every necesary command
    Args:
        extension_name (str): [Extension to load]
    """

    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.command()
async def unload(extension_name: str):
    """[Unloading extension]
    Unloads the specified extension
    Args:
        extension_name (str): [Extension to unload]
    """

    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("py!verify") == False and message.channel.id == 844732529474535436:
        msg = await message.channel.send("Por favor, escribe py!verify para verificarte y no pongas otras cosas!")
        await message.delete()
        await msg.delete(delay=3)
        await bot.process_commands(message=message)
        
    else:
        await bot.process_commands(message=message)
        return
    
    
    await bot.process_commands(message=message)

    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            print(f'[{m}*{r}] Loaded extension {g}{extension}{r}')
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

print(f'[{g}*{r}] Token del bot {re}cargado{r}')
bot.run(TOKEN)
