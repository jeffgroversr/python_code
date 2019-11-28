import time
time.sleep(5)

import fetch_data
print('fetch_data')
time.sleep(5)
import writetoweb
print('writetoweb')

time.sleep(5)
##########################TWITTER######################
CONSUMER_KEY = 'p7fg9MEglE4CtEajOPdkdcUnG'
CONSUMER_SECRET = '9iouaVZjpsILpBp706hXiWaHHFgkt4qmFUDY3tVDAFgLi7x14i'
ACCESS_TOKEN = '2297016128-bQirsSnuXUrOc48IzJzKCIvIpwYW5ePXG5T4qhc'
ACCESS_SECRET = '0gMwEFa5H6oq8sW3Misufd7zA5oV0z2UOORn1yex7syir'

import tweepy as ty
import random

def setTwitterAuth():

    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

def tweetHelloWorld(api):

    api.update_status("#PoT | #FRED | Check this out! We have just posted 10 of the popular FRED Series daily economic and financial data @ http://bayesniffer.com/PoT.html #{}"
                      .format(random.randint(0, 10000)))

if __name__ == "__main__":
    # set up authorization with twitter via tweepy
    api = setTwitterAuth()
    # tweet hello world!
    tweetHelloWorld(api)
###################TWITTER END#############################
time.sleep(5)
print('Tweeted FRED Pop Series Daily Data')
#import empty_folder

exit()