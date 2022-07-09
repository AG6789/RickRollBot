#rickroll bot

import praw 

bot = praw.Reddit(user_agent='RickRollBot v0.1',
                  client_id='demo_ID',
                  client_secret='demo_secret',
                  username='demo_username',
                  password='demo_pwd')

subreddit = bot.subreddit('all')

comments = subreddit.stream.comments()

for comment in comments:
    text  = comment.body
    author = comment.author 
    if 'dQw4w9WgXcQ' in text:
        message = "u/{0}, you dirty rickroller :(".format(author)

        comment.reply(message) # Send message
