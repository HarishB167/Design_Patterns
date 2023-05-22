from .email_client import EmailClient
from .gmail_provider import GmailProvider
from .gmail.gmail_client import GmailClient

if __name__ == "__main__":
    email_client = EmailClient()
    email_client.add_provider(GmailProvider(GmailClient()))
    email_client.download_emails()
    