import asyncio
import importlib
import sys
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Tune import LOGGER, app, userbot, init_ryzen
from Tune.core.call import Ryzen
from Tune.misc import sudo
from Tune.plugins import ALL_MODULES
from Tune.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # Initialize core components
    await init_ryzen()
    
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER(__name__).warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Tune.plugins" + all_module)

    LOGGER("Tune.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Ryzen.start()
    
    try:
        await Ryzen.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Tune").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        return
    except:
        pass
    
    await Ryzen.decorators()
    LOGGER("Tune").info("🎵 Ryzen Music Bot Started Successfully! 🎵")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())