import os
from datetime import datetime
import praw

# Constants
CONFIG_DIR = os.path.join(os.path.expanduser("~"), "RedditDomainScout_Configs")
CONFIG_FILE = os.path.join(CONFIG_DIR, "RedditDomainScout_Configs.txt")


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


def main():
    client_id, client_secret = get_api_config()
    USER_AGENT = 'RedditDomainScout'

    domain = input("Enter the domain you want to fetch posts from (e.g. imgur.com): ")

    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=USER_AGENT)

        # Fetch and display submissions
        for submission in reddit.domain(domain).new():
            title = submission.title
            created_time = datetime.fromtimestamp(submission.created)
            url = submission.url
            print(f"Title: {title}\nTime: {created_time}\nURL: {url}\n{'-' * 40}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
