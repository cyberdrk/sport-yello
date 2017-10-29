'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = '2LnOkxaXoK8CXmyJ3FzcE2aPb'	#Your Twitter API Consumer Key
MY_CONSUMER_SECRET = 'n7Zp5Q7bkkMHLm3mekzmjoGJK7w8P6G9Og1i4RbBnMz91Scp0q'	#Your Consumer Secret Key
MY_ACCESS_TOKEN_KEY = '924343889707671552-qdeTNU97SP9M4lXW28PyXQcF5Iwjh2i' 	#Your Twitter API Access Token Key
MY_ACCESS_TOKEN_SECRET = 'VjtVEOd9MrU32WbfZ66AKoIGUyOFhqkfq6gaytozTvdf6' 	#Your Access Token Secret

SOURCE_ACCOUNTS = ["Media_SAI", "StarSportsIndia"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 4 #how closely do you want this to hew to sensical? 2 is low and 4 is high.
SOURCE_EXCLUDE = r'^$' #Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "sport_yello" #The name of the account you're tweeting to.
