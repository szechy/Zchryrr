import unittest
import tweepy
import time
CONSUMER_KEY = 'CJW0r4Ap2blcYlQV3nSn7g' #Set consumer key
CONSUMER_SECRET = 'NcyE6SrzBiBI1fWnyqZKjBi541ibOZx1sVaJg69k' #Set consumer secret
ACCESS_KEY='371294336-3boCHFOuvaQbUrz70mMT5O8bEg5cWSn0RcEgv4E' #Set access key
ACCESS_SECRET='SvYIS4CZO8zkDKExPCxw7gQqw5gSS5nCpPFc0R32E' #set access secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

timeout = 4

class TestZchryrr(unittest.TestCase):
	#For testing Zchryrr
	#def setUp(self):

	def test_status_update(self):
		api.update_status("@Zchryrr #STATUS")
		time.sleep(timeout)
		timeline = api.mentions()
		last_tweet = timeline[0].text
		print timeline[0].text
		self.assertTrue(last_tweet == "@Zchryrr Zchryrr is currently online!")
			
if __name__ == '__main__':
    unittest.main()