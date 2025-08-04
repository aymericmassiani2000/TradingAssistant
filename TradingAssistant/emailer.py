import smtplib
import os
from email.message import EmailMessage

def send_email_alert(alerts):
    user = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASS")

    msg = EmailMessage()
    msg['Subject'] = "🚨 Crypto Alert: Major Altcoin Move"
    msg['From'] = user
    msg['To'] = user

    body = "\n".join([f"{coin}: {change:.2%} on {source} → ${price:.4f}" for coin, change, source, price in alerts])
    msg.set_content(f"The following altcoins moved more than ±50%:\n\n{body}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)
