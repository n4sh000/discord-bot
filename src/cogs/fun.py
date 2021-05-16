import random
from time import sleep
from discord.ext import commands
from string import digits as digits_string
import string
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.all = ''
        self.count = 0
        self.sentences = ["no se, nunca fui a la escuela",
                          "no soy lo suficientemente avanzado para responder",
                          "creo que me falta un poquito de calle para responder esto",
                          "quiero que mi creador me haga mas inteligente pero el man es tonto",
                          "algun dia sumaré como lo hace mi dios willyrex"]
        self.af = ["suponiendo que es igual al diametro de una papa", 
                   "es igual a la raiz cuadrada del diametro del sol",
                   "insulta minorias por twitter",
                   "trabaja como motociclista",
                   "su velocidad es de 200 kmph"]
        self.caps = {
            1: "Tirar tus productos que se experimentaron con animales, ayudará mucho al planeta! :billed_cap: ",
            2: "Cualquier consola es mejor que un pc, es lógico... :billed_cap: ",
            3: "El creador del bot tiene muchos amigos! :billed_cap: ",
            4: "Que juegazo fortnite, tiene una comunidad super unida! :billed_cap: ",
            5: "Buaaa que juegazo warzone, es un juego muy divertido! :billed_cap: ",
            6: "System 32 es una carpeta con archivos importantes :billed_cap: ",
            7: "Friday Night Funkin es un juegazo :billed_cap: ",
            8: "Im not imposter from amon gus :billed_cap: https://tenor.com/view/saturnius-trollge-troll-face-troll-happy-gif-19771840",
            9: "Los jugadores de Osu! No son pedófilos :billed_cap:",
            10: "No soy un señor de 40 años :billed_cap:",
            11: "Los shitposter y panafrescos si dan risa :billed_cap:",
            12: "Los otakus si tienen amigos y amor paternal :billed_cap:",
            13: "El socialismo es el mejor sistema económico :billed_cap:",
            14: "Con el comunismo el mundo funcionaría mejor :billed_cap:",
            15: "Marx tuvo ideas muy buenas :billed_cap:",
            16: "El feminismo ha hecho mucho por las mujeres :billed_cap:",
            17: "BLM fue un buen movimiento :billed_cap:"
        }

    @commands.command()
    async def dumb(self, ctx, *, message: str):
        await ctx.message.delete()
        for letter in message:
            try:
                if self.count % 2 is 1:
                    if letter not in string.ascii_letters or letter not in string.ascii_lowercase or letter not in string.ascii_uppercase:
                        self.all += letter
                        
                    
                    self.all += letter.upper()
                    
                else:
                    self.all += letter.lower()

                self.count += 1
            except Exception as e:
                await ctx.send("Algo ha ido mal compa, aprende a usar el bot")
                print(e)
                break

        await ctx.send(self.all)
        self.all = ''
        self.count = 0

    @commands.command()
    async def cap(self, ctx):
        await ctx.send(self.caps.get(random.randint(1, 17)))

        
        
    @commands.command()
    async def say(self, ctx, *, message):

        id_usr = f'<@{ctx.author.id}>'
        """[repeat]

        Args:
        ctx ([discord]): [contexto]
        message ([str]): [mensaje a repetir]
        """
        self.message = message
        if "im stupid" in self.message or self.message is "im stupid":
            self.stupid = "yeah, i also think you are stupid"
            await ctx.send(self.stupid)

        elif "im gay" in self.message or self.message is "im gay":
            self.gay = "yeah, i also think you are gay"
            await ctx.send(self.gay)

        elif "nigga" in self.message or self.message is "nigga":
            await ctx.send("AYOOOOOO, exposed bro :face_with_raised_eyebrow: :camera_with_flash: {}".format(id_usr))
        else:
            await ctx.message.delete()
            await ctx.send(self.message)

 
    
    


def setup(bot):
    bot.add_cog(Fun(bot))
