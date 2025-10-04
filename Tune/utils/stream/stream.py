import asyncio
import os
import yt_dlp
from pyrogram.types import Message
from Tune.core.call import Ryzen
from Tune.platforms.youtube import youtube

async def stream(_, mystic: Message, user_id: int, query: str, chat_id: int, user_name: str, message_id: int, streamtype: str):
    try:
        # Direct YouTube search without external APIs
        results = await youtube.search(query, 1)
        
        if not results:
            raise Exception("No results found")
        
        entry = results[0]
        title = entry.get("title", "Unknown")
        duration = entry.get("duration", 0)
        thumbnail = entry.get("thumbnail", "")
        url = entry.get("url", "")
        
        # Start streaming immediately
        if streamtype == "video":
            await Ryzen.join_call(
                chat_id, chat_id, url, video=True
            )
        else:
            await Ryzen.join_call(
                chat_id, chat_id, url
            )
        
        details = {
            "title": title,
            "duration_sec": duration,
            "thumb": thumbnail,
            "url": url
        }
        
        return details, entry.get("id", "")
        
    except Exception as e:
        raise Exception(f"Streaming failed: {str(e)}")

async def download_track(query: str):
    """Ultra-fast track download"""
    try:
        results = await youtube.search(query, 1)
        if results:
            return results[0]
    except:
        return None