import discord
import os
from discord.ext import commands

# Fun commands

from time import sleep

# Commands
startup_extensions = [
    "fun.repeat",
    "fun.random_cap",
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
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


# If bot's connected...
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run("ODMzMTQ2NTI0OTI1NTU4Nzg0.YHuGKg.lEUp6mT115CoxKLMov3vZ_RIA6k")