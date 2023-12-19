import os
import praw
import prawcore
import re
import time
from datetime import datetime


def load_config():
    home_directory = os.path.expanduser("~")
    directory_path = os.path.join(home_directory, 'AlteredAdmin_Reddit_Tools')
    file_path = os.path.join(directory_path, 'Reddit_URL_Scraper_Configs.txt')

    if not os.path.exists(directory_path):
        os.mkdir(directory_path)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            client_id = input("Enter your Reddit API client_id: ")
            client_secret = input("Enter your Reddit API client_secret: ")
            user_agent = input("Enter your user agent for Reddit API (e.g., 'Reddit Link Reaper User Agent'): ")
            file.write(f"client_id={client_id}\n")
            file.write(f"client_secret={client_secret}\n")
            file.write(f"user_agent={user_agent}\n")
        print(f"Config saved to {file_path}.")

    with open(file_path, 'r') as file:
        lines = file.readlines()
        config = {}
        for line in lines:
            key, value = line.strip().split('=')
            config[key] = value

    return config['client_id'], config['client_secret'], config['user_agent']


def extract_urls(target, target_type='subreddit', time_filter='all'):
    client_id, client_secret, user_agent = load_config()
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    urls = []

    try:
        if target_type == 'subreddit':
            subreddit = reddit.subreddit(target)
            if time_filter not in ['all', 'day', 'hour', 'month', 'week', 'year']:
                raise ValueError("Invalid time filter. Choose from 'all', 'day', 'hour', 'month', 'week', 'year'.")
            submissions = subreddit.top(time_filter=time_filter, limit=None)

            for submission in submissions:
                process_submission(submission, urls)

        elif target_type == 'user':
            user = reddit.redditor(target)
            submissions = user.submissions.top(time_filter=time_filter, limit=None)

            for submission in submissions:
                process_submission(submission, urls)

    except prawcore.exceptions.NotFound:
        print(f"Error: The {target_type} '{target}' was not found. Please check the name and try again.")
    except prawcore.exceptions.TooManyRequests as e:
        print("Too many requests. Waiting for 60 seconds before retrying...")
        time.sleep(60)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if urls:
            save_to_file(target, urls, append=True)

    return urls


def process_submission(submission, urls):
    print(f"Processing submission: {submission.title}")
    if not submission.is_self:
        urls.append(submission.url)

    urls.extend(extract_urls_from_text(submission.selftext))
    try:
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            print(f"Processing comment by {comment.author}")
            urls.extend(extract_urls_from_text(comment.body))
    except prawcore.exceptions.TooManyRequests as e:
        print("Too many requests when processing comments. Waiting for 60 seconds before retrying...")
        time.sleep(60)  # Wait for 60 seconds before retrying


def extract_urls_from_text(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(text)
    return [url for url in urls if not url.startswith('https://www.reddit.com/')]


def save_to_file(target_name, urls, append=False):
    mode = 'a' if append else 'w'
    filename = f"{target_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, mode) as file:
        for url in urls:
            file.write(f"{url}\n")
    print(f"URLs {'appended to' if append else 'saved to'} {filename}")


if __name__ == "__main__":
    urls = []
    target = ""
    try:
        target_type = input(
            "Do you want to fetch URLs from a subreddit or a user's account? Enter 'subreddit' or 'user': ").strip().lower()

        if target_type not in ['subreddit', 'user']:
            print("Invalid selection. Please choose either 'subreddit' or 'user'.")
            exit()

        target = input(f"Enter the name of the {target_type}: ")
        time_filter = input("Enter the time filter (all, day, hour, month, week, year): ")

        urls = extract_urls(target, target_type, time_filter)
        if not urls:
            print("No URLs extracted.")
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Saving collected URLs...")
    finally:
        if urls:
            save_to_file(target, urls, append=True)
        print("Exiting script.")
