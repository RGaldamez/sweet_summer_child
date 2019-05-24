import praw
from praw.models import MoreComments
import re
import time

reddit = praw.Reddit(client_id='cpP21zhmaFzssQ',
            client_secret='V9aPs_rZqXb3_ifhOuycxk7m49U',
            user_agent='<console:summer_child_bot:0.0.1 (by /u/seraPioSilva)>',
            username='seraPioSilva',
            password='TiNaBimW1776')

# print(reddit.read_only)
subreddits = ['bottesting','testing4756','testingground4bots']
pos = 0
title = "Just a test from a friendly bot"




subreddit = reddit.subreddit('testingground4bots')
submissions = subreddit.new(limit=5)
criteria_list = ['oh sweet summer child','sweet summer child', 'oh, sweet summer child', 'oh you sweet, summer child.']
reply_text = ""


for submission in submissions:
    print("Title: "+submission.title)  # Output: the submission's title
    # print(submission.score)  # Output: the submission's score
    # print(submission.id)     # Output: the submission's ID
    submission.comment_sort = 'new'
    # top_level_comments = list(submission.comments)
    all_comments = submission.comments.list()
    

    for comment in all_comments:
        normalized_body = comment.body.lower()

        for criteria in criteria_list:
            if(criteria in normalized_body):
                comment.downvote()
                

     
    
    

    