import tweepy

CONSUMER_KEY = 'CJW0r4Ap2blcYlQV3nSn7g' #Set consumer key
CONSUMER_SECRET = 'NcyE6SrzBiBI1fWnyqZKjBi541ibOZx1sVaJg69k' #Set consumer secret
ACCESS_KEY='371294336-3boCHFOuvaQbUrz70mMT5O8bEg5cWSn0RcEgv4E' #Set access key
ACCESS_SECRET='SvYIS4CZO8zkDKExPCxw7gQqw5gSS5nCpPFc0R32E' #set access secret
p = pyrowl.Pyrowl( "51b32b905b70349bcf72a34780e4a89c3564d136", "providerkey")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) #Call auth command
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) #No clue what this does
api = tweepy.API(auth) #set's api

def parse_objects_dm(message):
	print "Message text: " + message.text
	messagezor = message.text
	message_split = message.text.split(" ")
	print message_split
	array_count = len(message_split)
	print array_count
	check_command(message_split[0], message_split)

def check_command(hashtag, split_command_array):
	if hashtag == "#RESTART":
		#Write restart command
		pass
	if hashtag == "#STATUS":
		try:	
			api.update_status("Oh no! Something has gone wrong! The Medic has taken control!")
		except:
			p.push("@Zchryrr", "Medic Status Report", "Failed to update status. Medic has taken control.","","","")	

def check_dms():
	for message in api.direct_messages():
		parse_objects_dm(message)
		api.destroy_direct_message(message.id)

def main():
	t = Timer(60.0, check_dms)
	t.start()
		
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'
