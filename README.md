# README.md for AlteredAdmin's Reddit Tools

## Overview

AlteredAdmin Reddit Tools is a suite of Python scripts designed for various Reddit-related tasks, such as fetching posts from subreddits, extracting URLs, and saving post content to text files. These scripts utilize the PRAW library to interact with Reddit's API and are built for ease of use and flexibility.

## Scripts Overview

1. **Subreddit to Text**: Extracts posts from specified subreddits, saving their details and comments into text files.
2. **Reddit Post to Text**: Downloads a specific post and its comments from a given URL and saves them as a text file.
3. **Fetch Domain to Text**: Gathers posts from a specified domain on Reddit and displays details in the console.
4. **Reddit URL Scraper**: Extracts and saves URLs from a target subreddit or user's submissions, filtering by time.

## Installation

1. Clone or download this repository.
2. Ensure Python 3.x is installed on your system.
3. Install required Python packages: `pip install praw configparser datetime re os`

## Usage

- Run the script of your choice from the command line.
- On first run, each script will prompt you for Reddit API credentials (client_id, client_secret, user_agent) and store them in a configuration file.
- Follow on-screen instructions for each script to input specific parameters like subreddit names, URLs, or domains.

## Requirements

- Python 3.x
- PRAW: Python Reddit API Wrapper
- configparser: For handling configuration files
- datetime: For working with dates and times
- re: For regular expression operations
- os: For operating system dependent functionality

## Configuration

Each script will guide you through setting up a configuration file on its first run. This file stores essential information like Reddit API credentials and is typically located in the user's home directory.

## Support the Developer
If you found this helpful, please consider:
- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)

