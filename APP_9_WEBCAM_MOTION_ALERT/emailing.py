from dotenv import load_dotenv
import os
import smtplib
import filetype
from email.message import EmailMessage

load_dotenv()

username = os.getenv("LOGIN_EMAIL")
receiver = os.getenv("LOGIN_EMAIL")
password = os.getenv("PASSWORD")

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    image_type = filetype.guess(content)
    email_message.add_attachment(content, maintype="image", subtype=image_type.extension)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()
    print("send_email function ended")

if __name__ == "__main__":
    send_email("images/56.png")
