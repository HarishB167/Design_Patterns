from typing import List
from .oauth import Oauth
from .tweet import Tweet
from .twitter_client import TwitterClient


class TwitterApi:
    def __init__(self, app_key: str, secret: str) -> None:
        self.app_key: str = app_key
        self.secret: str = secret

    def get_recent_tweets(self) -> List[Tweet]:
        twitter_client = TwitterClient()
        tweets = twitter_client.get_recent_tweets(self.get_access_token())
    
    def get_access_token(self) -> str:
        oauth = Oauth()
        request_token = oauth.request_token(self.app_key, self.secret)
        return oauth.get_access_token(request_token)
