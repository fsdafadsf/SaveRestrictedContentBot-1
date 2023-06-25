#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=23411548, cast=int)
API_HASH = "349a01b6713ac1dd0c750e9ed3028021"
BOT_TOKEN = "6179624200:AAH6O9LUu_2yzJx9goE7Xx55SHzZp3nVC40"
SESSION = "BQCdpfEuL7PZnN0xxBVnFtooJNHzljD9IplBIXSc-FkDayLbxrt_KxuCX_wXsjL2w1f28M9zxlh9D7xRW7x27rE0FJrQtNOopFP9D2cDarztU090xQifMFnmADWWDReFSGUYKL1Wlmm_KbKeS5P-MCd1rUtvegkwPVv9wi09AnkCOSmhJgN1l_2I9F5WJvofFOxGDrV_PvNsHpQMVpQBGTfQLn2Sg40fY8EmH4SV5mWCkYeRQbIMnM4QFGUjBcthp-V9o4kKSiBLMwI9Yz-v1ZziOF5LgahKp_-o_fWIbKz3qKWd2whfh_snTbUZxnh52pc73R40Ir0ijGqfxOQ6j0iaL-Xs5QA"
FORCESUB = "SaveRestrictedContent02"
AUTH = config("AUTH", default=803597541, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)
try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
