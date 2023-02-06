# Title: Python - Download media from a reddit user
# Description: Download Media that a reddit user posted.
# More info: https://alteredadmin.github.io/posts/python-download-media-from-a-reddit-user/
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

users = [""]

# Here can you set what domains you want to download from.
# This list is short because there is not many external domains that get posted to reddit for media
for each in users:
    bio = reddit.redditor(each).subreddit["public_description"]
    print(bio)
    karma = reddit.redditor(each).link_karma
    print(karma)

imgs = ('https://i.redd.it', 'https://i.imgur.com')
vids = ('https://gfycat.com'

wd = os.path.join(os.path.expanduser("~"), "Downloads", "stuffs", "~users", '')
# all = reddit.subreddit(user).new(limit=100000)
# path = os.path.join(wd, user, '')
# ytdl = path + "%(title)s-%(id)s.%(ext)s"

print()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
print()

def img_getter(all):
    #marker
    try:
        os.mkdir(path)
    # print("Directory '% s' created" % directory)
    except OSError:
        print("Creation of the directory %s failed or already exists" % path)
    else:
        print("Successfully created the directory %s" % path)
    for post in all:
        print(post.url)
        if str(post.url).startswith(imgs):
            try:
                subprocess.run(["wget", "-nc", "-P", path, post.url])
                # wg = wget.download(post.url, path)
            except:
                break
        elif str(post.url).startswith(vids):
            print("Found a Vid")
            # subprocess.run(["youtube-dl", "-i", "-o", ytdl, post.url])
            subprocess.run(["youtube-dl", "-i", "--playlist-end", "1", "-o", ytdl, post.url])


for user in users:
    path = os.path.join(wd, user, '')
    ytdl = path + "%(title)s-%(id)s.%(ext)s"
    print('Getting new')
    img_getter(reddit.redditor(user).submissions.new(limit=None))
    # print('Getting Hot')
    img_getter(reddit.redditor(user).submissions.hot(limit=None))
    img_getter(reddit.redditor(user).top(limit=None))
