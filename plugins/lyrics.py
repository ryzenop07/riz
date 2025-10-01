import lyricsgenius
from pyrogram import filters
from pyrogram.types import Message
from Tune import app
from Tune.utils.decorators import language
import config

# Initialize Genius API (add your token)
genius = lyricsgenius.Genius("your_genius_access_token_here")  # Replace with actual token
genius.verbose = False
genius.remove_section_headers = True

@app.on_message(filters.command(["lyrics", "ly"]))
@language
async def lyrics_command(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:** /lyrics [song name]")
    
    query = message.text.split(None, 1)[1]
    mystic = await message.reply_text("🔍 **Searching for lyrics...**")
    
    try:
        song = genius.search_song(query)
        if song:
            lyrics = song.lyrics
            
            # Split lyrics if too long
            if len(lyrics) > 4096:
                lyrics_parts = [lyrics[i:i+4096] for i in range(0, len(lyrics), 4096)]
                await mystic.edit_text(f"🎵 **{song.title}** by **{song.artist}**\n\n{lyrics_parts[0]}")
                
                for part in lyrics_parts[1:]:
                    await message.reply_text(part)
            else:
                await mystic.edit_text(f"🎵 **{song.title}** by **{song.artist}**\n\n{lyrics}")
        else:
            await mystic.edit_text("❌ **No lyrics found for this song.**")
    
    except Exception as e:
        await mystic.edit_text("❌ **Failed to fetch lyrics. Try again later.**")

@app.on_message(filters.command(["queue", "q"]))
@language  
async def queue_command(client, message: Message, _):
    # Placeholder for queue functionality
    await message.reply_text(
        "📝 **Current Queue**\n\n"
        "🎵 No songs in queue currently.\n"
        "Use `/play [song name]` to add music!"
    )