#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "10170481"))
API_HASH = environ.get("API_HASH", "22dd74455eb31c9aca628c3008580142")
BOT_TOKEN = environ.get("BOT_TOKEN", "8049431003:AAExrnihVja6SE32huNwL0W5A2RJX1yKtzM")

OWNER = int(environ.get("OWNER", "8048202739"))
CREDIT = environ.get("CREDIT", "𝐈𝐓'𝐬𝐆𝐎𝐋𝐔")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8048202739').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8048202739').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
