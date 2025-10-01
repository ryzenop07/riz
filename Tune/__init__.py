import sys
from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from .logging import LOGGER
from .core.mongo import mongodb
from .core.dir import create_directories
from .core.git import check_git
from .core.bot import ryzen_bot

# Initialize clients
app = ryzen_bot.app

# Initialize Userbot
userbot = Client(
    "RyzenAssistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.STRING1,
)

# Initialize PyTgCalls
pytgcalls = PyTgCalls(userbot)

# Performance optimizations
app.set_parse_mode("html")
userbot.set_parse_mode("html")

# Initialize core components
async def init_ryzen():
    await mongodb.connect()
    create_directories()
    check_git()
    LOGGER(__name__).info("ᴅᴀᴛᴀʙᴀsᴇ ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ💗")