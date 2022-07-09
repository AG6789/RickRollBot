#rickroll bot

import praw 

bot = praw.Reddit(user_agent='RickRollBot v0.1',
                  client_id='PXelA16HMvxdxKl2nWQpvA',
                  client_secret='sThGzcvfiMwX0sV0IjvbrlSihd7o7A',
                  username='rickroll-or-not-bot',
                  password='30072018')

subreddit = bot.subreddit('all')

comments = subreddit.stream.comments()

for comment in comments:
    text  = comment.body
    author = comment.author 
    if 'dQw4w9WgXcQ' in text:
        message = "u/{0}, you dirty rickroller :(".format(author)

        comment.reply(message) # Send message