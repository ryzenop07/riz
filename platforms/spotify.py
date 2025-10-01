import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

class SpotifyAPI:
    def __init__(self):
        if config.SPOTIFY_CLIENT_ID and config.SPOTIFY_CLIENT_SECRET:
            self.client = spotipy.Spotify(
                client_credentials_manager=SpotifyClientCredentials(
                    client_id=config.SPOTIFY_CLIENT_ID,
                    client_secret=config.SPOTIFY_CLIENT_SECRET
                )
            )
        else:
            self.client = None

    async def search(self, query: str, limit: int = 1):
        """Search Spotify tracks"""
        if not self.client:
            return []
        
        try:
            results = self.client.search(q=query, type="track", limit=limit)
            tracks = []
            
            for track in results["tracks"]["items"]:
                tracks.append({
                    "id": track["id"],
                    "title": track["name"],
                    "artist": track["artists"][0]["name"],
                    "duration": track["duration_ms"] // 1000,
                    "thumbnail": track["album"]["images"][0]["url"] if track["album"]["images"] else "",
                    "spotify_url": track["external_urls"]["spotify"],
                })
            
            return tracks
        except:
            return []

    async def get_playlist(self, playlist_id: str, limit: int = 25):
        """Get Spotify playlist tracks"""
        if not self.client:
            return []
        
        try:
            results = self.client.playlist_tracks(playlist_id, limit=limit)
            tracks = []
            
            for item in results["items"]:
                track = item["track"]
                if track:
                    tracks.append({
                        "id": track["id"],
                        "title": track["name"],
                        "artist": track["artists"][0]["name"],
                        "duration": track["duration_ms"] // 1000,
                        "thumbnail": track["album"]["images"][0]["url"] if track["album"]["images"] else "",
                    })
            
            return tracks
        except:
            return []

spotify = SpotifyAPI()