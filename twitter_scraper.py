import tweepy
from tweepy import Stream
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener
import MySQLdb

# == OAuth Authentication ==
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="*********"
consumer_secret="*********"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="***********"
access_token_secret="**********"

# open the connection to the MySQL server
mydb = MySQLdb.connect(host='igor.gold.ac.uk',
    user='*********',
    passwd='*********',
    db='**********')
cursor = mydb.cursor()

# continious listening to twitter stream ... 
class listener(StreamListener):
	def on_data(self, data):	    	
		try:

			# shows tweet's anatomy: inspect and choose which data to extract 
			# print data 
			
			# get tweet text out of data
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet

			## get date and time out of data 
			# date_time = data.split('"created_at":')[1].split(',"id":')[0]
			# print date_time

			# insert directly into MySQL db
			data_tweet = tweet
			add_tweet = ('INSERT INTO bit_test(tweets) VALUES(%s)')
			cursor.execute(add_tweet, data_tweet) 

			return True
			# print "Import to MySQL is over"
			time.sleep(5)
		except BaseException,e: 
			print 'failed ondata,',str(e)
			
	def on_error(self, status):
		print status

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# at locatedst! we can search for tweets
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#bitcoin"])
