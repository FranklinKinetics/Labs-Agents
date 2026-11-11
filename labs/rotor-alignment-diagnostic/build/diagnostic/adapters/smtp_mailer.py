"""REAL mailer sketch using SMTP. Not called by any test. Credentials come from
environment variables only: DIAG_SMTP_HOST, DIAG_SMTP_USER, DIAG_SMTP_PASSWORD
(Secret Manager in production). Step 2 decides the real route (Google
Workspace mailbox or a sending service); this is the placeholder shape."""
from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage

from ..emails import Email, Mailer


class SmtpMailer(Mailer):
    def __init__(self, from_addr: str = "contact@franklinkinetics.com"):
        self.host = os.environ["DIAG_SMTP_HOST"]
        self.user = os.environ["DIAG_SMTP_USER"]
        self.password = os.environ["DIAG_SMTP_PASSWORD"]
        self.from_addr = from_addr

    def send(self, email: Email) -> None:
        m = EmailMessage()
        m["From"], m["To"], m["Subject"] = self.from_addr, email.to, email.subject
        m.set_content(email.body)
        for name, data, mime in email.attachments:
            maintype, _, subtype = mime.partition("/")
            m.add_attachment(data, maintype=maintype, subtype=subtype, filename=name)
        with smtplib.SMTP_SSL(self.host, 465, timeout=30) as s:
            s.login(self.user, self.password)
            s.send_message(m)
