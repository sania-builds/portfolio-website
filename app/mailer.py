"""
mailer.py

Sends contact form messages to the site owner by email through Gmail's
SMTP server. Credentials come from environment variables so they are
never stored in the code.
"""

import smtplib
from email.message import EmailMessage

from flask import current_app


def send_contact_email(name, email, subject, message):
    """
    Emails a contact form submission to the site owner.
    Returns True if the email was sent, False otherwise.
    """
    username = current_app.config.get("MAIL_USERNAME")
    password = current_app.config.get("MAIL_PASSWORD")
    recipient = current_app.config.get("MAIL_RECIPIENT") or username

    if not username or not password:
        current_app.logger.warning("Email credentials are not configured.")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio contact: {subject}"
    msg["From"] = username
    msg["To"] = recipient
    msg["Reply-To"] = email
    msg.set_content(
        f"You received a new message from your portfolio website.\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n"
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(username, password)
            server.send_message(msg)
        return True
    except Exception as error:
        current_app.logger.error(f"Failed to send contact email: {error}")
        return False
