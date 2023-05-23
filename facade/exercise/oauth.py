
class Oauth:

    def request_token(self, app_key: str, app_secret: str) -> str:
        print("Get a request token")
        return "request_token"

    def get_access_token(self, request_token: str) -> str:
        print("Get an access token")
        return "access_token"
        