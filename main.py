#!/usr/bin/env python3
"""
Ryzen Music Bot - Ultra-fast Telegram Music Bot
Main entry point for the application
"""

import asyncio
import importlib
import sys
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Tune import LOGGER, app, userbot, init_ryzen
from Tune.core.call import Ryzen
from Tune.misc import SUDOERS
from Tune.plugins import ALL_MODULES
from Tune.utils.database import get_banned_users, get_gbanned


async def main():
    """Main application entry point"""
    try:
        # Initialize core components
        await init_ryzen()
        
        # Check Spotify configuration
        if not config.SPOTIFY_CLIENT_ID or not config.SPOTIFY_CLIENT_SECRET:
            LOGGER(__name__).warning(
                "Spotify credentials not configured. Spotify features will be disabled."
            )

        # Load banned users
        try:
            banned_users = await get_gbanned()
            for user_id in banned_users:
                config.BANNED_USERS.add(user_id)
            
            banned_users = await get_banned_users()
            for user_id in banned_users:
                config.BANNED_USERS.add(user_id)
        except Exception as e:
            LOGGER(__name__).warning(f"Failed to load banned users: {e}")

        # Start bot and userbot
        await app.start()
        await userbot.start()
        
        # Import all plugins
        for module in ALL_MODULES:
            try:
                importlib.import_module(f"Tune.plugins{module}")
            except Exception as e:
                LOGGER(__name__).error(f"Failed to import {module}: {e}")

        LOGGER("Tune.plugins").info("Successfully imported all modules")
        
        # Start PyTgCalls
        await Ryzen.start()
        
        # Test stream call
        try:
            await Ryzen.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
        except NoActiveGroupCall:
            LOGGER("Tune").error(
                "Please turn on voice chat in your log group/channel.\n\nStopping Bot..."
            )
            return
        except Exception as e:
            LOGGER(__name__).warning(f"Stream test failed: {e}")
        
        # Setup decorators
        await Ryzen.decorators()
        
        LOGGER("Tune").info("🎵 Ryzen Music Bot Started Successfully! 🎵")
        await idle()
        
    except Exception as e:
        LOGGER(__name__).error(f"Failed to start bot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())