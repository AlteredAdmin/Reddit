# Subreddit to text

`reddit_subreddit_to_text` is a Python script designed to fetch posts from specified subreddits on Reddit and save their details in text format. The script is built using the `praw` library to interact with the Reddit API.

## Features

- Fetches posts from any subreddit (both new and hot posts).
- Saves post details such as title, timestamp, karma, URL, and comments to a text file.
- Easy-to-use configuration setup for Reddit API credentials.

## Requirements

- Python 3
- PRAW (Python Reddit API Wrapper)
- configparser

## Installation

1. Clone this repository or download the script.
2. Install required packages:

   ```
   pip install praw configparser
   ```

## Configuration

Before running the script, you need to set up your Reddit API credentials. The script will prompt you for your `client_id`, `client_secret`, and `user_agent`. These details are stored in a configuration file for subsequent use.

## Usage

1. Run the script:

   ```
   python reddit_subreddit_to_text.py
   ```

2. Enter your Reddit API credentials when prompted (only required on the first run).
3. Enter the name of the subreddit you want to scrape.

The script will save new and hot posts in separate text files named `<subreddit_name>_NEW_submissions.txt` and `<subreddit_name>_HOT_submissions.txt`.

## Error Handling

The script includes basic error handling for common issues such as Reddit API errors, configuration errors, and general IO errors.

## Support the Developer
If you found this helpful, please consider:
- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)
