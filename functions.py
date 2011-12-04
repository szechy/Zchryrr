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