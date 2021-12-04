# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: Shawn Zhu
# netid: jiachzhu      
# Student ID: 114590303

import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "b37NODAQBwDTT7QqLcM6gZMsR"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "luCsdclCIafY3qu1LaWM2OoUpuwZ4tKPIU4AI0Q0UIIDWkriQg"

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    tweets = simple_twit.get_home_timeline(api, 10)
    for tweet in tweets:
        print("ID: " + tweet.id_str + "\n author: " + tweet.author.name + "\n author's screen_name: " + tweet.author.screen_name + "\n creation date: " + str(tweet.created_at) + "\n full text: " + tweet.full_text)

# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    tweets = simple_twit.get_user_timeline(api, "IAE101_ckane", 10)
    for tweet in tweets:
        print("ID: " + tweet.id_str + "\n author: " + tweet.author.name + "\n author's screen_name: " + tweet.author.screen_name + "\n creation date: " + str(tweet.created_at) + "\n full text: " + tweet.full_text)


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    simple_twit.send_tweet(api, "Tweeting!")


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    simple_twit.send_media_tweet(api, "Art of the day", (r"C:\Users\Yiwuz\Desktop\IAE-101-Projects\Twitter\sunflower2.jpg"))

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(api):
    pass # remove this and replace with your solution code


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    exercise1(api)
    exercise2(api)
    exercise3(api)
    exercise4(api)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
