import asyncio
import socket
from typing import Dict, List

import heroku3
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config

# Sudo Users Management
SUDOERS = config.OWNER_ID + config.SUDO_USERS

# Performance Cache
CACHE: Dict = {}

# Active Chats
ACTIVE_CHATS: List[int] = []

# Auto-end Configuration
AUTO_END_TIME = 1

# Heroku Integration
if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
    heroku_conn = heroku3.from_key(config.HEROKU_API_KEY)
    heroku_app = heroku_conn.apps()[config.HEROKU_APP_NAME]
else:
    heroku_app = None

# Network Optimization
def is_heroku():
    return "heroku" in socket.getfqdn()

# Performance Utilities
async def sudo():
    return SUDOERS

def make_col(key):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🔙 Back",
                    callback_data=f"settingsback_helper",
                ),
                InlineKeyboardButton(
                    text="🗑 Close", callback_data=f"close"
                ),
            ]
        ]
    )