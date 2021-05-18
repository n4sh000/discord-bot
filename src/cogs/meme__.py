from discord.ext import commands
from discord import Embed, Color
import urllib as html
from random import choice, randint

from bs4 import BeautifulSoup

class Meme(commands.Cog):
     def __init__(self, bot):
          self.bot = bot
          self.subreddits = (
            "okbuddyretard",
            "orslokx",
            "cursedimages",
            "hmmm",
            "ihavereddit",
            "woooosh",
            "DylanteroYT",
            "dankmemes",
            "blursedimages",
            "starterpacks",
            "theydidthemath",
            "Minecrafthmmm",
            "MAAU",
            "facepalm",
            "cursedcomments",
            "comedyheaven",
        )

     def get_meme(self):
          self.subreddit = choice(self.subreddits)
          req = html.request.Request('https://www.reddit.com/r/{}/'.format(self.subreddit),
                                     headers={'User-Agent': 'Mozilla/5.0'})
          get_html = html.request.urlopen(req)
          
          soup = BeautifulSoup(get_html.read().decode(), 'html.parser')
          self.get_pfp = [image.get('src') for image in soup.find_all('img') if str(image.get('src')).startswith('https://styles.redditmedia.com')]
          self.list_images = [image.get('src') for image in soup.find_all('img') if str(image.get('src')).startswith('https://preview.redd.it/') == True and str(image.get('src')).startswith('https://preview.redd.it/award') == False]          

          return self.list_images, self.get_pfp
          
     @commands.command()
     async def meme(self, ctx):
          self.get_meme()
          embed = Embed(color=Color.random())
          embed.set_image(url=choice(self.list_images))
          embed.set_footer(text=self.subreddit, icon_url=self.get_pfp[0])
          await ctx.send(embed = embed)
def setup(bot):
     bot.add_cog(Meme(bot))
     
Meme('a')