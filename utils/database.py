from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from datetime import datetime
import config

# MongoDB Connection
TEMP_MONGODB = "mongodb+srv://ryzenmusic:ryzenmusic@cluster0.mongodb.net/?retryWrites=true&w=majority"

if config.MONGO_DB_URI is None:
    MONGO_DB_URI = TEMP_MONGODB
else:
    MONGO_DB_URI = config.MONGO_DB_URI

mongo = AsyncIOMotorClient(MONGO_DB_URI)
db = mongo.RyzenMusic

# Collections
usersdb = db.users
chatsdb = db.chats
sudoersdb = db.sudoers
blacklist_chatdb = db.blacklistChat
blacklist_userdb = db.blacklistUser
blockeddb = db.blocked
authdb = db.authuser
onoffdb = db.onoffper
langdb = db.language
assdb = db.assistants
autoenddb = db.autoend
countdb = db.upcount
cleandb = db.cleanmode
playmodedb = db.playmode
playtypedb = db.playtype
skipdb = db.skipmode
broadcastdb = db.broadcast

# User Management
async def add_served_user(user_id: int, name: str, username: str = None):
    """Add new user to database"""
    user_data = {
        "user_id": user_id,
        "name": name,
        "username": username,
        "joined_date": datetime.now(),
        "total_plays": 0,
        "last_active": datetime.now()
    }
    await usersdb.update_one(
        {"user_id": user_id}, 
        {"$set": user_data}, 
        upsert=True
    )

async def get_served_users() -> list:
    """Get all served users"""
    users = usersdb.find({"user_id": {"$gt": 0}})
    return [user["user_id"] async for user in users]

async def get_users_count() -> int:
    """Get total users count"""
    return await usersdb.count_documents({"user_id": {"$gt": 0}})

async def update_user_activity(user_id: int):
    """Update user last activity"""
    await usersdb.update_one(
        {"user_id": user_id},
        {"$set": {"last_active": datetime.now()}, "$inc": {"total_plays": 1}}
    )

# Chat Management  
async def add_served_chat(chat_id: int, chat_name: str, chat_type: str):
    """Add new chat to database"""
    chat_data = {
        "chat_id": chat_id,
        "chat_name": chat_name,
        "chat_type": chat_type,
        "joined_date": datetime.now(),
        "total_plays": 0,
        "is_active": True
    }
    await chatsdb.update_one(
        {"chat_id": chat_id},
        {"$set": chat_data},
        upsert=True
    )

async def get_served_chats() -> list:
    """Get all served chats"""
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    return [chat["chat_id"] async for chat in chats]

async def get_chats_count() -> int:
    """Get total chats count"""
    return await chatsdb.count_documents({"chat_id": {"$lt": 0}})

async def remove_served_chat(chat_id: int):
    """Remove chat from database"""
    await chatsdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"is_active": False}}
    )

# Broadcast Management
async def add_broadcast_user(user_id: int):
    """Add user to broadcast list"""
    await broadcastdb.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id, "type": "user", "active": True}},
        upsert=True
    )

async def add_broadcast_chat(chat_id: int):
    """Add chat to broadcast list"""
    await broadcastdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"chat_id": chat_id, "type": "chat", "active": True}},
        upsert=True
    )

async def get_broadcast_users() -> list:
    """Get all broadcast users"""
    users = broadcastdb.find({"type": "user", "active": True})
    return [user["user_id"] async for user in users]

async def get_broadcast_chats() -> list:
    """Get all broadcast chats"""
    chats = broadcastdb.find({"type": "chat", "active": True})
    return [chat["chat_id"] async for chat in chats]

async def remove_broadcast_user(user_id: int):
    """Remove user from broadcast"""
    await broadcastdb.update_one(
        {"user_id": user_id},
        {"$set": {"active": False}}
    )

# Ban Management
async def get_banned_users() -> list:
    users = blacklist_userdb.find({"user_id": {"$gt": 0}})
    return [user["user_id"] async for user in users]

async def get_gbanned() -> list:
    users = blacklist_userdb.find({"user_id": {"$lt": 0}})
    return [user["user_id"] async for user in users]

async def is_banned_user(user_id: int) -> bool:
    user = await blacklist_userdb.find_one({"user_id": user_id})
    return bool(user)

async def add_banned_user(user_id: int):
    await blacklist_userdb.update_one(
        {"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True
    )

async def remove_banned_user(user_id: int):
    await blacklist_userdb.delete_one({"user_id": user_id})

# Assistant Management
async def get_assistant(chat_id: int) -> str:
    assistant = await assdb.find_one({"chat_id": chat_id})
    return assistant["assistant"] if assistant else "1"

async def save_assistant(chat_id: int, number: str):
    await assdb.update_one(
        {"chat_id": chat_id}, {"$set": {"assistant": number}}, upsert=True
    )

# Statistics
async def get_global_stats():
    """Get global bot statistics"""
    total_users = await get_users_count()
    total_chats = await get_chats_count()
    total_plays = await usersdb.aggregate([
        {"$group": {"_id": None, "total": {"$sum": "$total_plays"}}}
    ]).to_list(1)
    
    plays_count = total_plays[0]["total"] if total_plays else 0
    
    return {
        "users": total_users,
        "chats": total_chats,
        "plays": plays_count
    }