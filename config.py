import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7439140731:AAHk4e5ZmzdPiRt3LJ5p7rUt1nD2xwbF2UQ")
API_ID = os.environ.get("API_ID", "28795512")
API_HASH = os.environ.get("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001970127211"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7381171860").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://SachinSanatani:SACHINxSANATANI@sanatani.bnmsfbd.mongodb.net/?retryWrites=true&w=majority&appName=Sanatani")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
