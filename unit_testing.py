import unittest
import tweepy
import time
from vars import *
from zchryrr import Zchryrr, StreamListener
from tweepy.error import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
timeout = 1
zchryrr_test = Zchryrr()
class TestZchryrr(unittest.TestCase):
	#For testing Zchryrr
	def setUp(self):
		zchryrr_test = Zchryrr()
	
	def tearDown(self):
		zchryrr_test = None
				
	def test_auth(self):
		zchryrr_test.auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
	
	def test_status_check(self):
		zchryrr_test.get_status("Zchryrr")
		time.sleep(timeout)
		mentions = zchryrr_test.api.mentions()
		for tweet in mentions:
			if("Zchryrr is currently" in tweet.text):
				zchryrr_test.api.destroy_status(tweet.id)
				break
	
	def test_mustache(self):
		zchryrr_test.mustache("http://dl.dropbox.com/u/4132519/DSC_0091.JPG", "Zchryrr")
		time.sleep(timeout)
		mentions = zchryrr_test.api.mentions()
		for tweet in mentions:
			if("mustachify" in tweet.text or "t.co" in tweet.text):
				zchryrr_test.api.destroy_status(tweet.id)	
				break

if __name__ == '__main__':
    unittest.main()