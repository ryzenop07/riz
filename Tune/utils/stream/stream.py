import asyncio
import os
import yt_dlp
from pyrogram.types import Message
from Tune.core.call import Ryzen

# Ultra-fast streaming configuration
ydl_opts = {
    "format": "bestaudio[ext=m4a]/bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "extractflat": False,
    "writethumbnail": True,
}

async def stream(_, mystic: Message, user_id: int, query: str, chat_id: int, user_name: str, message_id: int, streamtype: str):
    try:
        # Ultra-fast YouTube processing
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            if not info["entries"]:
                raise Exception("No results found")
            
            entry = info["entries"][0]
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
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            if info["entries"]:
                return info["entries"][0]
    except:
        return None