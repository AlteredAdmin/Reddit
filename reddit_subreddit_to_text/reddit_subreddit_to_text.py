import praw
from praw.models import MoreComments
import datetime
import configparser
import os

# Setting up the configuration directory and file paths in the user's home directory
CONFIG_DIR = os.path.join(os.path.expanduser("~"), "AlteredAdmin_Reddit_Tools")
CONFIG_FILE = os.path.join(CONFIG_DIR, "reddit_subreddit_to_text_Configs.txt")
BASE_URL = "https://www.reddit.com"


def initialize_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as file:
            client_id = input("Enter your Reddit client_id: ")
            client_secret = input("Enter your Reddit client_secret: ")
            user_agent = input("Enter your Reddit user_agent: ")

            config = configparser.ConfigParser()
            config['Reddit'] = {
                'client_id': client_id,
                'client_secret': client_secret,
                'user_agent': user_agent
            }
            config.write(file)


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def reddit_to_text(posts, file_name, category):
    print(f"Processing {category} data for subreddit '{sub}'...")
    with open(file_name, 'a', encoding="utf-8") as file:
        for post in posts:
            post_details = f"""
            Post Title: {post.title}
            Post Time: {datetime.datetime.fromtimestamp(post.created)}
            Post karma?: {post.score}
            Post ID: {post.id}
            Post URL: {BASE_URL + post.url}  # Convert relative URL to absolute URL
            Post Shortlink: http://redd.it/{post.id}

            Self Text: {post.selftext}

            Self Comments:
            """

            file.write(post_details)

            submission = reddit.submission(url=BASE_URL + post.url)  # Convert relative URL to absolute URL
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                file.write(top_level_comment.body)
                file.write("\n")

            file.write("=" * 120)
            file.write("\n")

        print(f"{category} data for subreddit '{sub}' has been processed and saved to {file_name}.")


try:
    initialize_config()
    config = get_config()

    # Initialize the Reddit object after the configuration has been loaded
    reddit = praw.Reddit(client_id=config.get('Reddit', 'client_id'),
                         client_secret=config.get('Reddit', 'client_secret'),
                         user_agent=config.get('Reddit', 'user_agent'))

    sub = input('Enter subreddit name: ')

    reddit_to_text(reddit.subreddit(sub).new(limit=None), f'{sub}_NEW_submissions.txt', "NEW")
    reddit_to_text(reddit.subreddit(sub).hot(limit=None), f'{sub}_HOT_submissions.txt', "HOT")

except praw.exceptions.PRAWException as e:  # Corrected the exception class name
    print(f"An error occurred while interacting with Reddit: {e}")
except configparser.Error as ce:
    print(f"Error with configuration: {ce}")
except IOError as io_err:
    print(f"IO error: {io_err}")
except Exception as general_error:
    print(f"An unexpected error occurred: {general_error}")
