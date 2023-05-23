from .oauth import Oauth

class OauthService:
    
    def get_access_token(self, app_key: str, app_secret: str):
        oauth = Oauth()
        request_token = oauth.request_token(app_key, app_secret)
        return oauth.get_access_token(request_token)
        