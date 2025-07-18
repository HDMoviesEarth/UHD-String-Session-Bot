import os
from typing import List

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "1900118264"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002645203047"))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "HDMoviesEarth")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002521290472").split())) # Add Multiple channel ids
