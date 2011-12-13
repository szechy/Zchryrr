import tweepy
import pyrowl
import os
import platform
import datetime

p = pyrowl.Pyrowl( "", "providerkey")
CONSUMER_KEY = '' #Set consumer key
CONSUMER_SECRET = '' #Set consumer secret
ACCESS_KEY='' #Set access key
ACCESS_SECRET='' #set access secret
tweet_ids = []
to_follow = []
sudoers = [""]
invalid_sudoer_message = "User is not in the sudoers file. This incident will be reported... To Santa!"
torrent_directory = ""

now = datetime.datetime.now()