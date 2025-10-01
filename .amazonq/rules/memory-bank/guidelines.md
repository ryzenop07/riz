# Ryzen Music Bot - Development Guidelines

## Code Quality Standards

### Import Organization (10/10 files follow this pattern)
- **Standard library imports first**: `import asyncio`, `import os`, `from typing import Dict`
- **Third-party imports second**: `from pyrogram import filters`, `import spotipy`
- **Local imports last**: `from Tune import app`, `from utils.database import get_users`
- **Blank lines separate import groups**

### Function Documentation (8/10 files follow this pattern)
```python
async def add_served_user(user_id: int, name: str, username: str = None):
    """Add new user to database"""
    # Implementation
```
- **Docstrings for all public functions**: Brief, descriptive purpose
- **Type hints consistently used**: Parameters and return types specified
- **Optional parameters with defaults**: `username: str = None`

### Error Handling Patterns (9/10 files follow this pattern)
```python
try:
    # Main operation
    await operation()
except Exception:
    # Graceful fallback or pass
    pass
```
- **Broad exception catching**: `except Exception:` for resilience
- **Silent failures preferred**: `pass` instead of logging for non-critical operations
- **Fallback mechanisms**: Alternative methods when primary fails

## Semantic Patterns

### Database Operations (10/10 files use this pattern)
```python
await collection.update_one(
    {"user_id": user_id},
    {"$set": data},
    upsert=True
)
```
- **Upsert pattern**: `upsert=True` for all user/chat operations
- **Async/await throughout**: All database operations are async
- **MongoDB aggregation**: Complex queries use aggregation pipeline

### Configuration Management (10/10 files follow this pattern)
```python
SETTING = getenv("SETTING", "default_value")
NUMERIC_SETTING = int(getenv("NUMERIC_SETTING", "123"))
LIST_SETTING = list(map(int, getenv("LIST_SETTING", "").split()))
```
- **Environment variables with defaults**: Always provide fallback values
- **Type conversion**: `int()`, `list(map(int, ...))` for proper types
- **Empty string handling**: `.split()` on potentially empty strings

### Pyrogram Command Handlers (8/10 files use this pattern)
```python
@app.on_message(filters.command("command") & filters.group)
@decorator
async def command_handler(client, message: Message, _):
    # Handler implementation
```
- **Decorator stacking**: Multiple decorators for permissions and language
- **Filter combinations**: `filters.command() & filters.group`
- **Consistent parameters**: `client, message, _` (underscore for language strings)

### Inline Keyboard Patterns (7/10 files follow this pattern)
```python
buttons = [
    [
        InlineKeyboardButton("Text", callback_data="data"),
        InlineKeyboardButton("URL", url="https://example.com"),
    ],
    [
        InlineKeyboardButton("Single Button", callback_data="single"),
    ]
]
reply_markup = InlineKeyboardMarkup(buttons)
```
- **Nested list structure**: Each row is a list of buttons
- **Mixed button types**: callback_data and url buttons combined
- **Consistent naming**: `buttons` variable, `InlineKeyboardMarkup` wrapper

### Async Class Initialization (6/10 files use this pattern)
```python
class APIClass:
    def __init__(self):
        self.client = None
        self.cache = {}
        
    async def load_config(self):
        # Async initialization logic
```
- **Sync __init__ with basic setup**: Initialize basic attributes
- **Separate async initialization**: `async def load_config()` or similar
- **Caching mechanisms**: `self.cache = {}` for performance

### Rate Limiting and Performance (8/10 files implement this)
```python
await asyncio.sleep(0.1)  # Rate limiting
# Update status every 50 messages
if (count) % 50 == 0:
    await update_status()
```
- **Sleep for rate limiting**: `asyncio.sleep(0.1)` between operations
- **Batch status updates**: Update UI every N operations, not every operation
- **Performance-conscious loops**: Avoid excessive API calls

### Cookie and Authentication Management (5/10 files use this pattern)
```python
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
if self.cookies:
    headers['Cookie'] = cookie_manager.get_cookie_header(self.cookies)
```
- **User-Agent spoofing**: Consistent browser user agent
- **Conditional cookie headers**: Only add cookies if available
- **Centralized cookie management**: `cookie_manager` utility class

## Internal API Usage Patterns

### Database Abstraction Layer
```python
# User management
await add_served_user(user_id, name, username)
await update_user_activity(user_id)
await get_users_count()

# Broadcast system
await add_broadcast_user(user_id)
await get_broadcast_users()
```
- **Consistent function naming**: `add_`, `get_`, `update_`, `remove_` prefixes
- **Separation of concerns**: Different functions for different entity types
- **Automatic user tracking**: Add users to broadcast list on interaction

### Streaming and Media Handling
```python
# Stream initialization
stream = AudioPiped(link) if not video else VideoPiped(link)
await self.pytgcalls.play(chat_id, stream)

# Platform integration
details, track_id = await stream(_, mystic, user_id, query, chat_id, name, msg_id, "music")
```
- **Conditional stream types**: AudioPiped vs VideoPiped based on content
- **Unified stream function**: Single function handles all streaming logic
- **Error propagation**: Let exceptions bubble up for handling

### Message and UI Patterns
```python
mystic = await message.reply_text("Loading...")
# Processing
await mystic.edit_text("Updated content")
await mystic.delete()
```
- **Loading messages**: Show immediate feedback with placeholder
- **Progressive updates**: Edit messages to show progress
- **Cleanup**: Delete temporary messages after completion

## Code Idioms and Conventions

### String Formatting (9/10 files use f-strings)
```python
f"🎵 Hey {user.first_name}!"
f"📊 Progress: {success_count + failed_count}/{total_targets}"
```
- **F-string preference**: Modern string formatting throughout
- **Emoji integration**: Consistent emoji usage in user messages
- **Mathematical expressions**: Calculations within f-strings

### List Comprehensions and Async Generators (7/10 files use this)
```python
users = [user["user_id"] async for user in users_cursor]
results = [item for item in data.get("items", [])]
```
- **Async list comprehensions**: For database cursors
- **Safe dictionary access**: `.get("key", [])` with defaults
- **Generator expressions**: Memory-efficient data processing

### Configuration Validation (6/10 files implement this)
```python
if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
    LOGGER.warning("Spotify credentials missing")
    self.client = None
```
- **Graceful degradation**: Disable features when credentials missing
- **Logging warnings**: Inform about missing optional features
- **Conditional initialization**: Only initialize when credentials available

### Modular Plugin Architecture
```python
# Plugin registration
@app.on_message(filters.command("command"))
async def handler(client, message):
    pass

# Module imports
for module in ALL_MODULES:
    importlib.import_module(f"Tune.plugins{module}")
```
- **Decorator-based registration**: Commands registered via decorators
- **Dynamic module loading**: Import all plugins programmatically
- **Centralized module list**: `ALL_MODULES` contains all plugin names