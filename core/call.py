import asyncio
from typing import Union
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls, filters
from pytgcalls.types import AudioPiped, VideoPiped
from pytgcalls.exceptions import NoActiveGroupCall

from Tune import app, userbot
from Tune.utils.database import get_assistant


class RyzenCall:
    def __init__(self):
        self.pytgcalls = PyTgCalls(userbot, cache_duration=100)
        self.cache = {}

    async def pause_stream(self, chat_id: int):
        try:
            await self.pytgcalls.pause_stream(chat_id)
        except:
            pass

    async def resume_stream(self, chat_id: int):
        try:
            await self.pytgcalls.resume_stream(chat_id)
        except:
            pass

    async def stop_stream(self, chat_id: int):
        try:
            await self.pytgcalls.leave_group_call(chat_id)
        except:
            pass

    async def force_stop_stream(self, chat_id: int):
        try:
            await self.pytgcalls.leave_group_call(chat_id)
        except:
            pass

    async def skip_stream(
        self,
        chat_id: int,
        link: str,
        video: Union[bool, str] = None,
        image: Union[bool, str] = None,
    ):
        if video:
            stream = VideoPiped(link)
        else:
            stream = AudioPiped(link)
        try:
            await self.pytgcalls.change_stream(
                chat_id,
                stream,
            )
        except Exception:
            return False
        return True

    async def seek_stream(self, chat_id, file_path, to_seek, duration, mode):
        stream = (
            VideoPiped(
                file_path,
                additional_ffmpeg_parameters=f"-ss {to_seek} -t {duration}",
            )
            if mode == "video"
            else AudioPiped(
                file_path,
                additional_ffmpeg_parameters=f"-ss {to_seek} -t {duration}",
            )
        )
        try:
            await self.pytgcalls.change_stream(chat_id, stream)
        except Exception:
            return False
        return True

    async def stream_call(self, link):
        try:
            await self.pytgcalls.play(
                app.me.id,
                AudioPiped(link),
            )
        except Exception:
            return False
        return True

    async def join_call(
        self,
        chat_id: int,
        original_chat_id: int,
        link,
        video: Union[bool, str] = None,
        image: Union[bool, str] = None,
    ):
        if video:
            stream = VideoPiped(link)
        else:
            stream = AudioPiped(link)
        try:
            await self.pytgcalls.play(
                chat_id,
                stream,
            )
        except NoActiveGroupCall:
            try:
                await userbot.invoke(
                    {
                        "_": "phone.CreateGroupCall",
                        "peer": await userbot.resolve_peer(chat_id),
                        "random_id": randint(10000, 999999999),
                    }
                )
                await self.pytgcalls.play(
                    chat_id,
                    stream,
                )
            except Exception:
                return False
        except Exception:
            return False
        return True

    async def change_stream(self, client, path):
        try:
            await self.pytgcalls.change_stream(
                client,
                AudioPiped(path),
            )
        except Exception:
            return False
        return True

    async def start(self):
        await self.pytgcalls.start()

    async def decorators(self):
        @self.pytgcalls.on_stream_end()
        async def stream_end_handler(client, update):
            if not isinstance(update, StreamAudioEnded):
                return
            await auto_end(client, update, self.pytgcalls)

Ryzen = RyzenCall()