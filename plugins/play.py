import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_dl import YoutubeDL

from Tune import app
from Tune.core.call import Ryzen
from Tune.utils.decorators import AdminRightsCheck
from Tune.utils.inline.play import stream_markup, telegram_markup
from Tune.utils.stream.stream import stream

@app.on_message(filters.command(["play", "p"]) & filters.group)
@AdminRightsCheck
async def play_commnd(client, message: Message, _, chat_id):
    if len(message.command) < 2:
        return await message.reply_text(_["playback_2"])
    
    query = message.text.split(None, 1)[1]
    mystic = await message.reply_text(_["play_1"])
    
    try:
        # Ultra-fast streaming logic
        details, track_id = await stream(
            _,
            mystic,
            message.from_user.id,
            query,
            chat_id,
            message.from_user.first_name,
            message.message_id,
            streamtype="music",
        )
    except Exception as e:
        ex_type = type(e).__name__
        err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
        return await mystic.edit_text(err)
    
    await mystic.delete()
    thumbnail = details["thumb"]
    duration = details["duration_sec"]
    buttons = stream_markup(_, chat_id)
    
    await message.reply_photo(
        photo=thumbnail,
        caption=_["stream_1"].format(
            message.from_user.first_name,
            f"https://t.me/{app.username}?startgroup=true",
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_message(filters.command(["vplay", "vp"]) & filters.group)
@AdminRightsCheck  
async def video_play_commnd(client, message: Message, _, chat_id):
    if len(message.command) < 2:
        return await message.reply_text(_["playback_2"])
    
    query = message.text.split(None, 1)[1]
    mystic = await message.reply_text(_["play_1"])
    
    try:
        details, track_id = await stream(
            _,
            mystic,
            message.from_user.id,
            query,
            chat_id,
            message.from_user.first_name,
            message.message_id,
            streamtype="video",
        )
    except Exception as e:
        ex_type = type(e).__name__
        err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
        return await mystic.edit_text(err)
    
    await mystic.delete()
    thumbnail = details["thumb"]
    buttons = stream_markup(_, chat_id)
    
    await message.reply_photo(
        photo=thumbnail,
        caption=_["stream_1"].format(
            message.from_user.first_name,
            f"https://t.me/{app.username}?startgroup=true",
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )