import tweepy
import pyrowl
import os
import platform
import datetime
p = pyrowl.Pyrowl( "51b32b905b70349bcf72a34780e4a89c3564d136", "providerkey")

CONSUMER_KEY = 'CJW0r4Ap2blcYlQV3nSn7g' #Set consumer key
CONSUMER_SECRET = 'NcyE6SrzBiBI1fWnyqZKjBi541ibOZx1sVaJg69k' #Set consumer secret
ACCESS_KEY='371294336-3boCHFOuvaQbUrz70mMT5O8bEg5cWSn0RcEgv4E' #Set access key
ACCESS_SECRET='SvYIS4CZO8zkDKExPCxw7gQqw5gSS5nCpPFc0R32E' #set access secret
tweet_ids = []
to_follow = []
authorized_torrenters = ["ZacharyOrr"]
torrent_directory = "/home/zachorr/torrents/"
#Test
now = datetime.datetime.now()