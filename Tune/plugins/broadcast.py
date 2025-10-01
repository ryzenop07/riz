import asyncio
from pyrogram import filters
from pyrogram.types import Message
from Tune import app
from Tune.misc import SUDOERS
from Tune.utils.database import get_broadcast_users, get_broadcast_chats

@app.on_message(filters.command("broadcast") & filters.user(SUDOERS))
async def broadcast_message(client, message: Message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**Usage:** /broadcast [message] or reply to a message")
    
    if message.reply_to_message:
        broadcast_msg = message.reply_to_message
        text = broadcast_msg.text or broadcast_msg.caption or ""
    else:
        text = message.text.split(None, 1)[1]
        broadcast_msg = None
    
    if not text and not broadcast_msg:
        return await message.reply_text("❌ No content to broadcast!")
    
    # Get all users and chats
    users = await get_broadcast_users()
    chats = await get_broadcast_chats()
    
    total_targets = len(users) + len(chats)
    
    if total_targets == 0:
        return await message.reply_text("❌ No users or chats to broadcast to!")
    
    status_msg = await message.reply_text(f"📡 **Broadcasting to {total_targets} targets...**")
    
    success_count = 0
    failed_count = 0
    
    # Broadcast to users
    for user_id in users:
        try:
            if broadcast_msg:
                if broadcast_msg.photo:
                    await app.send_photo(user_id, broadcast_msg.photo.file_id, caption=text)
                elif broadcast_msg.video:
                    await app.send_video(user_id, broadcast_msg.video.file_id, caption=text)
                elif broadcast_msg.document:
                    await app.send_document(user_id, broadcast_msg.document.file_id, caption=text)
                elif broadcast_msg.audio:
                    await app.send_audio(user_id, broadcast_msg.audio.file_id, caption=text)
                else:
                    await app.send_message(user_id, text)
            else:
                await app.send_message(user_id, text)
            success_count += 1
        except Exception:
            failed_count += 1
        
        # Update status every 50 messages
        if (success_count + failed_count) % 50 == 0:
            await status_msg.edit_text(
                f"📡 **Broadcasting...**\n"
                f"✅ Success: {success_count}\n"
                f"❌ Failed: {failed_count}\n"
                f"📊 Progress: {success_count + failed_count}/{total_targets}"
            )
        
        await asyncio.sleep(0.1)  # Rate limiting
    
    # Broadcast to chats
    for chat_id in chats:
        try:
            if broadcast_msg:
                if broadcast_msg.photo:
                    await app.send_photo(chat_id, broadcast_msg.photo.file_id, caption=text)
                elif broadcast_msg.video:
                    await app.send_video(chat_id, broadcast_msg.video.file_id, caption=text)
                elif broadcast_msg.document:
                    await app.send_document(chat_id, broadcast_msg.document.file_id, caption=text)
                elif broadcast_msg.audio:
                    await app.send_audio(chat_id, broadcast_msg.audio.file_id, caption=text)
                else:
                    await app.send_message(chat_id, text)
            else:
                await app.send_message(chat_id, text)
            success_count += 1
        except Exception:
            failed_count += 1
        
        await asyncio.sleep(0.1)  # Rate limiting
    
    await status_msg.edit_text(
        f"📡 **Broadcast Completed!**\n\n"
        f"✅ **Success:** {success_count}\n"
        f"❌ **Failed:** {failed_count}\n"
        f"📊 **Total:** {total_targets}"
    )

@app.on_message(filters.command("stats") & filters.user(SUDOERS))
async def bot_stats(client, message: Message):
    from Tune.utils.database import get_global_stats
    
    stats = await get_global_stats()
    users = await get_broadcast_users()
    chats = await get_broadcast_chats()
    
    await message.reply_text(
        f"📊 **Ryzen Music Statistics**\n\n"
        f"👥 **Total Users:** {stats['users']:,}\n"
        f"💬 **Total Chats:** {stats['chats']:,}\n"
        f"🎵 **Total Plays:** {stats['plays']:,}\n"
        f"📡 **Broadcast Users:** {len(users):,}\n"
        f"📡 **Broadcast Chats:** {len(chats):,}"
    )