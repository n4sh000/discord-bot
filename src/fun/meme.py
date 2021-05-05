from urllib import parse, request
import re
import urllib
import random
# Discord
import discord
from discord.ext import commands

class Meme(commands.Cog):
     """Searchs for memes in 4 different
     subreddits
     """
     def __init__(self, bot):
          self.bot = bot
          self.subreddits = {
               1: "okbuddyretard",
               2: "orslokx",
               3: "cursedimages",
               4: "hmmm",
               5: "ihavereddit",
               6: "woooosh",
               7: "DylanteroYT",
               8: "dankmemes",
               9: "blursedimages",
               10: "starterpacks",
          }
          self.post_image = []
     def get_subreddit_post_image(self):
          # This select a random subreddit from the dictionary
          self.get_sub = self.subreddits.get(random.randint(1,10))

          # This gets the subreddit full html content
          req = urllib.request.Request('https://www.reddit.com/r/{}/'.format(self.get_sub), headers={'User-Agent': 'Mozilla/5.0'})
          html_content = request.urlopen(req)
          
          # This gets all the posts in the subreddit
          search_results = re.findall(rf'/r/{self.get_sub}/comments/[a-zA-Z1-9]*/[a-zA-Z1-9_*]*/', html_content.read().decode())
          
          # This selects a random post from the returned list
          self.post = search_results[random.randint(2, 10)]
          
          # Gets the post html content
          req2 = urllib.request.Request(f'https://www.reddit.com{self.post}', headers={'User-Agent': 'Mozilla/5.0'})
          post_content = request.urlopen(req2)
          
          # Gets the post image
          self.post_image = re.findall(r'i.redd.it/[a-zA-Z1-9]*.[jpgpn]*', post_content.read().decode())
          self.got_it = True
          print(self.post_image)
     @commands.command()
     async def meme(self, ctx):
          await ctx.send("Esto puede tomar un poco de tiempo...")
          try:
               self.get_subreddit_post_image()
          except Exception:
               command_state = False
               while command_state == False:
                    try:
                         self.get_subreddit_post_image()
                         if self.got_it:
                              command_state = True
                         else:
                              continue
                    except Exception:
                         continue
               
          # Check if the post has an image
          if 'i.redd.it/award_' in self.post_image[0] or 'i.redd.it/t0' in self.post_image[0]:
               image_state = False
               while image_state == False:
                    try:
                         self.get_subreddit_post_image()
                         if 'i.redd.it/award_' in self.post_image[0] or 'i.redd.it/t0' in self.post_image[0]:
                              continue
                         else:
                              break
                    except Exception:
                         command_state = False
                         while command_state == False:
                              try:
                                   self.get_subreddit_post_image()
                                   if self.got_it:
                                        command_state = True
                                   else:
                                        continue
                              except Exception:
                                   continue
          # Sends the embed          
          embed = discord.Embed(title=f"Un meme que encontré en {self.get_sub} xd")
          embed.set_image(url=f"https://{self.post_image[0]}")
          embed.set_author(name=f'https://www.reddit.com{self.post}')
          await ctx.send(embed = embed)
          
def setup(bot):
     bot.add_cog(Meme(bot))