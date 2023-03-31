import os
import praw
import requests


# Authentication to the reddit app
def authenticate():
    print('logging in...')
    reddit = praw.Reddit("BOT1",
                         client_id="vQ-zP_hXpB27vBaaJDo62A",
                         client_secret="n3B4oRG3OKYPr5yeKvOdPVVNMPzbWw",
                         password="0tt3rL0v3<3!",
                         username="otter_lover_bot",
                         user_agent="BOT1 user agent",
                         )
    print('logged in as {}'.format(reddit.user.me()))
    return reddit


#  scrapes n amount of post in r/'name', sorted by new; day
def get_url(reddit, name, links, amount):
    # find subreddit
    subreddit = reddit.subreddit(name)
    for submission in subreddit.top(limit=amount, time_filter="new"):
        links.append(submission.url)
    return links
