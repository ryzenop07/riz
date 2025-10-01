from pyrogram import filters
from pyrogram.types import Message
from Tune import app
from Tune.core.call import Ryzen
from Tune.utils.decorators import AdminRightsCheck, language

@app.on_message(filters.command(["pause", "cpause"]) & filters.group)
@AdminRightsCheck
@language
async def pause_command(client, message: Message, _, chat_id):
    await Ryzen.pause_stream(chat_id)
    await message.reply_text("⏸ **Paused**\n\nMusic has been paused!")

@app.on_message(filters.command(["resume", "cresume"]) & filters.group)
@AdminRightsCheck
@language
async def resume_command(client, message: Message, _, chat_id):
    await Ryzen.resume_stream(chat_id)
    await message.reply_text("▶️ **Resumed**\n\nMusic has been resumed!")

@app.on_message(filters.command(["stop", "cstop", "end"]) & filters.group)
@AdminRightsCheck
@language
async def stop_command(client, message: Message, _, chat_id):
    await Ryzen.stop_stream(chat_id)
    await message.reply_text("⏹ **Stopped**\n\nMusic has been stopped and queue cleared!")

@app.on_message(filters.command(["skip", "cskip", "next"]) & filters.group)
@AdminRightsCheck
@language
async def skip_command(client, message: Message, _, chat_id):
    await Ryzen.skip_stream(chat_id, "", video=False)
    await message.reply_text("⏭ **Skipped**\n\nSkipped to next track!")

@app.on_message(filters.command(["mute", "cmute"]) & filters.group)
@AdminRightsCheck
@language
async def mute_command(client, message: Message, _, chat_id):
    await Ryzen.mute_stream(chat_id)
    await message.reply_text("🔇 **Muted**\n\nMusic has been muted!")

@app.on_message(filters.command(["unmute", "cunmute"]) & filters.group)
@AdminRightsCheck
@language
async def unmute_command(client, message: Message, _, chat_id):
    await Ryzen.unmute_stream(chat_id)
    await message.reply_text("🔊 **Unmuted**\n\nMusic has been unmuted!")