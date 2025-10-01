import os
from os import getenv

# Bot Configuration
API_ID = int(getenv("API_ID", "24395647"))
API_HASH = getenv("API_HASH", "0aa759ca1e37cf5efd89348df8b01ff3")
BOT_TOKEN = getenv("BOT_TOKEN", "7693545148:AAFwup45Pkyt0-LIORAUaCsz-GrN6ttDjGs")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ajay211st:vish123@musicbot.e8zz328.mongodb.net/?retryWrites=true&w=majority&appName=musicbot")
LOG_GROUP_ID = int(getenv("LOGGER_ID", "-1002332612274"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Ryzen Music")

# Owner & Sudo Configuration
OWNER_ID = list(map(int, getenv("OWNER_ID", "7850496630").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

# Assistant Configuration
STRING1 = getenv("STRING_SESSION", "BQF0P38AMTQEY1OHowsL6jNLAlg-P1wjZ5uQVo_XkGjpLJdcTm9ZvVGwjW1wypCXL2npqcOIpxMfXMqn403xnHyAdgLEZKcdvnVZFeovz4RODXhFkkSRYyPi9etJ65PGf5WfsAaDbOW3n9Wmioka1xj15aYoEP0cGwA1Sx6aaCW92K8sh7EZTLbcnDjeyehsV3RvHmuS5YZt5RtP24bH-aBle78qd6YzXTudS_yF-U5eETHk9LmK1694F8KjK7VYbgeX-qcNk5KEMrYGgTZ7R4AOlbG0FWFgU1UMQqdZxDdtZPBiXFaDkHB5zcKAEqmZXiAs8iWjTXIBuG_OoXbPJammrbcGlwAAAAHT7RJ2AA")
STRING2 = getenv("STRING2", "")
STRING3 = getenv("STRING3", "")
STRING4 = getenv("STRING4", "")
STRING5 = getenv("STRING5", "")

# API Keys for Enhanced Performance
YOUTUBE_API_KEY = getenv("API_KEY", "NxGBNexGenBots3fd157")
GENIUS_ACCESS_TOKEN = getenv("GENIUS_ACCESS_TOKEN", "")

# YouTube Cookies - Pastebin URL
YOUTUBE_COOKIES_URL = getenv("COOKIE_URL", "https://pastebin.com/ipRp9jwe")

# Support Configuration
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ryzensupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Ryzen_supportxc")

# Performance Optimization
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "180"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Auto Leaving Configuration
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))

# Spotify Configuration
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# GitHub Configuration
GIT_TOKEN = getenv("GIT_TOKEN", "")
REPO_URL = getenv("REPO_URL", "https://github.com/RyzenMusic/RyzenMusic")

# Heroku Configuration
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")

# Performance Settings
PREFETCH_PLAYLIST = True
CACHE_SIZE = 100
MAX_CONCURRENT_DOWNLOADS = 3
STREAM_QUALITY = "high"

# User Tracking
AUTO_ADD_USERS = True
BROADCAST_ON_START = True

# Banned Users List
BANNED_USERS = set()

# Ultra-Fast Configuration
UPSTREAM_REPO = "https://github.com/RyzenMusic/RyzenMusic"
UPSTREAM_BRANCH = "master"

# Advanced Features
ENABLE_LYRICS = True
ENABLE_QUEUE = True
ENABLE_BROADCAST = True
ENABLE_STATS = True