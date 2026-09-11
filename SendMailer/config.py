import os
from dotenv import load_dotenv

load_dotenv()

gmail = os.getenv("GMAIL_ADDRESS")
app_password = os.getenv("GMAIL_APP_PASSWORD")