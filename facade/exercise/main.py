from .twitter_api import TwitterApi

def show():

    twitter_api = TwitterApi("app_key", "secret")
    tweets = twitter_api.get_recent_tweets()

if __name__ == "__main__":
    show()


