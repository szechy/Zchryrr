import unittest
import tweepy
import time
from vars import *
from zchryrr import Zchryrr, StreamListener

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

timeout = 2
zchryrr_test = Zchryrr()

class TestZchryrr(unittest.TestCase):
	#For testing Zchryrr
	def setUp(self):
		zchryrr_test = Zchryrr()

	def test_auth(self):
		zchryrr_test.auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
		
	'''def test_status_update(self):
		zchryrr_test.api.update_status("@Zchryrr #STATUS")
		time.sleep(timeout)
		timeline = zchryrr_test.api.mentions()
		last_tweet = timeline[0].text
		print timeline[0].text
		self.assertTrue(last_tweet == "@Zchryrr Zchryrr is currently online!")
		print "" + timeline[0].id
		print "" + timeline[1].id
		print "" + timeline[0].text
		print "" + timeline[1].text
	'''
	def test_mustache(self):
		zchryrr_test.api.update_status("@Zchryrr #STACHE http://dl.dropbox.com/u/4132519/DSC_0091.JPG")
		time.sleep(timeout)
		timeline = zchryrr_test.api.mentions()
		last_tweet = timeline[0].text
		print timeline[0].text
		self.assertTrue(last_tweet == "@Zchryrr http://mustachify.me/?src=http://dl.dropbox.com/u/4132519/DSC_0091.JPG")
		print timeline
	def test_prowl_ping(self):
		zchryrr_test.send_prowl_ping()
	
			
if __name__ == '__main__':
    unittest.main()