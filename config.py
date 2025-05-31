import os
from typing import List

API_ID = os.environ.get("API_ID", "23889992")
API_HASH = os.environ.get("API_HASH", "70bf3c9baebf30afff8c32649bf23c3d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "1900118264"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002645203047"))

DB_URI = os.environ.get("DB_URI", "mongodb+srv://HDMoviesEarth:unqOY8gUrmDLNXHd@cluster0.0xjypxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "HDMoviesEarth")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001943817170").split())) # Add Multiple channel ids
