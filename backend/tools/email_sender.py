"""
Simple email sender for daily summaries.
DO NOT store credentials in code. Provide via environment variables when running.
"""

import os
import smtplib
from email.message import EmailMessage
from utils.logger import log_info

def send_email_report(to_email, subject, body, smtp_host=None, smtp_port=None, username=None, password=None):
    log_info("send_email_report running...")
    smtp_host = smtp_host or os.getenv("SMTP_HOST")
    smtp_port = smtp_port or int(os.getenv("SMTP_PORT", "587"))
    username = username or os.getenv("SMTP_USER")
    password = password or os.getenv("SMTP_PASS")
    if not smtp_host or not username or not password:
        raise ValueError("SMTP credentials not provided. Set env SMTP_HOST, SMTP_USER, SMTP_PASS")

    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_host, smtp_port) as s:
        s.starttls()
        s.login(username, password)
        s.send_message(msg)
