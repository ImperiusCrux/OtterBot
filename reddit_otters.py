import os
import asyncpraw as praw
import requests


# Authentication to the reddit app
async def authenticate():
    print('logging in...')
    reddit = praw.Reddit("BOT1",
                         client_id="vQ-zP_hXpB27vBaaJDo62A",
                         client_secret="n3B4oRG3OKYPr5yeKvOdPVVNMPzbWw",
                         password="0tt3rL0v3<3!",
                         username="otter_lover_bot",
                         user_agent="BOT1 user agent",
                         )
    print('logged in as {}'.format(await reddit.user.me()))
    return reddit


#  scrapes n amount of post in r/'name', sorted by new; day
async def get_url(auth, name, amount):
    links = []
    # find subreddit
    subreddit = auth.subreddit(name)
    for submission in subreddit.new(limit=amount):
        if not submission.is_self:
            links.append(submission.url)
    return links
