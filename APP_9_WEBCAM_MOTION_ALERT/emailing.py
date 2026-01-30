from dotenv import load_dotenv
import os

load_dotenv()

def send_email():

    username = "hypernxt@gmail.com"
    password = os.getenv("PASSWORD")

    