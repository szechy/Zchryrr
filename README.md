@Zchryrr
================================

Zchryrr (interchangeable with @Zchryrr) is a Twitter bot made up in Python to do simple tasks. Currently, the tasks include:

* Begin torrents from a URL via a reply (only from users in the authorized_torrenters list)

* Serve up mustached images!

* Send a Prowl ping to my phone (used for debugging purposes)

* Return the status of @Zchryrr (If he's running - if he's not running he won't return anything)

* Shutdown Zchryrr (only useable by myself - any additions to usernames will be changed)

* Follow users by request (needs authorization)

How Can I Use Zchryrr?
--------------------------------

To actually use Zchryrr, you'll need to have your own Twitter account (unless you want to run this on your prmiary account, which I do not recommend). I'll trust you can figure out how to make a Twitter account.

Next, head over to [dev.twitter.com](http://www.dev.twitter.com/) and sign in to your new Twitter account. Under the drop down of your name, click "My applications"

![Drop Down Menu](http://zcry.me/5ut2)

Assuming you don't have any other applications yet, click the "Create a new application" button

![Who can blame me? Vowels ARE pretty lame](http://zcry.me/wSZ4)

I'm gonna leave you with the picture below for how to set up the application. It's pretty simple.

![Easy enough?](http://zcry.me/GtBU)

Don't forget to agree to the ToS and enter the CAPTCHAs at the bottom. 

On the page you get directed to, you'll need to click the "Create my access token" button to get the information you need. The rest of the information you might need is included on that page.

![I know what you're thinking, you sneaky snake. But that application is no longer valid.](http://zcry.me/kWs2)

Then go to the "Settings" tab and change your "Application Type" to "Read, Write, and Access direct messages"

![Don't worry. Zchryrr won't go all HAL 9000 on you. You can trust him to access your DMs](http://zcry.me/IvCZ)

Now that we have that all set up, let's start with the actual code. To run your own Zchryrr on your local server, you'll need to first install Tweepy (the Python Twitter library I use)

	sudo pip install tweepy
	
Next, you'll need to edit your vars.py file to make sure that you have all of your information for you Python bot. You'll need to make a new application through the Twitter developer API (details and images on how to do this will come later). In vars.py, fill in the following areas

	p = pyrowl.Pyrowl("api key", "providerkey") #Check the Prowl website for an API key
	
	CONSUMER_KEY = '' #Set your Twitter consumer key
	
	CONSUMER_SECRET = '' #Set your Twitter consumer secret
	
	ACCESS_KEY='' #Set your Twitter access key
	
	ACCESS_SECRET='' #Set your Twitter access secret
	
	sudoers = ["ZacharyOrr"] #List of users who will have access to upper level commands, like starting torrents or shutting the bot down
	
	invalid_sudoer_message = "" #Message that will be tweeted when someone not in the list above tries to use an upper level command
	
	torrent_directory = "/home/zachorr/torrents/" #Directory that your torrent files will be downloaded to. Usually dependent on if you have torrents automatically starting from a folder location
	
After filling in all of that information, you should be set to go. CD to your directory and run
	
	python zchryrr.py

And if you'd like him to run in the background, run

	python zchryrr.py

Taking Advantage of @Zchryrr
--------------------------------

[Images and documentation to come soon of how to access some of the commands for Zchryrr]

And my implementation of this script, the real Zchryrr, is always running over at [twitter.com/Zchryrr](http://www.twitter.com/Zchryrr). Feel free to use him all you'd like!

Upcoming Features List
--------------------------------

* \#CuteCatMeBro - Serves up random cute cat images from Tumblr. Because who couldn't use more cute cats?

* Select memes will be able to be generated on the fly. To start, it'll just be some of my favorites.

* Chuck Testa mode - Will reply "Nope. Chuck Testa" to all questions when he is mentioned

How To Contribuite
--------------------------------

Did I break something? Do you want to add a feature? Do you want to see a feature added?

1. Fork it.
2. Create a branch (`git checkout -b my_repo_name`)
3. Commit your changes (`git commit -am "Added Moar Magic Sauce"`)
4. Push to the branch (`git push origin my_repo_name `)
5. Create an [Issue][1] with a link to your branch
6. Enjoy a refreshing Diet Coke and wait

Don't write Python code but would like a new feature? Create an issue with a feature and I'll see what I can do to implement it!
