import os
from discord.ext import commands
from discord.ext.commands.core import command
from .rpg_manage import Rpg
import sys
import discord
class Rpg_2(commands.Cog):
     def __init__(self, bot):
          self.rpg = Rpg()
          self.bot = bot
          self.GIFS = {
               "ARMOR" : {
                    1:'https://lh3.googleusercontent.com/proxy/OlC4R60aeE7hzdpX_nnUfVr9GhjKrGuqdqurMGd6WxKwQSPO00HdueXiiXivHdwfcNO9_ImI9GUYfv12IVuSy_p4inmQgTcd',
                    2:'http://pixeljoint.com/files/icons/full/2013050205__pixelart.gif',
                    3:'https://i.pinimg.com/originals/a3/5c/e8/a35ce8c6039b3a1a23aca7706e07c6fa.gif',
                    4:'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6540f018-c5a7-40dc-b8d0-d879c2b8ba81/dbddffx-f923c95a-0dce-4e74-8e38-d6685df5ff4e.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjU0MGYwMTgtYzVhNy00MGRjLWI4ZDAtZDg3OWMyYjhiYTgxXC9kYmRkZmZ4LWY5MjNjOTVhLTBkY2UtNGU3NC04ZTM4LWQ2Njg1ZGY1ZmY0ZS5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.PGz7tqtF_Ne-a130ylHjaPlafjanZZoyD9EqsaHKc28',
                    5:'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/6540f018-c5a7-40dc-b8d0-d879c2b8ba81/dbfg614-f921e465-2b1a-4ce3-9fbf-fe116cf20067.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzY1NDBmMDE4LWM1YTctNDBkYy1iOGQwLWQ4NzljMmI4YmE4MVwvZGJmZzYxNC1mOTIxZTQ2NS0yYjFhLTRjZTMtOWZiZi1mZTExNmNmMjAwNjcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.5N9JLhcLlDRe4YFHDa1A6BIYYEm9W59NSU_jRqtI_pM',
                    6:'https://64.media.tumblr.com/2be0e1a591f35dc0fde50b155c9017a0/tumblr_o47dg7Niqw1tgzy56o1_r2_400.gif',
                    7:'https://i.pinimg.com/originals/a6/b0/40/a6b0408c077c24587b2d4a8a2b51c6c4.gif',
               },
               "WEAPON" : {
                    1:'https://cdnb.artstation.com/p/assets/images/images/015/039/973/original/ray-manis-stick-mossanimated2.gif?1546827858',
                    2:'https://lh3.googleusercontent.com/proxy/6tW4Ye4yLzmm1Z6FCR2r-OlxsYPyiliUZnVPxHkE_rnS_LdtDuy2EujpXoCLnx1oe28DaJjc1ARTza1EEvnKBFMG9losVfsN',
                    3:'https://cdnb.artstation.com/p/assets/images/images/021/270/157/original/volkan-sozbir-ezgif-3-ae954d000c2e.gif?1571051499',
                    4:'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7c95ec7b-5a4f-4aef-93df-78fad9ba2505/ddh4slr-82c38d93-e1a3-4414-9128-d8613670dc97.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzdjOTVlYzdiLTVhNGYtNGFlZi05M2RmLTc4ZmFkOWJhMjUwNVwvZGRoNHNsci04MmMzOGQ5My1lMWEzLTQ0MTQtOTEyOC1kODYxMzY3MGRjOTcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.ElJVJDFOgnKjHAN3UP_yjOqxk1s3lWSyPtIo7tseO30',
                    5:'https://i.pinimg.com/originals/85/b2/45/85b24564700f352aa1b3b0174e38e54c.gif',
                    6:'https://i.pinimg.com/originals/2b/66/9f/2b669f8654f5819a6abfa174aa195fee.gif',
                    7:'https://i.pinimg.com/originals/c1/28/e7/c128e75a11ca7448d4225a5cbf04c5eb.gif',
                    8:'https://i.imgur.com/VUBjdSz.gif',
                    9:'https://i.pinimg.com/originals/31/7b/b9/317bb95178e5117de9636cfdc3b42660.png',
               },
               "ITEM" : {
                    1:'https://64.media.tumblr.com/c5bf15b0cf7029e3a633de6839efa49b/tumblr_ps8cwdR3f41y6ld9uo1_500.gifv',
                    2:'https://cdna.artstation.com/p/assets/images/images/022/759/442/original/korgun-akgun-big-health.gif?1576595180',
                    3:'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/baac3c5a-79a5-4d51-bfd3-a212adde27a6/dcm6ki9-79d63ba0-c347-4be8-b1cb-0e283f029627.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2JhYWMzYzVhLTc5YTUtNGQ1MS1iZmQzLWEyMTJhZGRlMjdhNlwvZGNtNmtpOS03OWQ2M2JhMC1jMzQ3LTRiZTgtYjFjYi0wZTI4M2YwMjk2MjcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.xFO9sBebtJV8VLJnlHdsDYjo-JPkgyOMG5GOGHdbrzY',
               },
               
               
          }
     
     @commands.command()
     async def buy(self, ctx, id_product: int, section: str):
          try:
               bought_item = self.rpg.shop_item(id=id_product, section=section)
               gif_1 = self.GIFS.get(section.upper())
               print(gif_1)
               gif_new = gif_1.get(id_product)
               user = self.rpg.get_user_stats(
                    userid=ctx.message.author.id
               )
               
               if self.rpg.is_valid(user_id=ctx.message.author.id):
                    self.rpg.inventory_insert(
                              username=user[0],
                              item=self.rpg.name
                         )
               else:
                    print("Id: ", ctx.message.author.id)
                    await ctx.send("Al parecer no eres valido")
                    return
               embed = discord.Embed(
                    color=discord.Color.gold()
               )
               print(gif_new)
               embed.set_image(url=gif_new)
               embed.title = "Has comprado exitosamente el item: {}".format(self.rpg.name)

               await ctx.send(embed = embed)
          except Exception as e:
               exc_type, exc_obj, exc_tb = sys.exc_info()
               fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
               print(exc_type, fname, exc_tb.tb_lineno)
               print(f"JODEEER UN ERRORRRRRR: {type(e).__name__}:{e}")
     
     @commands.command()
     async def inventory(self, ctx):
          try:
               lol = self.rpg.get_inventory(usr=ctx.message.author.id)

               embed = discord.Embed(
                    color=discord.Color.random()
               )
               embed.title = '¡Bienvenido a tu inventario, **aventurero**!'
               embed.description = "`Escribe **py!use (item)** para poder usarlo!`"
               
               embed.add_field(
                    name=lol[0],
                    value=f'`{lol[1]}`'
               )
               
               await ctx.send(embed = embed)
          except Exception as e:
               print(type(e).__name__, e)
          
     
def setup(bot):
     bot.add_cog(Rpg_2(bot))