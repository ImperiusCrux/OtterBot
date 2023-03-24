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


# delete all files in dir 'download'
def delete_download():
    target_dir = os.getcwd() + '\\download'
    for file in get_download():
        os.remove(target_dir + '\\' + file)


# get all files in dir 'download'
def get_download():
    target_dir = os.getcwd() + '\\download'
    downloads = []

    for path in os.listdir(target_dir):
        downloads.append(path)

    return downloads


#  scrapes n amount of post in r/Otters, sorted by top; day
def get_top_otters(amount, reddit):
    # store location
    target_dir = os.getcwd() + '\\download'

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # find r/Otters
    subreddit = reddit.subreddit('Otters')
    for submission in subreddit.top(limit=amount, time_filter="day"):
        # save post
        complete_name = os.path.join(target_dir, submission.name + '.jpg')
        r = requests.get(submission.url)
        with open(complete_name, 'wb') as f:
            f.write(r.content)
        f.close()

