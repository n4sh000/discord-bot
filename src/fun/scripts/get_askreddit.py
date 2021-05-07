from urllib import request
import re
import random
class AskReddit:
     def __init__(self):
          self.ask_reddit_sections = {
               1: "https://www.reddit.com/r/AskReddit",
               2: "https://www.reddit.com/r/AskReddit/new/",
               3: "https://www.reddit.com/r/AskReddit/top/",
               4: "https://www.reddit.com/r/AskReddit/top/?t=all",
               5: "https://www.reddit.com/r/AskReddit/top/?t=month",
               6: "https://www.reddit.com/r/AskReddit/top/?t=year",
               7: "https://www.reddit.com/r/AskReddit/top/?t=week",
               8: "https://www.reddit.com/r/AskReddit/top/?t=day",
               
          }
          self.gamble_subs = self.ask_reddit_sections.get(random.randint(1,8))
          self.get_post()
     def get_post(self):
          posts_link = []
          subreddit = self.gamble_subs
          # This section opens the gambled url
          url = request.Request(f'{subreddit}', headers={'User-Agent': 'Mozilla/5.0'})
          html_section = request.urlopen(url)
          
          posts_links = re.findall(r'/r/AskReddit/comments/[a-zA-Z1-9]*/[a-zA-Z1-9_*]*/', html_section.read().decode())
          
          select_random_post = posts_links[random.randint(0,len(posts_link))]
          print(f'post selected: https://reddit.com{select_random_post}')
          # Second request for post
          url_post = request.Request(f'https://reddit.com{select_random_post}', headers={'User-Agent': 'Mozilla/5.0'})
          html_post = request.urlopen(url_post)
          
          self.post_title = re.findall(r'<h1 class="_eYtD2XCVieq6emjKBH3m">([a-zA-Z1-9.* *]*)', html_post.read().decode())
          print(self.post_title[0])
          
app = AskReddit()