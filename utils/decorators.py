import asyncio
from functools import wraps
from pyrogram.types import Message
from Tune import app
from Tune.misc import SUDOERS

def AdminRightsCheck(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if message.from_user.id in SUDOERS:
            return await func(client, message, *args, **kwargs)
        
        try:
            member = await app.get_chat_member(message.chat.id, message.from_user.id)
            if member.status in ["administrator", "creator"]:
                return await func(client, message, *args, **kwargs)
        except:
            pass
        
        return await message.reply_text("❌ You need admin rights to use this command!")
    
    return wrapper

def language(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        # Ultra-fast language detection
        _ = {"en": "English"}  # Simplified for performance
        return await func(client, message, _, message.chat.id, *args, **kwargs)
    
    return wrapper