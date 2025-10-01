import os
import requests
import aiohttp
import asyncio
from typing import Dict, Optional

class CookieManager:
    def __init__(self):
        self.cookies_file = "cookies/youtube.txt"
        self.pastebin_url = None
        self.cookies_cache = {}
        
    async def load_cookies_from_file(self) -> Dict:
        """Load cookies from local file"""
        try:
            if os.path.exists(self.cookies_file):
                cookies = {}
                with open(self.cookies_file, 'r') as f:
                    for line in f:
                        if line.startswith('#') or not line.strip():
                            continue
                        parts = line.strip().split('\t')
                        if len(parts) >= 7:
                            cookies[parts[5]] = parts[6]
                return cookies
        except:
            pass
        return {}
    
    async def load_cookies_from_pastebin(self, url: str) -> Dict:
        """Load cookies from pastebin URL"""
        try:
            # Convert pastebin.com URL to raw format
            if "pastebin.com/" in url and "/raw/" not in url:
                paste_id = url.split("/")[-1]
                url = f"https://pastebin.com/raw/{paste_id}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        content = await response.text()
                        cookies = {}
                        
                        for line in content.split('\n'):
                            if line.startswith('#') or not line.strip():
                                continue
                            parts = line.strip().split('\t')
                            if len(parts) >= 7:
                                cookies[parts[5]] = parts[6]
                        
                        # Cache cookies locally
                        with open(self.cookies_file, 'w') as f:
                            f.write(content)
                        
                        return cookies
        except Exception as e:
            print(f"Failed to load cookies from pastebin: {e}")
        return {}
    
    async def get_cookies(self, pastebin_url: Optional[str] = None) -> Dict:
        """Get cookies with priority: pastebin -> local file -> cache"""
        
        # Try pastebin first if URL provided
        if pastebin_url:
            cookies = await self.load_cookies_from_pastebin(pastebin_url)
            if cookies:
                self.cookies_cache = cookies
                return cookies
        
        # Try local file
        cookies = await self.load_cookies_from_file()
        if cookies:
            self.cookies_cache = cookies
            return cookies
        
        # Return cached cookies
        return self.cookies_cache
    
    def get_cookie_header(self, cookies: Dict) -> str:
        """Convert cookies dict to header string"""
        return '; '.join([f'{k}={v}' for k, v in cookies.items()])

# Global cookie manager instance
cookie_manager = CookieManager()