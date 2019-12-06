## Import the modules fro Rasp PI
from picamera import PiCamera()
from datetime import datetime
from time import sleep
from gpiozero import Button
from random import choice 
import tweepy
import json

## Set up the camera object and tactile button call
camera = PiCamera()
button = Button(14) #ask Prof Li to see if we can program a keyboard key to take the picture or act as the button

####### TWITTER API STUFF #######
with open('twitter_auth.json') as file:
    secrets = json.load(file)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)

status = ["Looking Fresh, keeping  it cash", 
            "Hello, World! I'm a Dub!", 
            "DM me if you think I'm a 10",
            "I belong on Reddit's r/camwhores or r/hotpics", 
            "Come on, you know I'm a dub"]



filename = ''
## Take the picture by defining a function that gets timestamp, takes a photo and then saves it. 

def take_photo():
	global filename
    ## Get the current datetime stamp 
    now = datetime.now()

    filename = "{0:%Y}-{0:%m}-{0:%H}-{0:%M}-{0:%S}.png".format(now)
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/filename where it saves picture".format(filename))
    camera.stop_preview()
    ## Code to get the timstamp
	## Then take a photo and save it 


#sends the tweet to twitter but picks a random phrase from the ones we wrote above
def send_tweet():
    twitter.update_with_media(filename, choice(status))
	##code to send tweet

#final action command that prompts the teddy bear to take the photo and then send the tweet
def main():
    take_photo()
    send_tweet()


## Code to trigger the function when the button is pressed
btn.when_pressed = main


# button.when_pressed = take_photo

## Remove the camera.close()
## Close the camera
## camera.close()