### zchryrr.py
### Version = 1.0.0

import tweepy #Should be installed
import string
import re
from vars import *
import platform
import sys
import urllib2
import threading
import pyrowl

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            #print '\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source)
            #print status.text
            parse_objects(status)
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
       	p.push("@Zchryrr", "Error", "An error has occured! Status code = %s." % status_code + " Godspeed.","","","")		
        return True  # keep stream alive
        
	def on_limit(self, track):
		p.push("@Zchryrr", "Limit Notice", "Limit Notice has arrived! Ahhhh!","","","")		
		return
    def on_timeout(self):
    	p.push("@Zchryrr", "Timeout", "@Zchryrr has timed out. Serious issue...","","","")		
        print 'Snoozing Zzzzzz'

def error_handling(error_message):
	if tweepy.error.TweepError:
		p.push("@Zchryrr", "@Zchryrr is broken!", error_message)

def check_dms():
	print "Checking DMs"
	if api.direct_messages():
		for message in api.direct_messages():
			print "Found some messages"
			print message.text
			parse_objects_dm(message)
			api.destroy_direct_message(message.id)
	else:
		print "I aint got no messages!"
	
	threading.Timer(60, check_dms).start()	

def parse_objects(message):
	print "Message text: " + message.text
	message_split = message.text.split(" ")
	print message_split
	array_count = len(message_split)
	print array_count
	if array_count > 1:
		if message_split[0] == "@Zchryrr" or "@zchryrr":
			check_command(message_split[1], message_split, message)
			
def parse_objects_dm(message):
	print "Message text: " + message.text
	message_split = message.text.split(" ")
	print message_split
	array_count = len(message_split)
	print array_count
	check_command(message_split[0], message_split, message)
				
def check_command(hashtag, split_command_array, original_object):
	print hashtag
	if hashtag == "#SHUTDOWN":
		if original_object.author.screen_name == "ZacharyOrr":
			shutitdown()
			
	if hashtag == "#PROWL":
		send_prowl_ping()
	
	if hashtag == "#TOR":
		try:
			response = urllib2.urlopen(split_command_array[2]) # Some shortened url
		except:
			response = urllib2.urlopen(split_command_array[1]) # Some shortened url
		url_destination = response.url
		try:
			os.system("cd " + torrent_directory + " && wget " + url_destination)
			if split_command_array[1] == hashtag and original_object.author.screen_name in authorized_torrenters:
				try:
					error_handling(split_command_array[0] + " Mischief Manged >:3")
				except:
					error_handling("Running torrent but failed to update status")
			else:
				error_handling(original_object.author.screen_name + " has attempted to start a torrent.")
		except:
			error_handling("Torrenting " + url_destination + " failed")
			
	if hashtag == "#STATUS":
		get_status(original_object.author.screen_name)

	if hashtag == "#FOLLOW":
		if original_object.author.screen_name == "ZacharyOrr":
			follow_me(split_command_array[2])
		else:
			error_handling(original_object.author.screen_name + " has tried to follow " + split_command_array[2]) 

	if hashtag == "#STACHE":
		try:
			mustache(split_command_array[2], original_object.author.screen_name)
		except:
			error_handling("Could not mustache")
	
def mustache(url, user):
	mustache_url = "http://mustachify.me/?src=" + url
	api.update_status("@"+user+" "+mustache_url)

def follow_me(to_follow):
	try:
		api.create_friendship(split_command_array[2])
		print "Following " + split_command_array[2]
		error_handling("Now following " + split_command_array[2])
	except:
		error_handling("Failed to follow user " + split_command_array[2])

def get_status(user):
	try:
		api.update_status(user + " Zchryrr is currently online!")
	except:
		error_handling("Running, but failed to send update")

def shutitdown():
	error_handling("Shutting down by request")
	sys.exit(1)

def send_prowl_ping():
	p.push("Twitter DM", "DM'd", "Zchryrr was requested to DM you","","","")		

def follow_back():
	try:
		followers = api.followers() #Gets an array (followers) of all of my followers
	except:		
		error_handling("Could not get followers")
	try:
		friends = api.friends() #Gets an array (friends) of all of the people I'm following
	except:
		error_handling("Could not get friends")
		
	followers_list = [u.screen_name for u in followers] #Sets followers so it's something readable
	friends_list = [s.screen_name for s in friends] #sets friends so it's something readable
	print followers_list #prints out followers
	print friends_list #prints out following
	for follower in followers_list:
	    if follower not in friends_list:
	    	tweepy.API(auth) #set's api
	        to_follow.append(follower)	
	        print to_follow
	for follower in tweepy.Cursor(api.followers).items():
		try:
			if follower in tweepy.Cursor(api.friends).items():
				print "Already following %s", follower.screen_name
				pass
			else:
				print follower.screen_name
				print follower in tweepy.Cursor(api.followers).items()
				follower.follow()
		except:
			#error_handling("Couldn't follow back")
			pass
	pass
	threading.Timer(3600, follow_back).start()

def main():
	p.push("@Zchryrr", "Status", "@Zchryrr has started!", "", "", "")
	#follow_back()
	while 1:
		stream.userstream()
		
#Tweepy API Stuff
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
stream = tweepy.Stream(auth, StreamListener(), timeout=None, secure=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'