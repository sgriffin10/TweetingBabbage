## Import the modules fro Rasp PI
from picamera import PiCamera
from datetime import datetime
from time import sleep
from random import choice 
import tweepy
from credentials import *

## Set up the camera object 
camera = PiCamera()

####### TWITTER API #######
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    twitter = tweepy.API(auth)
    return twitter

status = ["G's Only!!!","Looking Fresh, keeping  it cash", 
            "Hello, World! I'm a Dub!", 
            "DM me if you think I'm a 10",
            "I belong on Reddit's r/hotpics", 
            "Come on, you know I'm a dub"]





filename = ''
## Take the picture by defining a function that gets timestamp, takes a photo and then saves it. 

def take_video():
    '''
    Creates filename variable which will name photo based on the time taken.  
    Uses PiCamera module to open camera, set up for 5 seconds, capture photo, and save it to path specified. 
    '''
    global filename
    # Get the current datetime stamp 
    now = datetime.now()
    filename = "{0:%Y}-{0:%m}-{0:%H}-{0:%M}-{0:%S}.png".format(now)
    camera.start_preview(alpha=190)
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    sleep(5)
    camera.capture("/home/pi/Desktop/TweetingBabbage/Photos/{0}".format(filename))
    camera.stop_preview()
    # Code to get the timstamp
	# Then take a photo and save it 
    


#sends the tweet to twitter but picks a random phrase from the ones we wrote above
def send_tweet():
    '''
    Uses Twitter API to send out tweet of the photo with the corresponding filepath below

    '''
    twitter = twitter_setup()
    twitter.update_with_media("/home/pi/Desktop/TweetingBabbage/Photos/{0}".format(filename), choice(status)) 
	##code to send tweet

#final action command that prompts the teddy bear to take the photo and then send the tweet

def main():
    '''
    Triggers take_photo() and sent_tweet() functions
    '''
    take_video()
    send_tweet()

if __name__ == "__main__":
    main()
