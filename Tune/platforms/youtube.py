import asyncio
import yt_dlp
from typing import Dict, List
from Tune.utils.cookies import cookie_manager
import config

class YouTubeAPI:
    def __init__(self):
        self.pastebin_url = config.YOUTUBE_COOKIES_URL if hasattr(config, 'YOUTUBE_COOKIES_URL') else None
        self.cookies = {}
        
        # Base yt-dlp options
        self.ydl_opts = {
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "quiet": True,
            "no_warnings": True,
            "extractflat": False,
            "writethumbnail": False,
            "writeinfojson": False,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "http_headers": {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }

    async def load_cookies(self):
        """Load cookies from pastebin or local file"""
        self.cookies = await cookie_manager.get_cookies(self.pastebin_url)
        
        if self.cookies:
            # Update yt-dlp options with cookies
            cookie_header = cookie_manager.get_cookie_header(self.cookies)
            self.ydl_opts['http_headers']['Cookie'] = cookie_header
            
            # Also set cookiefile if local file exists
            import os
            if os.path.exists("cookies/youtube.txt"):
                self.ydl_opts['cookiefile'] = "cookies/youtube.txt"

    async def search(self, query: str, limit: int = 1) -> List[Dict]:
        """Direct yt-dlp search without external APIs"""
        try:
            await self.load_cookies()
            
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)
                results = []
                
                for entry in info.get("entries", []):
                    results.append({
                        "id": entry.get("id"),
                        "title": entry.get("title"),
                        "duration": entry.get("duration", 0),
                        "thumbnail": entry.get("thumbnail"),
                        "url": entry.get("url"),
                        "uploader": entry.get("uploader"),
                        "view_count": entry.get("view_count", 0),
                    })
                
                return results
        except Exception:
            return []

    async def get_download_url(self, video_id: str) -> str:
        """Get direct download URL with cookies"""
        try:
            await self.load_cookies()
            
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(f"https://youtube.com/watch?v={video_id}", download=False)
                return info.get("url", "")
        except:
            return ""

    async def get_playlist(self, playlist_url: str, limit: int = 25) -> List[Dict]:
        """Get playlist tracks with cookies"""
        try:
            await self.load_cookies()
            
            opts = self.ydl_opts.copy()
            opts["playlistend"] = limit
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(playlist_url, download=False)
                results = []
                
                for entry in info.get("entries", []):
                    if entry:
                        results.append({
                            "id": entry.get("id"),
                            "title": entry.get("title"),
                            "duration": entry.get("duration", 0),
                            "thumbnail": entry.get("thumbnail"),
                            "url": entry.get("url"),
                        })
                
                return results
        except:
            return []

youtube = YouTubeAPI()