import discord
from discord.ext import commands
from config import TOKEN

# Commands extensions
startup_extensions = [
    # Fun commands
    "fun.repeat",
    "fun.random_cap",
    "fun.helloworld",
    "fun.dumb",
    "fun.meme",
    # Useful commands
    "useful.google",
]

# Bot instance
bot = commands.Bot(command_prefix='py!', description='Beta version of this bot')

@bot.event
async def on_ready():
    game = discord.Game("with python")
    await bot.change_presence(activity=game)
    
    print('Exitosamente iniciado con el nombre de usuario {0.user}'.format(bot))


@bot.command()
async def load(extension_name : str):
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
async def unload(extension_name : str):
    """[Unloading extension]
    Unloads the specified extension
    Args:
        extension_name (str): [Extension to unload]
    """
    
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)