from discord.ext import commands
import discord

class Server(commands.Cog):
     def __init__(self, bot: commands.Bot):
          self.bot = bot
          
     
     @commands.command()
     async def publish(self, ctx: commands.Context, *, url: str):
          try:
               sm_list = []
               embed = discord.Embed(
                    color=discord.Color.random()
               )
               
               def check(m: discord.Message):
                    return m.channel == ctx.channel and m.author == ctx.message.author
               
               await ctx.send("Manda un mensaje con el título del embed, no hace falta ningun prefijo")
               
               titl = await self.bot.wait_for('message', check=check)
               
               await ctx.send("Ahora manda la descripcion del mensaje, no hace falta ningun prefijo")
               
               desc = await self.bot.wait_for('message', check=check)

               embed.description = desc.content        
               
               
               
               
               
               embed.title = titl.content
               for link in url.split():
                    if link.endswith(".png") or link.endswith(".jpg") or link.endswith('.gif'):
                         embed.set_image(url=link)
                         
                    elif link.startswith("https://twitter.com") or link.startswith("http://twitter.com") or link.startswith("twitter.com"):
                         emoji = self.bot.get_emoji(id=844987841917616218)
                         embed.add_field(
                              name=f"{emoji} -> Twitter",
                              value=f"{link}"
                         )
                         
                         
                         sm_list.append(emoji)
                    elif link.startswith("https://instagram.com") or link.startswith("http://instagram.com") or link.startswith("instagram.com"):
                         emoji = self.bot.get_emoji(id=844987843125837854)
                         embed.add_field(
                              name=f"{emoji} -> Instagram",
                              value=f"{link}"
                         )
                         emoji = discord.utils.get(self.bot.get_all_emojis(), "instagram")
                         sm_list.append(emoji)
                         
                    elif link.startswith("https://github.com") or link.startswith("http://github.com") or link.startswith("github.com"):
                         emoji = self.bot.get_emoji(id=844987842879160370)
                         embed.add_field(
                              name=f"{emoji}  -> Github",
                              value=f"{link}"
                         )
                         
                         sm_list.append(emoji)
                    
                    elif link.startswith("https://twitch.tv") or link.startswith("http://twitch.tv") or link.startswith("twitch.tv"):
                         emoji = self.bot.get_emoji(id=844987841318486057)
                         embed.add_field(
                              name=f"{emoji}   -> Twitch",
                              value=f"{link}"
                         )

                         sm_list.append(emoji)

                    elif link.startswith("https://youtube.com") or link.startswith("http://youtube.com") or link.startswith("youtube.com"):
                         emoji = self.bot.get_emoji(id=844987841737523240)
                         embed.add_field(
                              name=f"{emoji}  -> Youtube",
                              value=f"{link}"
                         )
                         sm_list.append(emoji)
                    
                    else:
                         print("se bugueo pues XD")
                         embed.add_field(
                              name="Otros",
                              value=f"{link}"
                         )
               channel = self.bot.get_channel(id=844765340528934938)
               msg = await channel.send(embed = embed)
               for emoji in sm_list:
                    await msg.add_reaction(emoji)
                                           
          except Exception as e:
               print('error: ', type(e).__name, e)
          
          
     @commands.command()
     async def rules(self, ctx):
          bot = self.bot
          shitpost_chan = bot.get_channel(id=844757014085369867)
          spam_chan = bot.get_channel(id=844769531045216278)
          embed = discord.Embed(
               color=discord.Color.gold()
          )
          embed.title = f"Las reglas de **{ctx.message.guild.name}**"
          embed.description = f">>> Bienvenido a las reglas de {ctx.message.guild.name}, por favor, **tomarlas seriamente**"
          
          embed.add_field(
               name="Respeto ante todo",
               value=">>> El **no faltar el respeto**, no sentirse superior si alguien pregunta es fundamental, recordemos que **no todos nacemos sabiendo**",
               inline=False
          )
          embed.add_field(
               name="Nsfw **no permitido**",
               value=">>> El nsfw (not safe for work) no está permitido bajo ninguna circunstancia",
               inline=False
          )
          embed.add_field(
               name="Tags innecesarios",
               value=">>> Por favor, **evita hacer tags inecesarios, es muy molesto**, {}".format(ctx.message.author.mention),
               inline=False
          )
          
          embed.add_field(
               name="No meterse en temas políticos **a menos que el canal lo permita**",
               value=">>> Por ejemplo, en el canal de {0.mention}, puedes poner libremente del tema que se te antoje".format(shitpost_chan),
               inline=False

          )

          embed.add_field(
               name="No hacer spam ni flood",
               value="""
               >>> Flood se refiere a la acción de mandar muchos mensajes con un texto repetidamente,
               por favor, no hacerlo o el auto mod lo detectará
               
               Y no hagan spam **a menos que sea en el canal adecuado**, el unico canal adecuado es 
               {0.mention}
               
               """.format(spam_chan),
               inline=False
          )

          embed.add_field(
               name="Y **lo mas importante:**",
               value=">>> **Disfruta del servidor! bienvenido!**",
               inline=False
          )
          
          embed.set_thumbnail(url='https://cdnb.artstation.com/p/assets/images/images/026/723/261/original/victor-villalta-libro-day2-1000video.gif?1589544255')
          embed.set_image(url='https://bbycurls.carrd.co/assets/images/gallery02/3d9db92a.gif?v06505442010061')
          
          
          await ctx.send(embed = embed)
          
          await ctx.message.delete()
     
     
def setup(bot):
     bot.add_cog(Server(bot))