from .gmail.gmail_client import GmailClient
from .email_provider import EmailProvider

class GmailProvider(EmailProvider):

    def __init__(self, provider: GmailClient) -> None:
        self.provider: GmailClient = provider

    def download_emails(self):
        self.provider.connect()
        self.provider.get_emails()
        self.provider.disconnect()
        