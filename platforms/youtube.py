import asyncio
import yt_dlp
import requests
from typing import Dict, List
from utils.cookies import cookie_manager
import config

class YouTubeAPI:
    def __init__(self):
        self.api_key = config.YOUTUBE_API_KEY
        self.pastebin_url = config.YOUTUBE_COOKIES_URL if hasattr(config, 'YOUTUBE_COOKIES_URL') else None
        self.base_url = "https://www.googleapis.com/youtube/v3"
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
            if os.path.exists("cookies/youtube.txt"):
                self.ydl_opts['cookiefile'] = "cookies/youtube.txt"

    async def search_api(self, query: str, limit: int = 1) -> List[Dict]:
        """Search using YouTube Data API with cookies"""
        try:
            await self.load_cookies()
            
            url = f"{self.base_url}/search"
            params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'maxResults': limit,
                'key': self.api_key,
                'videoCategoryId': '10'
            }
            
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            if self.cookies:
                headers['Cookie'] = cookie_manager.get_cookie_header(self.cookies)
            
            response = requests.get(url, params=params, headers=headers, timeout=10)
            data = response.json()
            
            results = []
            for item in data.get('items', []):
                video_id = item['id']['videoId']
                snippet = item['snippet']
                
                # Get video details
                details_url = f"{self.base_url}/videos"
                details_params = {
                    'part': 'contentDetails,statistics',
                    'id': video_id,
                    'key': self.api_key
                }
                
                details_response = requests.get(details_url, params=details_params, headers=headers, timeout=5)
                details_data = details_response.json()
                
                duration = 0
                if details_data.get('items'):
                    duration_str = details_data['items'][0]['contentDetails']['duration']
                    duration = self._parse_duration(duration_str)
                
                results.append({
                    "id": video_id,
                    "title": snippet['title'],
                    "duration": duration,
                    "thumbnail": snippet['thumbnails']['high']['url'],
                    "url": f"https://youtube.com/watch?v={video_id}",
                    "uploader": snippet['channelTitle'],
                    "view_count": int(details_data['items'][0]['statistics'].get('viewCount', 0)) if details_data.get('items') else 0,
                })
            
            return results
        except Exception:
            return await self.search_fallback(query, limit)

    async def search_fallback(self, query: str, limit: int = 1) -> List[Dict]:
        """Fallback search using yt-dlp with cookies"""
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

    async def search(self, query: str, limit: int = 1) -> List[Dict]:
        """Main search method with API and cookies"""
        if self.api_key and self.api_key != "AIzaSyDcWKhJQIJlOaOPWGz8QqQqQqQqQqQqQqQ":
            return await self.search_api(query, limit)
        return await self.search_fallback(query, limit)

    def _parse_duration(self, duration_str: str) -> int:
        """Parse ISO 8601 duration to seconds"""
        import re
        pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'
        match = re.match(pattern, duration_str)
        if match:
            hours = int(match.group(1) or 0)
            minutes = int(match.group(2) or 0)
            seconds = int(match.group(3) or 0)
            return hours * 3600 + minutes * 60 + seconds
        return 0

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