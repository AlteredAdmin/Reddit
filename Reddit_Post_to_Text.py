import praw
import re
import os

# Constants
CONFIG_DIR = os.path.join(os.path.expanduser("~"), "AlteredAdmin_Reddit_Tools")
CONFIG_FILE = os.path.join(CONFIG_DIR, "Reddit_Post_to_Text_Configs.txt")

def read_config():
    with open(CONFIG_FILE, "r") as f:
        lines = f.readlines()
        client_id = lines[0].strip()
        client_secret = lines[1].strip()
    return client_id, client_secret

def write_config(client_id, client_secret):
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    with open(CONFIG_FILE, "w") as f:
        f.write(client_id + "\n")
        f.write(client_secret + "\n")

def get_api_config():
    if not os.path.exists(CONFIG_FILE):
        print("Configuration file not found.")
        client_id = input("Enter your Reddit Client ID: ")
        client_secret = input("Enter your Reddit Client Secret: ")
        write_config(client_id, client_secret)
    else:
        client_id, client_secret = read_config()
    return client_id, client_secret

# Get API credentials
client_id, client_secret = get_api_config()
user_agent = 'script by /u/your_reddit_username'

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Function to sanitize the title to be used as a filename
def sanitize_title(title):
    # Remove invalid filename characters
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    # Truncate long titles
    return title[:200] if len(title) > 200 else title

# Function to get post and comments
def get_post_and_comments(url):
    post = reddit.submission(url=url)
    sanitized_title = sanitize_title(post.title)

    with open(f'{sanitized_title}.txt', 'w', encoding='utf-8') as file:
        # Write post title and content
        file.write(f'Title: {post.title}\n')
        file.write(f'Post: {post.selftext}\n\n')

        # Write all comments
        post.comments.replace_more(limit=None)  # Load all comments
        for comment in post.comments.list():
            file.write(f'Comment by {comment.author}:\n{comment.body}\n\n')

# Prompt the user for the URL of the Reddit post
post_url = input("Enter the URL of the Reddit post: ")

# Fetch and save post and comments
get_post_and_comments(post_url)
