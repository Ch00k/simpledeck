from typing import List

import requests
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail.backends.base import BaseEmailBackend


class MailgunEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages: List[EmailMessage]) -> int:
        url = f"{settings.MAILGUN_API_BASE_URL}/{settings.MAILGUN_DOMAIN}/messages"

        count = 0
        for m in email_messages:
            resp = requests.post(
                url,
                auth=("api", settings.MAILGUN_API_KEY),
                data={
                    "from": f"SimpleDeck <accounts@{settings.MAILGUN_DOMAIN}>",
                    "to": m.to,
                    "subject": m.subject,
                    "text": m.body,
                },
            )
            count += resp.status_code == 200

        return count
