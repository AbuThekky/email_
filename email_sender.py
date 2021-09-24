import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #access to html

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Andrei Neagoie"
email["to"] = "zakkycudos@outlook.com"
email["subject"] = "You won 1,000,000 dollars!"

email.set_content(html.substitute({"name": "tintin"}), "html")

with smtplib.SMTP(host="smpt.gmail.com", port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("zak123@gmail.com", "password123")
	smtp.send_message(email)
	print("all good")