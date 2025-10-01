from pyrogram import Client
from Tune.logging import LOGGER
import config

class RyzenBot:
    def __init__(self):
        self.app = Client(
            "RyzenMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )
        LOGGER(__name__).info("Bot client initialized.")

    async def start(self):
        await self.app.start()
        LOGGER(__name__).info("Bot started successfully.")

    async def stop(self):
        await self.app.stop()
        LOGGER(__name__).info("Bot stopped.")

ryzen_bot = RyzenBot()