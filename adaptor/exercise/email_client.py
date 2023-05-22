from typing import List
from .email_provider import EmailProvider

class EmailClient:

    def __init__(self) -> None:
        self.providers: List[EmailProvider] = []

    def add_provider(self, provider: EmailProvider):
        self.providers.append(provider)

    def download_emails(self):
        for provider in self.providers:
            provider.download_emails()