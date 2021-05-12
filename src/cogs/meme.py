import random
import re
import urllib
from urllib import request

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
            11: "theydidthemath",
            12: "Minecrafthmmm",
            13: "MAAU",
            14: "facepalm",
            15: "cursedcomments",
            16: "comedyheaven",
            17: "okbuddyretard",
            18: "orslokx",
            19: "cursedimages",
            20: "hmmm",
            21: "ihavereddit",
            22: "woooosh",
            23: "DylanteroYT",
            24: "dankmemes",
            25: "blursedimages",
            26: "starterpacks",
            27: "theydidthemath",
            28: "Minecrafthmmm",
            29: "MAAU",
            30: "facepalm",
            31: "cursedcomments",
            32: "comedyheaven"
        }
        self.post_image = []

    def get_subreddit_post_image(self):
        # This select a random subreddit from the dictionary
        self.get_sub = self.subreddits.get(random.randint(1, 32))

        # This gets the subreddit full html content
        req = urllib.request.Request('https://www.reddit.com/r/{}/'.format(self.get_sub),
                                     headers={'User-Agent': 'Mozilla/5.0'})
        html_content = request.urlopen(req)

        # This gets all the posts in the subreddit
        search_results = re.findall(rf'/r/{self.get_sub}/comments/[\w]+/[\w]+/', html_content.read().decode())

        # This selects a random post from the returned list
        self.post = search_results[random.randint(2, 10)]

        # Gets the post html content
        req2 = urllib.request.Request(f'https://www.reddit.com{self.post}', headers={'User-Agent': 'Mozilla/5.0'})
        post_content = request.urlopen(req2)

        # Gets the post image
        self.post_image = re.findall(r'i.redd.it/[\w]+\.[\w]{3}', post_content.read().decode())
        self.got_it = True
        print(self.post_image)

    def if_exception(self):
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

    @commands.command()
    async def meme(self, ctx):
        await ctx.send("Esto puede tomar un poco de tiempo...")
        self.if_exception()

        embed = discord.Embed(colour=discord.Colour.random())
        try:
            embed.set_image(url=f"https://{self.post_image[0]}")
        except Exception:
            command_state = False
            while command_state == False:
                try:
                    self.if_exception()
                    try:
                        embed.set_image(url=f"https://{self.post_image[0]}")
                        command_state = True
                    except (IndexError, Exception):
                        continue
                except Exception:
                    continue
        embed.add_field(name='post', value=f'https://www.reddit.com{self.post}')
        embed.set_footer(text=f"Encontrado en el subreddit de {self.get_sub}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meme(bot))
