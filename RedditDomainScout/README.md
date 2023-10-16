# RedditDomainScout

RedditDomainScout is a Python tool designed to fetch recent posts from a specified domain using the Reddit API. It provides an interactive experience, prompting users for the desired domain and displaying the most recent submissions linked to that domain.

## Features

- Interactive domain input.
- Automated handling of Reddit API configurations.
- Easy storage and retrieval of API configurations.
- Comprehensive error handling.
- Neat and organized output for quick browsing.

## Installation

1. Clone the repository:

```
git clone [repository-url]
```

2. Navigate to the project directory:

```
cd [project-directory]
```

3. Ensure you have the `praw` library installed. If not, install it via pip:

```
pip install praw
```

## Usage

Simply run the `RedditDomainScout.py` script:

```
python RedditDomainScout.py
```

On the first run, you'll be prompted to enter your Reddit API credentials (client ID and client secret). These are stored locally for future runs. 

Next, you'll be prompted to enter the domain you wish to search (e.g., `imgur.com`). The script will then display recent Reddit posts linked to that domain.

## Configuration

Your Reddit API configurations are stored in the `RedditDomainScout_Configs` directory in your home folder, under the `RedditDomainScout_Configs.txt` file.
