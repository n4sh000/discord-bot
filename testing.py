from urllib import parse, request
import urllib
import re
import random
def search():
     req = urllib.request.Request('https://www.reddit.com/r/okbuddyretard/', headers={'User-Agent': 'Mozilla/5.0'})
     html_content = request.urlopen(req)
     search_results = re.findall(r'/r/okbuddyretard/comments/[a-zA-Z1-9]*/[a-zA-Z1-9_*]*/', html_content.read().decode())
     
     post = search_results[random.randint(2, 15)]
     
     req2 = urllib.request.Request(f'https://www.reddit.com{post}', headers={'User-Agent': 'Mozilla/5.0'})
     post_content = request.urlopen(req2)
     post_image = re.findall(r'i.redd.it/[a-zA-Z1-9]*.[jpgpn]*', post_content.read().decode())
     post_author = re.findall(r'u/[a-zA-Z1-9]*', post_content.read().decode())
     print(post_author)
     
search()
