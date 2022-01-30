
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


## find negative posts 
## pull every post and check if it contains negative words

## the question is , what if the post has multiple words in the excel sheet

## airflow phase will be for hw 1
## count the occurences of each word in the post if theres more negative words than positive words post is negative
## if theres more positive words than negative words post is positive
## its inpsiring people to read the post 
## check if what makes a post conterversational 
## use airflow to schedule the job

## would positive posts be more engaging?
## would negative posts be more engaging?

## using twitter api to pull tweets
##pull posts that represent reddit
## use a sample of the posts to test the model
## predict the upvotes of the post
## classify the post as catogory
## posts as positive or negative

## Catagorize the posts with negative and positive 

## design the table 
## create a table with the columns
## post_id, post_title, post_text, post_score, post_category
## post_id is the id of the post date as id
## each post per row


## Date    Post_ID(id)    Post_Title(title)    Post_Text(text)    Post_Score(Upvotes)    Post_Category

## what is sentiment analysis?

## count positive and negative words in the post
## if theres more negative words than positive words post is negative

## range from -1 to 1 
## Do negative posts get more influence over positive posts?

