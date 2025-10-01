#!/usr/bin/env python3
"""
Pyrogram Session String Generator
Generate session string for Ryzen Music Bot
"""

from pyrogram import Client

print("🎵 Ryzen Music Bot - Session Generator")
print("=" * 50)

API_ID = input("Enter your API ID: ")
API_HASH = input("Enter your API HASH: ")

try:
    with Client("session", api_id=API_ID, api_hash=API_HASH) as app:
        session_string = app.export_session_string()
        print(f"\n✅ Session String Generated Successfully!")
        print(f"📋 Your Session String:")
        print(f"{session_string}")
        print(f"\n⚠️ Keep this session string safe and don't share it!")
        
except Exception as e:
    print(f"❌ Error: {e}")