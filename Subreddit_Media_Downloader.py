# Title: Python - Download media from Subreddit
# Description: Download Media Posted to a Subreddit
# More info: https://alteredadmin.github.io/posts/python-download-media-from-subreddit/
# =====================================================
# Name: Altered Admin
# Website: https://alteredadmin.github.io/
# If you found this helpful Please consider:
# Buymeacoffee: http://buymeacoffee.com/alteredadmin
# BTC: bc1qhkw7kv9dtdk8xwvetreya2evjqtxn06cghyxt7
# LTC: ltc1q2mrh9s8sgmh8h5jtra3gqxuhvy04vuagpm3dk9
# ETH: 0xef053b0d936746Df00C9CCe0454b7b8afb1497ac


import praw
import datetime
import os.path
import subprocess

# Make sure to Fill in below API info
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='my user agent')

now = datetime.datetime.now()

subs = [""]

# here can you set what domains you want to download from.
# This list is short because there is not many external domains that get posted to reddit
imgs = ('https://i.redd.it', 'https://i.imgur.com')
vids = ('https://gfycat.com')

wd = os.path.join(os.environ.get("HOME"), "Downloads", "stuffs", '')

print()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
print()


def img_getter(all):
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed or already exists" % path)
    else:
        print("Successfully created the directory %s" % path)
    for post in all:
        print(post.url)
        if str(post.url).startswith(imgs):
            try:
                subprocess.run(["wget", "-nc", "-P", path, post.url])
            except:
                break
        elif str(post.url).startswith(vids):
            print("Found a Vid")
            # subprocess.run(["youtube-dl", "-i", "-o", ytdl, post.url])
            subprocess.run(["youtube-dl", "-i", "--playlist-end", "1", "-o", ytdl, post.url])

for sub in subs:
    path = os.path.join(wd, sub, '')
    ytdl = path + "%(title)s-%(id)s.%(ext)s"
    print(sub)
    print('Getting new')
    img_getter(reddit.subreddit(sub).hot(limit=None))
    img_getter(reddit.subreddit(sub).new(limit=None))
    img_getter(reddit.subreddit(sub).top(limit=None))
    img_getter(reddit.subreddit(sub).controversial(limit=None))
