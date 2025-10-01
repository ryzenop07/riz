#!/usr/bin/env python3

import asyncio
from pyrogram import Client

print("🎵 Ryzen Music - Session String Generator")
print("=" * 40)

API_ID = int(input("Enter API_ID: "))
API_HASH = input("Enter API_HASH: ")

async def generate_session():
    async with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as app:
        session_string = await app.export_session_string()
        print(f"\n✅ Your Session String:\n{session_string}")
        print("\n📝 Add this to your .env file as STRING1")

if __name__ == "__main__":
    asyncio.run(generate_session())