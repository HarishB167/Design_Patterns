from typing import List
from .tweet import Tweet

class TwitterClient:

    def get_recent_tweets(self, access_token: str) -> List[Tweet]:
        print("Getting recent tweets")
        return []
    