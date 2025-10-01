from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Tune import app
from Tune.utils.decorators import language
from Tune.utils.database import add_served_user, add_served_chat, add_broadcast_user, add_broadcast_chat, update_user_activity
import config

@app.on_message(filters.command("start") & filters.private)
@language
async def start_command(client, message: Message, _):
    user = message.from_user
    
    # Add user to database and broadcast list
    await add_served_user(user.id, user.first_name, user.username)
    await add_broadcast_user(user.id)
    await update_user_activity(user.id)
    
    buttons = [
        [
            InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton("📚 Commands", callback_data="help_back"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats_back"),
            InlineKeyboardButton("🆘 Support", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton("🔥 Updates", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton("💝 Donate", callback_data="donate"),
        ],
    ]
    
    await message.reply_photo(
        photo="https://te.legra.ph/file/c0e014ff34f34d1056627.png",
        caption=f"""**🎵 Hey {user.first_name}!**

I'm **Ryzen Music**, the fastest Telegram music bot with nanosecond response time!

**🚀 Features:**
• Ultra-fast streaming with API & cookies
• High-quality audio/video playback
• Advanced queue management
• Multi-platform support (YouTube, Spotify)
• Smart user tracking & analytics
• Broadcast system for updates

**🎯 Quick Commands:**
• `/play` - Play any song instantly
• `/vplay` - Play video with audio
• `/queue` - View current playlist
• `/lyrics` - Get song lyrics

**Click the buttons below to get started!**""",
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_message(filters.command("start") & filters.group)
@language  
async def start_group(client, message: Message, _):
    chat = message.chat
    user = message.from_user
    
    # Add chat and user to database
    await add_served_chat(chat.id, chat.title, chat.type)
    await add_served_user(user.id, user.first_name, user.username)
    await add_broadcast_chat(chat.id)
    await add_broadcast_user(user.id)
    
    buttons = [
        [
            InlineKeyboardButton("📚 Help", callback_data="help_back"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("🎵 Play Music", switch_inline_query_current_chat=""),
            InlineKeyboardButton("📊 Stats", callback_data="stats_back"),
        ]
    ]
    
    await message.reply_text(
        f"**🎵 Ryzen Music Started in {chat.title}!**\n\n"
        f"✨ **Ultra-fast music streaming is now active!**\n"
        f"🎯 Use `/play [song name]` to start streaming music instantly!\n\n"
        f"**🔥 Features Available:**\n"
        f"• High-quality audio streaming\n"
        f"• Video playback support\n"
        f"• Smart queue management\n"
        f"• Multi-platform search\n"
        f"• Admin controls & more!",
        reply_markup=InlineKeyboardMarkup(buttons),
    )