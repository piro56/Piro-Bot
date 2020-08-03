import DiscordExtension
from discord import Color
from discord import Embed
import tweepy
import os
import random
from dotenv import load_dotenv


class TwitterAPI:
    def __init__(self):
        load_dotenv()
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        self.auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit_notify=True)
        self.user = self.api.get_user('viruien')
        # TODO: IMPORT AND IMPLEMENT STREAM LISTENER
        self.myStreamListener = MyStreamListener()
        self.filter = ""
        self.silenced = False

    def api(self):
        return self.api

    def loopTimeline(self):
        for status in tweepy.Cursor(self.api.home_timeline, tweet_mode="extended").items(10):
            # TODO: PROCESS STATUS
            print(status.text)
            # process_status(status)

    def myStreamListener(self):
        return self.myStreamListener

    def twitterStream(self):
        return self.twitterStream

    def createStream(self, filterTrack):
        self.stopStream()
        self.filter = filterTrack
        self.twitterStream = tweepy.Stream(auth=self.api.auth, listener=self.myStreamListener)
        self.twitterStream.filter(track=[filterTrack], is_async=True, )
        print(f'Created Stream with filter: {filterTrack}')

    # gets current filter
    def filter(self):
        return self.filter

    def stopStream(self):
        try:
            self.twitterStream.disconnect()
            del self.twitterStream
            self.filter = ""
        except:
            pass

    def toggle_silence(self):
        self.silenced = not self.silenced


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if (valid_tweet(status)):
            try:
                if (not myTwitterExtension.silenced):
                    embedmsg = Embed(
                        # title=f'{status.user.screen_name}',
                        colour=Color.blue(),
                        description=f'{status.text}'
                    )
                    embedmsg.set_author(name=status.user.screen_name, icon_url=status.user.profile_image_url)
                    DiscordExtension.on_Tembed(embedmsg)
                r = random.randint(1, 5)
                if r == 3:
                    message = f'**{status.user.screen_name} -->** {status.text}'
                    myTwitterExtension.api.retweet(status.id)
                    print(f'Retweeted {message}')
            except:
                print("Message does not exist!")


def valid_tweet(status):
    if (not status.text.startswith("RT") and not 'media' in status.entities and not "https" in status.text):
        if (
                status.in_reply_to_status_id is None and status.in_reply_to_user_id is None and myTwitterExtension.filter in status.text):
            return True
        else:
            return False
    else:
        return False


"""TWITTER IS ENABLED HERE"""
myTwitterExtension = TwitterAPI()


def enable_Twitter():
    global myTwitterExtension
    try:
        myTwitterExtension
        return True
    except:
        myTwitterExtension = TwitterAPI()
        print("Enabled twitter")
        return False


def checkStatusTwitter():
    global myTwitterExtension
    try:
        myTwitterExtension
        return True
    except:
        return False


"""DISABLE TWITTER HERE"""


def disable_Twitter():
    global myTwitterExtension
    try:
        del myTwitterExtension
        print("Disabled Module!")
        return True
    except:
        print("Twitter Module is already off!")
        return False
