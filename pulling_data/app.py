
import xlsxwriter
import json
import time
import datetime
import os
import numpy as np
import pandas as pd
import tweepy as tw
import requests as rq
from flask import Flask
import praw
import dotenv


# Load environment variables
dotenv.load_dotenv()
reddit_key = os.getenv("REDDIT_KEY")
reddit_secret = os.getenv("REDDIT_SECRET")



reddit_key = os.getenv("REDDIT_KEY")
reddit_secret = os.getenv("REDDIT_SECRET")


reddit = praw.Reddit(
    client_id=reddit_key,
    client_secret=reddit_secret
    , user_agent= "radical"
    , username= "segfal32"
    )

subreddit = reddit.subreddit("compsci")


#for submission in reddit.subreddit("compsci").hot(limit=1):
    #print(submission.title)
    #submission.public_description
    
#    print(submission.selftext)
    
#    for comments in submission.comments:
#        print(comments.body)## prints all comments
    

#print(subreddit.public_description)

'''
for submission in reddit.subreddit("compsci").new(limit=10):
    print(submission.title)
    print(submission.selftext)
''' #prints new posts
