import discord
from discord.ext import commands
import random

class RandomCap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.caps= {
            1: "Tirar tus productos que se experimentaron con animales, ayudará mucho al planeta! :billed_cap: ",
            2: "Cualquier consola es mejor que un pc, es lógico... :billed_cap: ",
            3: "El creador del bot tiene muchos amigos! :billed_cap: ",
            4: "Que juegazo fortnite, tiene una comunidad super unida! :billed_cap: ",
            5: "Buaaa que juegazo warzone, es un juego muy divertido! :billed_cap: ",
            6: "System 32 es una carpeta con archivos importantes :billed_cap: ",
            7: "Friday Night Funking es un juegazo :billed_cap: ",
            8: "Im not imposter from amon gus :billed_cap: https://tenor.com/view/saturnius-trollge-troll-face-troll-happy-gif-19771840",
            9: "Los jugadores de Osu! No son pedófilos :billed_cap:",
            10: "No soy un señor de 40 años :billed_cap:",
            11: "Los shitposter y panafrescos si dan risa :billed_cap:",
            12: "Los otakus si tienen amigos y amor paternal :billed_cap:"
        }

    @commands.command()
    async def cap(self, ctx):
        await ctx.send(self.caps.get(random.randint(1,12)))
        
def setup(bot):
    bot.add_cog(RandomCap(bot))
